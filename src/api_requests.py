import concurrent.futures
import time
import requests
import pandas as pd
import json
import logging
from typing import Tuple
from tqdm import tqdm
import os
from dotenv import load_dotenv


def _generate_user_prompt(df_batch: pd.DataFrame, id_column: str = "id", text_column: str = "text") -> str:
    """
    Generates a user prompt to process a batch
    """    
    if id_column not in df_batch.columns:
        raise ValueError(f"ID column '{id_column}' not found in DataFrame")
    if text_column not in df_batch.columns:
        raise ValueError(f"Text column '{text_column}' not found in DataFrame")

    #! Should I make it more generic and not talk about tweets here?
    prompt_lines: list[str] = ["Process these tweets:"]
    
    for _, row in df_batch.iterrows():
        prompt_lines.append(f"ID: {row[id_column]}, Text: {repr(row[text_column])}")
    
    prompt_lines.append("\nReturn JSON in the specified format.")
    return "\n".join(prompt_lines)

def _send_batch_request(system_prompt: str,user_prompt: str, model: str = "deepseek-chat", 
        url: str = "https://api.deepseek.com/v1/chat/completions") -> str:
    """
    Sends a batch of data to the API and returns the response.
    """    
    load_dotenv()
    headers = {
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.1,
        "type": "json_object"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def process_batch(batch_df: pd.DataFrame, system_prompt: str, retries: int = 3, 
                  base_delay: int = 2) -> Tuple[pd.DataFrame, str]:
    """
    Process a single batch of data with retries and exponential backoff.
    """
    for attempt in range(retries):
        try:
            # Generate prompt and make API call
            user_prompt: str = _generate_user_prompt(batch_df)
            return batch_df, _send_batch_request(system_prompt, user_prompt)  # Replace with your API call
            
        except Exception as e:
            if attempt == retries - 1:
                print(f"Batch {batch_df['id'].tolist()[0]} failed running last attempt.")
                return batch_df, f"error: Final failure: {str(e)} on batch: {batch_df['id'].tolist()}"
            time.sleep(base_delay * (2 ** attempt))  # Exponential backoff
        print(f"Batch {batch_df['id'].tolist()[0]} failed running attempt {attempt}")

def parallel_processor(input_df: pd.DataFrame, max_chunks: int, output_file: str, max_workers: int = 10) -> None:
    """
    Process DataFrame in parallel batches
    """
    # Create thread pool with rate limiting
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures: list = []
        for count, chunk in enumerate(input_df):
            if count >= max_chunks:
                break
            futures.append(executor.submit(process_batch, chunk, system_prompt))
        
        # Monitor progress
        with tqdm(total=len(futures)) as pbar:
            for future in concurrent.futures.as_completed(futures):
                result: tuple[pd.DataFrame, str] = future.result()
                chunk_df, batch_result = result
                try:
                    json_batch_result: dict = json.loads(batch_result.strip('```').lstrip('json').strip())
                except json.JSONDecodeError as e:
                    #TODO: I should try to handle the chinese censorship issue
                    #TODO: The way I should do this is probably using a small LLM to replace  
                    #TODO: chinese-sensitive words and then retry the request 
                    #? Also I should probably return the dict itself after checking inside the function
                    logging.error(f"JSON decoding error: {e} for batch: {batch_result}")
                    exit(1)
                batch_df: pd.DataFrame = pd.DataFrame.from_dict(
                    json_batch_result, orient="index", columns=["spam", "emotion", "sentiment"])
                batch_df.index = batch_df.index.astype(int)
                merged_df: pd.DataFrame = chunk_df.merge(batch_df, left_on="id", right_index=True, how="left")
                write_header = not os.path.exists(output_file)
                merged_df.to_csv(output_file, mode='a', index=False, header=write_header)
                pbar.update(1)
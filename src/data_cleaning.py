def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
    """Handle missing values in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to clean.
        strategy (str): The strategy to handle missing values. Options are 'drop' or 'fill'.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(method='ffill')  # Forward fill as an example
    else:
        raise ValueError("Invalid strategy. Use 'drop' or 'fill'.")

def normalize_text(text: str) -> str:
    """Normalize text by converting to lowercase and removing special characters.

    Args:
        text (str): The text to normalize.

    Returns:
        str: The normalized text.
    """
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special characters
    return text

def preprocess_data(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    """Preprocess the DataFrame by handling missing values and normalizing text.

    Args:
        df (pd.DataFrame): The DataFrame to preprocess.
        text_column (str): The name of the text column to normalize.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    df = handle_missing_values(df, strategy='drop')
    df[text_column] = df[text_column].apply(normalize_text)
    return df

def save_processed_data(df: pd.DataFrame, output_path: str) -> None:
    """Save the processed DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The path to save the processed data.
    """
    df.to_csv(output_path, index=False)
import pytest
import pandas as pd
from src.data_cleaning import clean_data  # Adjust the import based on your actual function names

def test_clean_data_removes_nulls():
    # Create a sample DataFrame with null values
    data = {
        'id': [1, 2, 3, 4],
        'text': ['Tweet 1', None, 'Tweet 3', 'Tweet 4']
    }
    df = pd.DataFrame(data)

    # Clean the data
    cleaned_df = clean_data(df)

    # Check that the cleaned DataFrame does not contain nulls
    assert cleaned_df['text'].isnull().sum() == 0

def test_clean_data_normalizes_text():
    # Create a sample DataFrame with mixed case text
    data = {
        'id': [1, 2],
        'text': ['Tweet 1', 'TWEET 2']
    }
    df = pd.DataFrame(data)

    # Clean the data
    cleaned_df = clean_data(df)

    # Check that the text is normalized (e.g., lowercased)
    assert cleaned_df['text'].iloc[0] == 'tweet 1'
    assert cleaned_df['text'].iloc[1] == 'tweet 2'

def test_clean_data_handles_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['id', 'text'])

    # Clean the data
    cleaned_df = clean_data(df)

    # Check that the cleaned DataFrame is still empty
    assert cleaned_df.empty

def test_clean_data_removes_duplicates():
    # Create a sample DataFrame with duplicate rows
    data = {
        'id': [1, 1, 2],
        'text': ['Tweet 1', 'Tweet 1', 'Tweet 2']
    }
    df = pd.DataFrame(data)

    # Clean the data
    cleaned_df = clean_data(df)

    # Check that duplicates are removed
    assert cleaned_df.shape[0] == 2  # Should have 2 unique rows

# Add more tests as needed for other cleaning functions and edge cases
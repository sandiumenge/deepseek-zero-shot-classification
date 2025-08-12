import matplotlib.pyplot as plt
import pandas as pd

def plot_emotion_distribution(df: pd.DataFrame, title: str = "Emotion Distribution"):
    """
    Plots the distribution of emotions in the given DataFrame.

    Parameters:
    - df: DataFrame containing the 'emotion' column.
    - title: Title of the plot.
    """
    emotion_counts = df['emotion'].value_counts(normalize=True) * 100
    plt.figure(figsize=(10, 6))
    emotion_counts.plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel('Emotions')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_sentiment_distribution(df: pd.DataFrame, title: str = "Sentiment Distribution"):
    """
    Plots the distribution of sentiment scores in the given DataFrame.

    Parameters:
    - df: DataFrame containing the 'sentiment' column.
    - title: Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    df['sentiment'].hist(bins=20, color='lightgreen', alpha=0.7)
    plt.title(title)
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_spam_category_distribution(df: pd.DataFrame, title: str = "Spam Category Distribution"):
    """
    Plots the distribution of spam categories in the given DataFrame.

    Parameters:
    - df: DataFrame containing the 'spam' column.
    - title: Title of the plot.
    """
    spam_counts = df['spam'].value_counts(normalize=True) * 100
    plt.figure(figsize=(10, 6))
    spam_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title(title)
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
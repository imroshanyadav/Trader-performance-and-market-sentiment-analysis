import pandas as pd
import numpy as np
from .utils import map_sentiment_to_score

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop rows with missing critical columns
    df = df.dropna(subset=['Coin', 'Side', 'Closed PnL', 'Size USD', 'value'])

    # Convert Closed PnL to float
    df['Closed PnL'] = pd.to_numeric(df['Closed PnL'], errors='coerce')

    # Convert Size USD to float
    df['Size USD'] = pd.to_numeric(df['Size USD'], errors='coerce')

    # Create outcome: win if Closed PnL > 0
    df['Win'] = (df['Closed PnL'] > 0).astype(int)

    # Map sentiment classification to numeric score
    df['sentiment_score'] = df['classification'].apply(map_sentiment_to_score)

    # Extract month and year for time series analysis
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')

    # Additional feature: trade direction (Long/Short) based on Side? We have 'Direction' column.
    # We'll use 'Direction' for long/short classification.

    # Remove outliers in PnL (e.g., > 3 std) if needed
    # We'll keep for now, but we can cap later.

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")
    return df

if __name__ == "__main__":
    preprocess_data('../data/merged_dataset.csv', '../data/cleaned_dataset.csv')

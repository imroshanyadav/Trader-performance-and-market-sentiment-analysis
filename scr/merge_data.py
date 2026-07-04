import pandas as pd
from .utils import parse_date_from_timestamp, parse_timestamp_ist

def merge_datasets(fear_greed_path, historical_path, output_path):
    # Load datasets
    fear_greed = pd.read_csv(fear_greed_path)
    historical = pd.read_csv(historical_path)

    # Parse date from historical 'Timestamp IST'
    historical['date'] = historical['Timestamp IST'].apply(parse_date_from_timestamp)

    # Parse date from fear_greed (already in 'date' column)
    fear_greed['date'] = pd.to_datetime(fear_greed['date']).dt.date

    # Merge on date
    merged = historical.merge(fear_greed, on='date', how='left')

    # Save merged dataset
    merged.to_csv(output_path, index=False)
    print(f"Merged dataset saved to {output_path}")
    return merged

if __name__ == "__main__":
    merge_datasets('../data/fear_greed_index.csv',
                   '../data/historical_data.csv',
                   '../data/merged_dataset.csv')

import pandas as pd
from datetime import datetime

def parse_timestamp_ist(ts_str):
    """
    Convert timestamp string like '02-12-2024 22:50' to datetime object.
    """
    return pd.to_datetime(ts_str, format='%d-%m-%Y %H:%M')

def parse_date_from_timestamp(ts_str):
    """
    Extract date (YYYY-MM-DD) from timestamp string.
    """
    dt = parse_timestamp_ist(ts_str)
    return dt.date()

def map_sentiment_to_score(classification):
    """
    Map sentiment classification to numeric score for correlation.
    """
    mapping = {
        'Extreme Fear': 0,
        'Fear': 1,
        'Neutral': 2,
        'Greed': 3,
        'Extreme Greed': 4
    }
    return mapping.get(classification, 2)

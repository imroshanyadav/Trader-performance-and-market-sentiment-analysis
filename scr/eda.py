import pandas as pd
import numpy as np
from .utils import map_sentiment_to_score

def run_eda(input_path):
    df = pd.read_csv(input_path)

    # Overall metrics
    total_trades = len(df)
    total_pnl = df['Closed PnL'].sum()
    avg_pnl = df['Closed PnL'].mean()
    win_rate = df['Win'].mean()

    print(f"Total trades: {total_trades}")
    print(f"Total PnL: {total_pnl:.2f}")
    print(f"Average PnL per trade: {avg_pnl:.2f}")
    print(f"Win rate: {win_rate:.2%}")

    # Sentiment distribution
    sentiment_counts = df['classification'].value_counts()
    print("\nSentiment distribution:")
    print(sentiment_counts)

    # PnL by sentiment
    pnl_by_sentiment = df.groupby('classification')['Closed PnL'].agg(['mean', 'sum', 'count'])
    print("\nPnL by sentiment:")
    print(pnl_by_sentiment)

    # Win rate by sentiment
    win_rate_by_sentiment = df.groupby('classification')['Win'].mean()
    print("\nWin rate by sentiment:")
    print(win_rate_by_sentiment)

    # Long/Short ratio
    direction_counts = df['Direction'].value_counts()
    print("\nLong/Short distribution:")
    print(direction_counts)

    # Top assets by trade count
    top_assets = df['Coin'].value_counts().head(10)
    print("\nTop 10 assets by trade count:")
    print(top_assets)

    # Monthly performance
    monthly_pnl = df.groupby('month')['Closed PnL'].sum()
    print("\nMonthly total PnL:")
    print(monthly_pnl)

    # Correlation between sentiment score and PnL
    corr = df[['sentiment_score', 'Closed PnL']].corr()
    print(f"\nCorrelation between sentiment score and PnL: {corr.iloc[0,1]:.3f}")

    # Return summary for further use
    summary = {
        'total_trades': total_trades,
        'total_pnl': total_pnl,
        'avg_pnl': avg_pnl,
        'win_rate': win_rate,
        'sentiment_counts': sentiment_counts,
        'pnl_by_sentiment': pnl_by_sentiment,
        'win_rate_by_sentiment': win_rate_by_sentiment,
        'direction_counts': direction_counts,
        'top_assets': top_assets,
        'monthly_pnl': monthly_pnl,
        'correlation': corr.iloc[0,1]
    }
    return df, summary

if __name__ == "__main__":
    df, summary = run_eda('../data/cleaned_dataset.csv')
    # Save summary to a text file or excel later

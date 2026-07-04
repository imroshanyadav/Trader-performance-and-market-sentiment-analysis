import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def create_visualizations(df, output_dir='../charts/'):
    # Set style
    sns.set_style('whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)

    # 1. Sentiment distribution
    plt.figure()
    df['classification'].value_counts().plot(kind='bar')
    plt.title('Sentiment Classification Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{output_dir}sentiment_distribution.png')
    plt.close()

    # 2. Win rate
    plt.figure()
    df.groupby('classification')['Win'].mean().plot(kind='bar', color=['red', 'green', 'blue', 'orange', 'purple'])
    plt.title('Win Rate by Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Win Rate')
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(f'{output_dir}win_rate.png')
    plt.close()

    # 3. PnL by sentiment (boxplot)
    plt.figure()
    sns.boxplot(x='classification', y='Closed PnL', data=df)
    plt.title('PnL Distribution by Sentiment')
    plt.yscale('symlog')  # because of outliers
    plt.tight_layout()
    plt.savefig(f'{output_dir}boxplot_pnl.png')
    plt.close()

    # 4. Long/Short ratio
    plt.figure()
    df['Direction'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Long vs Short Trades')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(f'{output_dir}long_short_ratio.png')
    plt.close()

    # 5. Trade size distribution
    plt.figure()
    df['Size USD'].hist(bins=50, log=True)
    plt.title('Trade Size Distribution (USD)')
    plt.xlabel('Size (USD)')
    plt.ylabel('Frequency (log scale)')
    plt.tight_layout()
    plt.savefig(f'{output_dir}trade_size_distribution.png')
    plt.close()

    # 6. Correlation heatmap (numeric features)
    plt.figure()
    num_cols = ['value', 'sentiment_score', 'Closed PnL', 'Size USD', 'Fee']
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(f'{output_dir}correlation_heatmap.png')
    plt.close()

    # 7. Monthly performance
    monthly = df.groupby('month')['Closed PnL'].sum().reset_index()
    monthly['month'] = monthly['month'].astype(str)
    plt.figure()
    plt.bar(monthly['month'], monthly['Closed PnL'])
    plt.title('Monthly Total PnL')
    plt.xlabel('Month')
    plt.ylabel('Total PnL')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}monthly_performance.png')
    plt.close()

    # 8. Top assets
    top = df['Coin'].value_counts().head(10)
    plt.figure()
    top.plot(kind='bar')
    plt.title('Top 10 Assets by Trade Count')
    plt.xlabel('Asset')
    plt.ylabel('Number of Trades')
    plt.tight_layout()
    plt.savefig(f'{output_dir}top_assets.png')
    plt.close()

    # 9. PnL by sentiment (aggregated sum)
    pnl_sum = df.groupby('classification')['Closed PnL'].sum().sort_values()
    plt.figure()
    pnl_sum.plot(kind='bar')
    plt.title('Total PnL by Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Total PnL')
    plt.tight_layout()
    plt.savefig(f'{output_dir}pnl_by_sentiment.png')
    plt.close()

    print("All charts saved.")

if __name__ == "__main__":
    df = pd.read_csv('../data/cleaned_dataset.csv')
    create_visualizations(df)

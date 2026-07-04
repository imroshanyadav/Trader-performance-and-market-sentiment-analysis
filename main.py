from src.merge_data import merge_datasets
from src.data_preprocessing import preprocess_data
from src.eda import run_eda
from src.visualization import create_visualizations
import pandas as pd

def main():
    # Step 1: Merge data
    merged = merge_datasets('data/fear_greed_index.csv',
                            'data/historical_data.csv',
                            'data/merged_dataset.csv')

    # Step 2: Preprocess
    cleaned = preprocess_data('data/merged_dataset.csv',
                              'data/cleaned_dataset.csv')

    # Step 3: EDA
    df, summary = run_eda('data/cleaned_dataset.csv')

    # Step 4: Visualizations
    create_visualizations(df, output_dir='charts/')

    # Optionally save summary to report
    summary_df = pd.DataFrame([summary]).T
    summary_df.to_excel('report/summary_tables.xlsx', header=False)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()

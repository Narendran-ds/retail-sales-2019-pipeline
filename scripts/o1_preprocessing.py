import pandas as pd
import os

def preprocess_sales_data():
    """
    Loads the raw sales data from 'Sales_April_2019.csv', cleans it, 
    performs feature engineering, and saves the processed files.
    """
    print("--- Starting Data Pre-processing ---")
    
    # Define file paths
    raw_path = os.path.join('01_data', 'raw', 'Sales_April_2019.csv')
    processed_dir = os.path.join('01_data', 'processed')
    processed_sales_path = os.path.join(processed_dir, 'cleaned_sales.parquet')
    
    # Create directories if they don't exist
    os.makedirs(processed_dir, exist_ok=True)
    
    # Load Data
    try:
        df = pd.read_csv(raw_path)
    except FileNotFoundError:
        print(f"Error: The file '{raw_path}' was not found.")
        return

    # Initial Cleaning
    df.dropna(how='all', inplace=True)
    df = df[df['Order ID'] != 'Order ID']
    
    # Correct Data Types
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')

    # Feature Engineering
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    df['City'] = df['Purchase Address'].apply(lambda x: f"{x.split(',')[1].strip()} ({x.split(',')[2].strip().split(' ')[0]})")
    df['Hour'] = df['Order Date'].dt.hour
    
    # Save Processed Data
    df.to_parquet(processed_sales_path)
    print("--- Pre-processing Complete ---")

if __name__ == '__main__':
    preprocess_sales_data()

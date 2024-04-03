# python3 -m venv venv
# dataset: https://www.kaggle.com/datasets/bharatkumar0925/walmart-store-sales/data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Walmart_Store_sales.csv')

def create_weekly_store_sales_for_all_stores():
    number_of_stores = len(df['Store'].unique()) + 1
    for store_number in range(1, number_of_stores):
        store = df[df['Store'] == store_number]
        plt.plot(store['Date'], store['Weekly_Sales'])
    plt.title("Weekly Sales for All Stores")
    plt.xlabel("Date")
    plt.ylabel("Weekly Sales")
    plt.legend()
    plt.show()

def create_total_sales_by_store():
    sales_by_store = df.groupby('Store')['Weekly_Sales'].sum()
    sales_by_store.plot(kind='bar')
    plt.title("Total Weekly Sales by Store")
    plt.xlabel("Store")
    plt.ylabel("Total Weekly Sales")
    plt.show()


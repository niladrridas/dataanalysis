# data_explorer.py
import pandas as pd

def explore_data(file_path):
    # Load data into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Display basic information about the data
    print("Data Information:")
    print(data.info())

    # Display basic statistics of the numerical columns
    print("\nDescriptive Statistics:")
    print(data.describe())

    # Display the first few rows of the data
    print("\nFirst 5 Rows:")
    print(data.head())

if __name__ == "__main__":
    # Pass the file path as a command-line argument
    import sys
    if len(sys.argv) != 2:
        print("Usage: python data_explorer.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    explore_data(file_path)


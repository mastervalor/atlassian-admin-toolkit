import pandas as pd

file = 'Projects metrics 2'


def filter_months_before(target_month, target_year, csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert the 'Last ticket creation date' column to datetime format
    df['Last ticket creation date'] = pd.to_datetime(df['Last ticket creation date'])

    # Filter the DataFrame based on the condition (months before target_date)
    filtered_df = df[df['Last ticket creation date'] < pd.to_datetime(f"{target_month} {target_year}")]

    return filtered_df

# Replace 'your_file.csv' with the actual file path of your CSV file
csv_file = 'Projects metrics 2'
target_month = 'May'
target_year = 2023

result = filter_months_before(target_month, target_year, csv_file)
print(result)

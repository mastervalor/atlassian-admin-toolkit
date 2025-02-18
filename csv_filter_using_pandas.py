import pandas as pd
import os

# Assuming the CSV files are on your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Replace "file1.csv" and "file2.csv" with your actual file names
csv1_path = os.path.join(desktop_path, "Projects - new_file.csv")
csv2_path = os.path.join(desktop_path, "Archiving projects plan and times.csv")

# Read CSV files into pandas DataFrames
df1 = pd.read_csv(csv1_path)
df2 = pd.read_csv(csv2_path)

# Extract the "Name" columns from both DataFrames
names_csv1 = set(df1['Name'])
names_csv2 = set(df2['Name'])

# Find names that are in CSV 1 but not in CSV 2
names_only_in_csv1 = names_csv1 - names_csv2

# Create a new DataFrame with the result
result_df = pd.DataFrame({'Name': list(names_only_in_csv1)})

# Specify the output CSV file path
output_csv_path = os.path.join(desktop_path, "output_file.csv")

# Write the result to a new CSV file
result_df.to_csv(output_csv_path, index=False)

print(f"Result has been saved to {output_csv_path}")

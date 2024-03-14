# import csv
# import random

# # Set the range for random values
# min_value = 1.6
# max_value = 6

# # Number of rows
# num_rows = 500

# with open('random_values.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['Random Values'])  # Header

#     for _ in range(num_rows):
#         row_value = round(random.uniform(min_value, max_value), 3)
#         csvwriter.writerow([row_value])
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('random_values.csv')

# Sort the values in the DataFrame
df_sorted = df.sort_values(by='Random Values', ascending=False)

# Save the sorted values back to the CSV file
df_sorted.to_csv('sorted_random_values.csv', index=False)

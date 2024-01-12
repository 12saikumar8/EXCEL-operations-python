# import pandas as pd

# def read_and_display_csv(file_path, sheet_names):
#     try:
#         # Read the CSV file into a dictionary of DataFrames with sheet names as keys
#         dfs = pd.read_csv(file_path,sheet_names)

#         # Display data from each sheet
#         for sheet_name, df in dfs.items():
#             print(f"\nSheet Name: {sheet_name}")
#             print(df)

#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")

#     except pd.errors.EmptyDataError:
#         print(f"Error: The file '{file_path}' is empty.")

#     except pd.errors.ParserError as e:
#         print(f"Error: Parsing error - {e}")

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Example usage
# file_path = 'sample4.csv'  # Replace with the path to your CSV file
# sheet_names = ['sample4']  # Replace with the sheet names you want to read

# read_and_display_csv(file_path,sheet_names)


import pandas
df = pandas.read_csv('sample4.csv')
print(df)
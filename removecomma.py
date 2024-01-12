# import pandas as pd
# def remove_commas(file_path,sheet_name,column_name):

#     reading=pd.ExcelFile(file_path)

#     if sheet_name not in reading.sheet_names:
#         print(f"sheet '{sheet_name} not found in Excelfile")

#         return

#     df=pd.read_excel(file_path,sheet_name)

#     if column_name not in df.columns:
#         print(f"column'{column_name} not found in sheet'{sheet_name}")

#         return

#     df[column_name]=df[column_name]. str.replace(',','')

#     print(df)

# file_path="hello_world.xlsx"
# sheet_name="Suman"
# column_name="A1"

# remove_commas(file_path,sheet_name,column_name)

import pandas as pd

def remove_commas(file_path, sheet_name, column_name):
    # Read the Excel file into a pandas DataFrame
    xls = pd.ExcelFile(file_path)

    # Check if the sheet exists
    if sheet_name not in xls.sheet_names:
        print(f"Sheet '{sheet_name}' not found in the Excel file.")
        return

    # Read the data from the specified sheet
    df = pd.read_excel(file_path, sheet_name)

    # Check if the specified column exists
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the sheet '{sheet_name}'.")
        return

    # Remove commas from the specified column
    df[column_name] = df[column_name].str.replace(',', '')

    # Display the updated data
    print(f"\nSheet: {sheet_name}\n")
    print(df)

# Specify the path to your Excel file, sheet name, and column name
file_path = "reviews-sample.xlsx"  # Change this to the actual path of your Excel file
sheet_name = "amazon_reviews_us_Watches_v1_00"  # Change this to the desired sheet name
column_name = "product_category"  # Change this to the desired column name

# Call the function to remove commas from the specified column
remove_commas(file_path, sheet_name, column_name)


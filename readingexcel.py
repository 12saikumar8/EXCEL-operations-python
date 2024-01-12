# import openpyxl

# dataframe=openpyxl.load_workbook("reviews-sample.xlsx")

# dataframe1=dataframe.active

# for row in range(0,dataframe1.max_row):
#     for col in dataframe1.iter_cols(1,dataframe1.max_column):
#         print(col[row].value)


import pandas as pd

def read_excel_sheets(file_path):
    excel_data = pd.ExcelFile(file_path)
    sheet_names = excel_data.sheet_names

    print(f"Sheet Names: {sheet_names}")

    for sheet_name in sheet_names:
        sheet_data = pd.read_excel(file_path, sheet_name)

        print(f"\nSheet: {sheet_name}\n")
        print(sheet_data)

if __name__ == "__main__":
    excel_file_path = "./hello_world.xlsx"
    read_excel_sheets(excel_file_path)

import openpyxl

file_path = '../original_files/ST_14198_2628.txt'  # Replace with the path to your text file
excel_file_path = 'output.xlsx'  # Replace with the desired output Excel file path

try:
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Read the first line from the text file
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if "," in line and line.split(",")[1] == str(1) and line.split(",")[0] =="DayFile":
                first_line = line
                sheet['A1'] = first_line
            
            if line.startswith("1,"):
                sheet['B2'] = line

            

    # Save the workbook to the specified path
    workbook.save(excel_file_path)

    print(f"Excel file '{excel_file_path}' created and saved.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

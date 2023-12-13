import openpyxl

file_path = '../original_files/ST_14198_2628.txt'  # Replace with the path to your text file
excel_file_path = 'output.xlsx'  # Replace with the desired output Excel file path

try:
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    name_number_dict={}
    # Read the first line from the text file
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("DayFile"):
                name_number_dict[line.split(",")[0]]=line.split(',')[1]

    # Write each key to a new row in column A
    for index, key in enumerate(name_number_dict.keys(), start=1):
        sheet[f'A{index*2-1}'] = key

    # Loop through column A, get the corresponding value, and insert a new row with that value
    for row in range(1, sheet.max_row + 1):
        key = sheet[f'A{row}'].value
        if key in name_number_dict:
            line = [line for line in open(file_path,'r') if line.startswith(f"{key},")][0]
            if len(line)>1:print("hi")
            print(line)
            print(key)
            sheet[f'A{row}'].value=line
            line_number = line.split(",")[1]
            lines =[line for line in open(file_path,'r') if line.startswith(f"{line_number},")]
            for line in lines:
                # value = name_number_dict[key]
                sheet.insert_rows(row + 1)
                sheet[f'B{row + 1}'] = line.strip()

            

    # Save the workbook to the specified path
    workbook.save(excel_file_path)

    print(f"Excel file '{excel_file_path}' created and saved.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

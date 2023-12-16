from openpyxl import Workbook

def process_txt(txt_file_path,excel_file_path):
    workbook = Workbook()
    high_datasets = {}
    low_datasets={}
    low_dataset_lines=[]
    all_lines = []

    with open(txt_file_path, 'r') as txt_file:
        for line in txt_file:
            line = line.strip()
            all_lines.append(line)
            line_list = line.split(",")
            if "[]" in line:
                low_dataset_lines.append(line)
            if line_list[0].startswith("DayFile") and line_list[2] == "List" and line_list[0].count(".")==1 and "[]" not in line_list[0]:
                high_datasets[line_list[0]]=line_list[1]
    
    for high_dataset in high_datasets.keys():
        low_data_set_values = []
        for line in low_dataset_lines:
            if high_dataset in line and "[]" in line:
                low_data_set_values.append(line)
        low_datasets[high_dataset]=low_data_set_values

    for key,value in low_datasets.items():
        sheet = workbook.create_sheet(title=key)
        for line in all_lines:
            if line.startswith(f"{key},"):
                sheet['A1'] = line

                if line.split(","):pass
    

    # Remove the default sheet created by openpyxl (Sheet)
    default_sheet = workbook['Sheet']
    workbook.remove(default_sheet)

    # Save the Excel workbook
    workbook.save(excel_file_path)



if __name__ == "__main__":
    txt_file_path = "../original_files/modified.txt"
    excel_file_path = "new_output.xlsx"

    process_txt(txt_file_path, excel_file_path)

    print(f"Excel file created with sheets named according to conditions. Saved to {excel_file_path}.")

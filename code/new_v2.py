from openpyxl import Workbook

def process_txt(txt_file_path, excel_file_path):
    workbook = Workbook()
    names_of_the_datasets = []

    with open(txt_file_path, 'r') as txt_file:
        for line in txt_file:
            line = line.strip()
            comma_separated_line_list = line.split(',')
            first_entry = comma_separated_line_list[0]
            if line.startswith("DayFile") and "[]" not in first_entry:
                sheet_name = first_entry
                names_of_the_datasets.append(line)
                sheet = workbook.create_sheet(title=sheet_name)
                sheet['A1'] = line

    for dataset in names_of_the_datasets:
        comma_separated_dataset_list = dataset.split(",")
        dataset_sheet_name = comma_separated_dataset_list[0]
        dataset_sheet = workbook[dataset_sheet_name]
        dataset_line_number = comma_separated_dataset_list[1]
        with open(txt_file_path,'r') as txt_file:
            for line in txt_file:
                line = line.strip()
                if line.startswith(f"{dataset_line_number},"):
                    dataset_sheet['B3'] = line

    
    with open(txt_file_path, 'r') as txt_file:
        
        for line in txt_file:
            line = line.strip()
            comma_separated_line_list = line.split(',')
            first_entry = comma_separated_line_list[0]
            for dataset in names_of_the_datasets:
                starting_row=5
                comma_separated_dataset_list = dataset.split(",")
                dataset_sheet_name = comma_separated_dataset_list[0]
                dataset_sheet = workbook[dataset_sheet_name]
                if first_entry == f'{dataset_sheet_name}[]':
                    dataset_sheet[f'A{starting_row}'] = line
                    starting_row+=1


    # Remove the default sheet created by openpyxl (Sheet)
    default_sheet = workbook['Sheet']
    workbook.remove(default_sheet)

    # Save the Excel workbook
    workbook.save(excel_file_path)



if __name__ == "__main__":
    txt_file_path = "../original_files/ST_14198_2628.txt"
    excel_file_path = "new_output.xlsx"

    process_txt(txt_file_path, excel_file_path)

    print(f"Excel file created with sheets named according to conditions. Saved to {excel_file_path}.")

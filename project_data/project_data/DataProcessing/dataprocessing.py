import pandas as pd

def process_and_clean_data(file_path, file_path2, file_path3):
    """
    Loads, processes, and cleans multiple DataFrames based on the provided logic.

    Parameters:
        file_path (str): Path to the first Excel file.
        file_path2 (str): Path to the second Excel file.
        file_path3 (str): Path to the third Excel file.

    Returns:
        dict: A dictionary containing cleaned DataFrames.
    """
    def load_table_to_dataframe(file_path, sheet_name, header_row, num_rows):
        try:
            return pd.read_excel(file_path, sheet_name=sheet_name, header=header_row, nrows=num_rows)
        except Exception as e:
            print(f"Error while loading the table from {sheet_name}: {e}")
            return None

    # Load all DataFrames
    education_52_1929 = load_table_to_dataframe(file_path, "Table 5.2", header_row=1, num_rows=9)
    education_53_1929 = load_table_to_dataframe(file_path, "Table 5.3", header_row=1, num_rows=791)
    education_54_1929 = load_table_to_dataframe(file_path, "Table 5.4", header_row=1, num_rows=790)
    education_51_2333 = load_table_to_dataframe(file_path2, "Table 5.1", header_row=1, num_rows=8)
    education_52_2333 = load_table_to_dataframe(file_path2, "Table 5.2", header_row=1, num_rows=9)
    education_53_2333 = load_table_to_dataframe(file_path2, "Table 5.3", header_row=1, num_rows=833)
    education_54_2333 = load_table_to_dataframe(file_path2, "Table 5.4", header_row=1, num_rows=832)
    occupation_11_1929 = load_table_to_dataframe(file_path3, "Table 1.1", header_row=1, num_rows=23)

    # Process and clean data
    occupation_11_1929['lables'] = occupation_11_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    title_labels_dict = occupation_11_1929.set_index('lables')['2019 National Employment Matrix title'].to_dict()

    education_53_1929['lables'] = education_53_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    education_53_1929['Title Labels'] = education_53_1929['lables'].map(title_labels_dict)

    education_53_2333['lables'] = education_54_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    education_53_2333['Title Labels'] = education_53_2333['lables'].map(title_labels_dict)

    education_54_1929['lables'] = education_54_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    education_54_1929['Title Labels'] = education_54_1929['lables'].map(title_labels_dict)

    education_54_2333['lables'] = education_54_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    education_54_2333['Title Labels'] = education_54_2333['lables'].map(title_labels_dict)

    education_53_1929['2019 National Employment Matrix title'] = education_53_1929[
        '2019 National Employment Matrix title'
    ].str.replace(r'\(.*?\)', '', regex=True).str.strip()

    education_53_2333['2023 National Employment Matrix title'] = education_53_2333[
        '2023 National Employment Matrix title'
    ].str.replace(r'\[.*?\]', '', regex=True).str.strip()

    # Return all DataFrames in a dictionary
    return {
        "education_52_1929": education_52_1929,
        "education_53_1929": education_53_1929,
        "education_54_1929": education_54_1929,
        "education_51_2333": education_51_2333,
        "education_52_2333": education_52_2333,
        "education_53_2333": education_53_2333,
        "education_54_2333": education_54_2333,
        "occupation_11_1929": occupation_11_1929
    }

# Example usage

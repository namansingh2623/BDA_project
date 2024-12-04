import pandas as pd

def load_table_to_dataframe(file_path, sheet_name, header_row, num_rows):
    """
    Reads an Excel table into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to read.
        header_row (int): Row number to use as the header (0-indexed).
        num_rows (int): Number of rows to read starting from the header row.

    Returns:
        pandas.DataFrame: DataFrame containing the extracted data.
    """
    try:
        # Read the Excel file with specified parameters
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row, nrows=num_rows)
        return df
    except Exception as e:
        print(f"Error while loading the table: {e}")
        return None
    


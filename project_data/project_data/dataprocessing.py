import pandas as pd

def process_and_clean_data():
    """
    Loads, processes, and cleans multiple DataFrames based on the provided logic.

    Parameters:
        file_path (str): Path to the first Excel file.
        file_path2 (str): Path to the second Excel file.
        file_path3 (str): Path to the third Excel file.

    Returns:
        dict: A dictionary containing cleaned DataFrames.
    """


    #Naman Paths
    # "BDA_project/project_data/project_data/Datasets/2019-29/education.xlsx"
    # "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/education.xlsx"
    # file_path = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/education.xlsx"
    # file_path2 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2023-33/education.xlsx"
    # file_path3 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/occupation.xlsx"
    # file_path4 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2023-33/skills.xlsx"
    # file_path5 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2023-33/occupation.xlsx"

    # Malavs Paths
    # file_path = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/education.xlsx"
    # file_path2 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2023-33/education.xlsx"
    # file_path3 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/occupation.xlsx"

    # LISA PATHS: 
    file_path = "Datasets/2019-29/education.xlsx"
    file_path2 = "Datasets/2023-33/education.xlsx"
    file_path3 = "Datasets/2019-29/occupation.xlsx"
    file_path4 = "Datasets/2023-33/skills.xlsx"
    file_path5 = "Datasets/2023-33/occupation.xlsx"
    

    # DAN PATHS
    # file_path = "project_data/project_data/Datasets/2019-29/education.xlsx"
    # file_path2 = "project_data/project_data/Datasets/2023-33/education.xlsx"
    # file_path3 = "project_data/project_data/Datasets/2019-29/occupation.xlsx"
    # file_path4 = "project_data/project_data/Datasets/2023-33/skills.xlsx"



    #DYLAN PATH:
    # file_path = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/education.xlsx"
    # file_path2 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2023-33/education.xlsx"
    # file_path3 = "/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/2019-29/occupation.xlsx"
    # print("FIle Paths==>",file_path, file_path2, file_path3, file_path4)
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
    occupation_12_1929 = load_table_to_dataframe(file_path3, "Table 1.2", header_row=1, num_rows=1048)
    occupation_13_1929 = load_table_to_dataframe(file_path3, "Table 1.3", header_row=1, num_rows=31)
    occupation_14_1929 = load_table_to_dataframe(file_path3, "Table 1.4", header_row=1, num_rows=31)
    occupation_15_1929 = load_table_to_dataframe(file_path3, "Table 1.5", header_row=1, num_rows=31)
    occupation_16_1929 = load_table_to_dataframe(file_path3, "Table 1.6", header_row=1, num_rows=31)
    
    occupation_13_2333 = load_table_to_dataframe(file_path=file_path5, sheet_name='Table 1.3', header_row=1, num_rows=31)
    occupation_14_2333 = load_table_to_dataframe(file_path=file_path5, sheet_name='Table 1.4', header_row=1, num_rows=31)
    occupation_15_2333 = load_table_to_dataframe(file_path=file_path5, sheet_name='Table 1.5', header_row=1, num_rows=31)
    occupation_16_2333 = load_table_to_dataframe(file_path=file_path5, sheet_name='Table 1.6', header_row=1, num_rows=31)
    
    # skills_51_2333 = load_table_to_dataframe(file_path4, "Table 5.1", header_row=1, num_rows=10)
    # skills_52_2333 = load_table_to_dataframe(file_path4, "Table 5.2", header_row=1, num_rows=10)

    # data_1929 = pd.read_excel("/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/OurProcessedDatasets/top_5_1929.xlsx")
    # data_2333 = pd.read_excel("/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/OurProcessedDatasets/top_5_2333.xlsx")
    # Check if DataFrames are loaded successfully
    dataframes = [
    education_52_1929, education_53_1929, education_54_1929,
    education_51_2333, education_52_2333, education_53_2333, education_54_2333,
    occupation_11_1929, occupation_12_1929, occupation_13_1929, occupation_14_1929
    ]

# Check if any DataFrame failed to load
    if any(df is None for df in dataframes):
        print("Failed to load one or more DataFrames. Please check the file paths and sheet names.")
        return

    # Example: Extracting labels and creating a dictionary for title labels    #skills dfs
    skills_61_2333 = load_table_to_dataframe(file_path4, "Table 6.1", header_row=1, num_rows=23)
    skills_62_2333 = load_table_to_dataframe(file_path4, "Table 6.2", header_row=1, num_rows=833)
    skills_63_2333 = load_table_to_dataframe(file_path4, "Table 6.3", header_row=1, num_rows=31)
    skills_64_2333 = load_table_to_dataframe(file_path4, "Table 6.4", header_row=1, num_rows=9)
    skills_65_2333 = load_table_to_dataframe(file_path4, "Table 6.5", header_row=1, num_rows=833)

    # Process and clean data
    occupation_11_1929['lables'] = occupation_11_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    title_labels_dict = occupation_11_1929.set_index('lables')['2019 National Employment Matrix title'].to_dict()
    occupation_12_1929['lables'] = occupation_12_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    occupation_13_1929['lables'] = occupation_13_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    occupation_14_1929['lables'] = occupation_14_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    occupation_13_2333['lables'] = occupation_13_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    occupation_14_2333['lables'] = occupation_14_2333['2023 National Employment Matrix code'].str.split('-').str[0]


    occupation_15_1929['lables'] = occupation_15_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    occupation_16_1929['lables'] = occupation_15_1929['2019 National Employment Matrix code'].str.split('-').str[0]
    occupation_15_2333['lables'] = occupation_15_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    occupation_16_2333['lables'] = occupation_16_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    


    
    occupation_11_1929.drop(index=0,inplace=True)
    occupation_12_1929.drop(index=0,inplace=True)
    occupation_13_1929.drop(index=0,inplace=True)
    occupation_14_1929.drop(index=0,inplace=True)
    occupation_13_14_1929 = pd.concat(
    [occupation_13_1929,  # First DataFrame
    occupation_14_1929], # Second DataFrame
    axis=0
    )
    occupation_13_14_1929.drop_duplicates(subset="2019 National Employment Matrix code", keep='first', inplace=True)

    occupation_13_2333.drop(index=0,inplace=True)
    occupation_14_2333.drop(index=0,inplace=True)
    occupation_13_14_2333 = pd.concat(
    [occupation_13_2333,  # First DataFrame
    occupation_14_2333], # Second DataFrame
    axis=0
    )
    occupation_13_14_2333.drop_duplicates(subset="2023 National Employment Matrix code", keep='first', inplace=True)


    occupation_15_1929.drop(index=0, inplace=True)
    occupation_16_1929.drop(index=0, inplace=True)
    occupation_15_2333.drop(index=0, inplace=True)
    occupation_16_2333.drop(index=0, inplace=True)  

    occupation_15_16_1929 = pd.concat(
    [occupation_15_1929,  # First DataFrame
    occupation_16_1929], # Second DataFrame
    axis=0
    )
    occupation_15_16_1929.drop_duplicates(subset="2019 National Employment Matrix code", keep='first', inplace=True)


    occupation_15_16_2333 = pd.concat(
    [occupation_15_2333,  # First DataFrame
    occupation_16_2333], # Second DataFrame
    axis=0
    )
    occupation_15_16_2333.drop_duplicates(subset="2023 National Employment Matrix code", keep='first', inplace=True)


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
    
    # process skills
    skills_61_2333['2023 National Employment Matrix title'] = skills_61_2333[
        '2023 National Employment Matrix title'
    ].str.replace(r'\[.*?\]', '', regex=True).str.strip()
    skills_62_2333['2023 National Employment Matrix title'] = skills_62_2333[
        '2023 National Employment Matrix title'
    ].str.replace(r'\[.*?\]', '', regex=True).str.strip()
    skills_63_2333['2023 National Employment Matrix title'] = skills_63_2333[
        '2023 National Employment Matrix title'
    ].str.replace(r'\[.*?\]', '', regex=True).str.strip()
    skills_65_2333['2023 National Employment Matrix title'] = skills_65_2333[
        '2023 National Employment Matrix title'
    ].str.replace(r'\[.*?\]', '', regex=True).str.strip()

    # #"BDA_project/project_data/project_data/"
    # national_M2019_dl = pd.read_excel("/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/oesm19nat/national_M2019_dl.xlsx")
    # national_M2023_dl = pd.read_excel("/Users/naman/Desktop/SEM-3 PDFS/BDA_PROJECT/BDA_project/project_data/project_data/Datasets/oesm23nat/national_M2023_dl.xlsx")
    
    # #"BDA_project/project_data/project_data/"
    national_M2019_dl = pd.read_excel("Datasets/oesm19nat/national_M2019_dl.xlsx")
    national_M2023_dl = pd.read_excel("Datasets/oesm23nat/national_M2023_dl.xlsx")

    skills_61_2333['lables'] = skills_61_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    title_labels_dict_skills = skills_61_2333.set_index('lables')['2023 National Employment Matrix title'].to_dict()
    skills_61_2333['Title Labels'] = skills_61_2333['lables'].map(title_labels_dict_skills)
    skills_62_2333['lables'] = skills_62_2333['2023 National Employment Matrix code'].str.split('-').str[0]
    skills_62_2333['Title Labels'] = skills_62_2333['lables'].map(title_labels_dict_skills)

    # Return all DataFrames in a dictionary
    return {
        "education_52_1929": education_52_1929,
        "education_53_1929": education_53_1929,
        "education_54_1929": education_54_1929,
        "education_51_2333": education_51_2333,
        "education_52_2333": education_52_2333,
        "education_53_2333": education_53_2333,
        "education_54_2333": education_54_2333,
        "occupation_11_1929": occupation_11_1929,
        "occupation_12_1929": occupation_12_1929,
        "occupation_13_1929": occupation_13_1929,
        "occupation_14_1929":occupation_14_1929,
        "occupation_13_14_1929":occupation_13_14_1929,
        "occupation_13_2333": occupation_13_2333,
        "occupation_14_2333": occupation_14_2333,
        "occupation_13_14_2333":occupation_13_14_2333,
        "occupation_15_1929": occupation_15_1929,
        "occupation_16_1929": occupation_16_1929,
        "occupation_15_16_1929":occupation_15_16_1929,
        "occupation_15_2333": occupation_15_2333,
        "occupation_16_2333": occupation_16_2333,
        "occupation_15_16_2333":occupation_15_16_2333, 
        "title_labels_dict": title_labels_dict,
        "oesm_national_M2019_dl_19":national_M2019_dl,
        "oesm_national_M2023_dl_23":national_M2023_dl,
        "skills_61_2333":skills_61_2333,
        "skills_62_2333":skills_62_2333,
        "skills_63_2333":skills_63_2333,
        "skills_64_2333":skills_64_2333,
        "skills_65_2333":skills_65_2333,

    }

# **BDA Project**  
## **Documentation**  

### **Nomenclature Guidelines**  

#### **General Rules**  
1. **Case Sensitivity**: All names should be in **lowercase**.  
2. **Spacing**: Use an **underscore (`_`)** to replace spaces in all rows and names.  

#### **DataFrame Nomenclature**  
The format for naming DataFrames follows this structure:  

- **sheetname**: Descriptive name of the data.  
- **tablenumber**: A unique numeric identifier for the table.  
- **yearstart**: The starting year of the data.  
- **yearend**: The ending year of the data.  

#### **Examples**  
| **DataFrame Name**       | **Description**                                      |  
|---------------------------|------------------------------------------------------|  
| `skills_63_2333`          | Data for "skills," table 63, prediction year 2333.   |  
| `skills_63_1919`          | Data for "skills," table 63, for the same year 1919. |  

Use this consistent nomenclature for easy identification and management of datasets across the project.

---

### **Creating a DataFrame**  
- We are using **Pandas** as the primary library for data manipulation and analysis.  
- To create a DataFrame, use the following function:  

#### **Function Parameters**  
- **file_path (str)**: Path to the Excel file.  
- **sheet_name (str)**: Name of the sheet to read.  
- **header_row (int)**: Row number to use as the header (0-indexed).  
- **num_rows (int)**: Number of rows to read starting from the header row.  

#### **Returns**  
- **pandas.DataFrame**: DataFrame containing the extracted data.  

---

#### **Example**  
```python
# Example of loading a DataFrame
education_52_1929 = load_table_to_dataframe(file_path, "Table 5.2", header_row=1, num_rows=9)
```


# MORE QUERIES: 
1: Lisa: Work on Wage. 
    - Give understanding of Meadian wage for selcted Profession

2: Naman: Work on Skills. Improve on Dan code with Dropdown

3: Danial: Occupation 1.12 2023. He will work on providing analysis and Reasoning of 
why there is a Incline or Decline in Professions and Employment in perticular Sector.
Maybe add Dropdown and filter data based on Selection

4: 

import pandas as pd
import os

# --- Configuration ---
FILE_SOURCE = 'iris.csv' 
FILE_OUTPUT = 'iris_vis.xlsx' # Changed output name to match README

#1. Loading and Type Conversion (Real/Float)
try:
    # Read the CSV file, specifying the dot ('.') as the decimal separator 
    # to ensure that the values are correctly read as floats (real numbers).
    df = pd.read_csv(FILE_SOURCE, decimal='.')
except FileNotFoundError:
    print(f"Error: The file '{FILE_SOURCE}' was not found.")
    exit()

# Identify the numerical measurement columns (the first 4)
numerical_cols = df.columns[0:4] 

# Force conversion to the numerical type (float)
for col in numerical_cols:
    # 'errors="coerce"' replaces non-numeric values with NaN
    df[col] = pd.to_numeric(df[col], errors='coerce')


#2.Data Cleaning

# Remove duplicates
if df.duplicated().sum() > 0:
    df.drop_duplicates(keep='first', inplace=True)

# Remove rows containing NaN (introduced by the forced conversion)
# This ensures only fully clean rows remain for the final file.
if df[numerical_cols].isnull().sum().sum() > 0:
    df.dropna(subset=numerical_cols, inplace=True)


#3.Exporting the Cleaned DataFrame to Excel
try:
    # Write the cleaned DataFrame to an Excel file (.xlsx)
    # index=False excludes the Pandas index column from the final Excel sheet.
    df.to_excel(FILE_OUTPUT, index=False)
    
    print(f"Success: The cleaned data has been exported to the file: {FILE_OUTPUT}")
    print(f"Final dataset size: {df.shape[0]} rows.")
    
except Exception as e:
    print(f"Error during export to Excel: {e}")
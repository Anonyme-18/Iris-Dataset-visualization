Iris Dataset Analysis & Visualization Dashboard


1. Project Overview
This repository contains Python scripts designed to perform Data Cleaning, Exploratory Data Analysis (EDA), and Statistical Visualization on the classic Iris species dataset.
The main deliverable is a high-quality statistical dashboard, generated via Python, which summarizes key metrics (Mean, Min, Max) of the four flower measurements across the three Iris species.
2. Prerequisites
You must have Python 3.x installed on your system.
Required Libraries
All necessary libraries can be installed using pip.
Bash
pip install pandas numpy matplotlib seaborn openpyxl


Library
	Purpose
	pandas
	Data manipulation and cleaning (clean.py).
	numpy
	Numerical operations (underlying dependency).
	matplotlib
	Core plotting library.
	seaborn
	Statistical visualization and aesthetic rendering.
	openpyxl
	Required by pandas to write .xlsx files.
	

3. File Structure
Ensure the following files are downloaded and placed in the same directory before starting the execution:
├── iris.csv            # The raw data file (required input).
├── clean.py            # Script for data cleaning and Excel output.
├── iris_vis.py         # Script for specialized visualization functions (if applicable).
├── script.py           # Main script for generating the final statistical dashboard.
└── README.md           # This guide.




4. Execution Steps
The recommended workflow proceeds in three logical steps: Cleaning, Intermediate Excel Validation, and Final Python Visualization.
Step 1: Data Cleaning
This step cleans the raw data (iris.csv) by handling incorrect data types, missing values, and duplicate entries. It creates a validated file ready for visualization.
1. Ensure iris.csv and clean.py are in the same directory.


2. Execute the cleaning script from your terminal:
Bash
python clean.py


   3. Output: Upon successful completion, a new file named iris_clean.xlsx will be generated in your directory. This file contains the cleaned data in a format suitable for direct use in Microsoft Excel.
Step2: Excel Visualization (Optional)
You can now perform an intermediate visualization check using external tools:
   * Excel: Open iris_clean.xlsx and use Pivot Tables (TCD) to quickly calculate and visualize aggregate statistics (Mean, Max, Min) by species.
   * Python Scripts: The iris_vis.py file (assuming it contains specific visual functions) can be used to run specialized visualizations separate from the main dashboard.
Step 3: Python Dashboard Execution
This is the final step to generate the comprehensive statistical dashboard, which is more robust and visually appealing than basic Excel charts.
Execute the main dashboard script from your terminal:
Bash
python script.py
   1.    2. Output:
   * Console Output: Statistical tables (mean, max, min by species) will be printed to the terminal.
   * Screen Display: A figure containing the 4-panel statistical dashboard (bar plots and box plots) will be displayed on your screen. This figure represents the final project visualization.

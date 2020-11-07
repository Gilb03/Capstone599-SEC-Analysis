import os 
import csv
import xlrd 
import openpyxl
import glob
import sqlite3
import pandas as pd
from os import listdir, path


###################################################
# READ IN ALL OF THE XLSX BOOKS INTO ONE DATAFRAME 
####################################################


#TURN XLSX INTO ONE DATAFRAME
os.chdir('dataset/')
extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# FORMAT AND FIX THE DATA FRAME SO WE CAN HAVE MULTIPLE SHEETS IN ONE WORKBOOK
combined_xlsx = pd.concat([pd.read_excel(f) for f in all_filenames ])
combined_xlsx.to_sql('super_financial_statements.sql', index=False, encoding='utf-8-sig')

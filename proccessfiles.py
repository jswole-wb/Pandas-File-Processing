import pandas as pd
from pandas import DataFrame
import os, fnmatch
from openpyxl import load_workbook
#import shutil #if you need to move files
from datetime import date
#import uuid # this is for generating a  guid


##This file will see If a cell and next one are empty, take previous value after loading everything in a pandas data frame.





df_excel = pd.ExcelFile('FileNAME.xlsx')
df = df_excel.parse('Sheet Name')
df = df.fillna(method='ffill')
#names = df['Property Character Location Other'].unique()
#for name in names:
 #   df.loc[df['Property Character Location Other'] == name, 'UUID'] = uuid.uuid4()

print(df)
for col in list(df):  # All columns
    pprow = 0
    prow = 1
    for row in df[1:].iterrows():  # All rows, except first
        if pd.isnull(df.loc[prow, 'Column Name']):  # If this cell is empty all in the same row too.
            continue
        elif pd.isnull(df.loc[prow, col]) and pd.isnull(df.loc[row[0], col]):  # If a cell and next one are empty, take previous value. 
            df.loc[prow, col] = df.loc[pprow, col]
        pprow = prow
        prow = row[0]
    
writer = pd.ExcelWriter('cot_data.xlsx', engine='openpyxl')
    # try to open an existing workbook
writer.book = load_workbook('cot_data.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'cot_data.xlsx',sheet_name='Sheet1')
# write out the new sheet
df.to_excel(writer,index=False,header=True,startrow=len(reader)+1, sheet_name='Sheet1')
    #df.to_csv('filename.csv', index=False) # Save as .CSV instead of xlas 
print("File Done.")
writer.close()        
    
import pandas as pd
from pandas import DataFrame
import os, fnmatch
from openpyxl import load_workbook
import shutil
from datetime import date
today = date.today()
d4 = today.strftime("%Y-%m-%d") #format date to string which will be used as the folder name


sourcefiles = './'   # Path to where the source CSV files are located
outputfiles = './old' # Path to where the output CSV files are located and should be stored 
cwd = os.getcwd()

#########################################################################################
#
#########################################################################################
def load_cot(directory1): #chain of title
    #listOfFiles = os.listdir(directory1)
    listOfFiles = os.listdir('./')
    for entry in listOfFiles:
        if entry.endswith('.csv'):
            #fullname = os.path.join(directory1, entry)
            process_cot(entry)


##################################################################
#
##################################################################


def process_cot(entry):
#This function will process the chain of title file 
    data = pd.read_csv(entry) 
    
    df = DataFrame(data)
    df.index = pd.Series(df.index).fillna(method='ffill')
    #df = DataFrame(data, columns= ['Property Character Location Other', 'Project(s) Requested','First appearance','Talent']) # for specific columns
    #df['importdate']= d4
    print(entry) #file name
    print(df) #dataframe
    
    
    
    
    
    writer = pd.ExcelWriter('cot_data.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('cot_data.xlsx')
# copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
    reader = pd.read_excel(r'cot_data.xlsx',sheet_name='Sheet1')
# write out the new sheet
    #df.to_excel(writer,index=False,header=False,startrow=len(reader)+1, sheet_name='Sheet1')
    #df.to_csv('nintendo.csv', index=False)
    #shutil.move(entry, "old/")
    print("File Done.")
    writer.close()



##################################################
#Call the functions
##################################################
folder_name = os.path.join(cwd, d4)
load_cot(folder_name)




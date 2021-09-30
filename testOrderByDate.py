import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByICA4Dfs0"
        
os.chdir(dirHome)        

dat = pd.read_csv("Whiteface Farms.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)

# change dat 'date' to date format
dat['date'] = pd.to_datetime(dat['date'])

dat = dat.sort_values(by = ['date'])

# print(dat['date'][22])

print(dat)
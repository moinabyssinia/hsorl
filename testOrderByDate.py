import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\staticWellFile_WS"
        
os.chdir(dirHome)        

dat = pd.read_csv("staticWellFile_byWS.txt")
print(dat)

dat = dat[~(dat['watershed'].isnull())]

print(dat)
print(dat.columns)

dat.to_csv('staticWellFileByWS.csv')
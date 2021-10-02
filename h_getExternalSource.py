"""  
Created on Wed Sep 30 17:46:00 2021

prepare the withdrawal csvs to get total monthly withdrwal

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByICA4Dfs0"

dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsExternalSource"

os.chdir(dirHome)

for wellDat in os.listdir():
    
    os.chdir(dirHome)

    print(wellDat)
    
    dat = pd.read_csv(wellDat)
    
    dat['monthlyWithdrawal'] = dat.iloc[:,2:].sum(axis = 1)
    
    os.chdir(dirOut)
    
    dat[['date', 'monthlyWithdrawal']].to_csv(wellDat)




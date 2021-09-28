"""  
Created on tue Sep 28 17:04:00 2021

this script gets the wells based on the watersheds
to later prepare them for dfs0 files 

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\07-staticFile"
dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\"\
                "07-staticFile\\wellsByICA"


os.chdir(dirHome)

dat = pd.read_csv("allWells_watershed.csv")
dat = dat[~dat['watershed'].isnull()]

dat.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

for ws in dat['watershed'].unique():
    # os.chdir(dirHome)
    print(ws)
    currentWells = dat[dat['watershed'] == ws]
    
    os.chdir(dirOut)
    currentWells.to_csv(ws+".csv")
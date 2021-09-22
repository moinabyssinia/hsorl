"""  
Created on Wed Sep 08 09:51:00 2021

this script orders the well data based on year

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\irrigation-module\\01-data"

os.chdir(dirHome)

dat = pd.read_csv("agWells.csv")

dat.sort_values(by='year', inplace = True)

dat.drop(['Unnamed: 0'], axis = 1, inplace = True)

print(dat)

dat.to_csv("agWellsSortedByYear.csv")
"""  
Created on Thu Sep 23 16:13:00 2021

fix dfs0 dimension problem

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
from datetime import datetime
from mikeio import Dfs0, Dataset
from mikeio.eum import ItemInfo, EUMType, EUMUnit
import pandas as pd 
from mikeio import Dfs0


dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\07-staticFile"

os.chdir(dirHome)

dat = pd.read_csv("staticWellFileCleaned.csv")

dat.drop(['Unnamed: 0','dfs0File'], axis = 1, inplace = True)

dat.columns = ['wellID', 'x', 'y', 'level', 'wellField', 'top', 'bottom', 'depth',
       'fraction', 'dfs0Item', 'dfs0File']

print(dat)

dat['dfs0File'] = dat['dfs0File'] + ".dfs0"

print(dat)

dat.to_csv('staticWellFileCleaned_ws_ICA.csv')
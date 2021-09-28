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

dat = pd.read_csv("allWells_watershed.csv")

print(dat['watershed'].unique())


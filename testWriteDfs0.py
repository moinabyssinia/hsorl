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



nt = 10
d1 = np.zeros(nt)
d2 = np.ones(nt)

data = [d1, d2]

print(data)


# ds = Dataset(data=[d1,d2],
#              time=pd.date_range(datetime(2000,1,1), periods=nt, freq='H'), # hourly data
#              items=[ItemInfo("Zeros", EUMType.Water_Level, EUMUnit.meter), 
#                     ItemInfo("Ones", EUMType.Discharge, EUMUnit.meter_pow_3_per_sec)])
# print(ds)


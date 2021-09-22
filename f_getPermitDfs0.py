"""  
Created on Wed Sep 22 18:24:00 2021

prepare dfs0 permit files - using the mikeio tool

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 
from mikeio import Dfs0

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\"\
                                "ECFTX\\extractedWellData\\04-byCounty"
                                
os.chdir(dirHome)

##########################################################
# provide county name
# brevard | indianRiver | martin | okeechobee | stLucie | 
county = "stLucie"
##########################################################

# preprocess file
dat = pd.read_csv(county + ".csv")
dat['mon'] = dat['mon'].str.replace('AVE','JAN')
dat['date'] = dat['mon'].map(str) + "-" + dat['year'].map(int).map(str)
print(dat)

# filter unique permits/wells
print(len(dat['rowColPermit'].unique()))

uniquePermits = dat['rowColPermit'].unique()

first = True
for permit in uniquePermits:
    print(permit) 
    currentPermit = dat[dat['rowColPermit'] == permit][['date','withdrawal']]
    currentPermit.reset_index(inplace = True)
    currentPermit.drop("index", axis = 1, inplace = True)
    currentPermit.columns = ['date', permit]
    
    print(currentPermit)
    
    if first:
        withdrawalDat = currentPermit
        first = False
    else:
        withdrawalDat = pd.merge(withdrawalDat, currentPermit, on="date", how="outer")

print(withdrawalDat)

# save as csv
withdrawalDat.to_csv(county + "4Dfs0.csv")

# get readable time format
getDate = lambda x: pd.to_datetime(x) 
withdrawalDat['date'] = pd.DataFrame(list(map(getDate, withdrawalDat['date'])))

print(withdrawalDat)

withdrawalDat.set_index('date', inplace = True)

# writing dataframe to dfs0
withdrawalDat.to_dfs0(county + ".dfs0")

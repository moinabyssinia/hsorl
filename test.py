"""  
Created on Fri Sep 17 15:28:00 2021

testing script
testing mikeio for dfs0 manipulation

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 
from mikeio import Dfs0
import mikeio

def test1():
        dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\06-allWellsFinal"

        os.chdir(dirHome)

        dat = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_allWells.csv")

        print(dat[dat['rowColPermit'] == "487_592_SF_56-00033-W_15970"])


dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\"\
                                "ECFTX\\extractedWellData\\04-byCounty"


os.chdir(dirHome)

# preprocess file
dat = pd.read_csv("indianRiver.csv")
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

withdrawalDat.to_csv("test_indianRiver.csv")

# get readable time format
getDate = lambda x: pd.to_datetime(x) 
dat['date'] = pd.DataFrame(list(map(getDate, dat['date'])))

print(dat)

# writing dataframe to dfs0
dat.to_dfs0("indianRiver.dfs0")

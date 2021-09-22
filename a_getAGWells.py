"""  
Created on Wed Sep 08 08:07:00 2021

this script filters the AG wells from the wells file prepared

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\irrigation-module\\01-data"

os.chdir(dirHome)

# file containing AG well tags
ica = pd.read_csv("WMD_ICA_info.csv")

# all wells files
allWells = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_allWells.csv")
allWells.drop('Unnamed: 0', axis = 1, inplace = True)
print(allWells.columns)

unqPermit = ica['PERMITID'].unique()


# create an empty ag well dataframe 
agWells = pd.DataFrame(columns = ['layer', 'row', 'columns',
        'withdrawal', 'name', 'mon', 'year',
            'monYear', 'rowColPermit', 'rowcol', 'county'])



for permit in unqPermit:
    print(permit)

    dat = allWells[allWells['name'].str.startswith(permit)]

    # concat agwell files
    agWells = pd.concat([agWells, dat], axis = 0)

    # drop agwells from allWells
    allWells.drop(dat.index, axis = 0, inplace = True)


# save as csv
agWells.sort_values(by = 'year')
agWells.to_csv("agWells.csv")
allWells.to_csv("otherWells.csv")
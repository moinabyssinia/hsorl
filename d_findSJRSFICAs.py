"""  
Created on Mon Sep 13 15:30:00 2021

this script filters the AG&LRA wells from
the ECFTX model with the water consumptive
use permit files from SF and SJR

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 

os.chdir("C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\irrigation-module\\01-data")

# these are coming from the district 
# consumptive water use permit file
sf_sjrICA = pd.read_csv("sf_sjr_ica.csv")
# print(sf_sjrICA)

# these are coming from the EXFTX model 
agLra = pd.read_csv("ag_lra.csv")


# getting unique values
sfAGLRA = agLra[~(agLra['PERMITID'] == 'None') & (agLra['DISTRICT'] == 'SFWMD')]
sjrAGLRA = agLra[~(agLra['PERMITID'] == 'None') & (agLra['DISTRICT'] == 'SJRWMD')]

sfAGLRAUnq = sfAGLRA['PERMITID'].unique()
sjrAGLRAUnq = sjrAGLRA['PERMITID'].unique()

# print(sfAGLRAUnq)
# print(sjrAGLRAUnq)

# remove prefix from sf agLra 
getCleanSF = lambda x: x.split('SF_')[1]
getCleanSJR = lambda x: x.split('SJ_')[1]
sfAGLRAUnq = list(map(getCleanSF, sfAGLRAUnq))
sjrAGLRAUnq = list(map(getCleanSJR, sjrAGLRAUnq))

# print(sfAGLRAUnq)
# print(sjrAGLRAUnq)


# filter based on unique values
isSJRICA = sf_sjrICA['OFFCL_PRMT'].isin(sjrAGLRAUnq)
isSFICA = sf_sjrICA['PERMIT_NO'].isin(sfAGLRAUnq)

# print(sf_sjrICA[isSJRICA])
# print(sf_sjrICA[isSFICA])


allSJRSFICA = pd.concat([sf_sjrICA[isSJRICA], sf_sjrICA[isSFICA]], axis = 0)

# combinind sjr and sf icas that match the ones from exftx and CUPs
# print(allSJRSFICA)
# allSJRSFICA.to_csv('allSJRSFICA.csv')

print(sf_sjrICA[sf_sjrICA['PERMIT_NO'] == '56-00343-W'])
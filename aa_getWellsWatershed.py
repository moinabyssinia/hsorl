"""  
Created on tue Sep 28 16:06:00 2021

this script gets the watersheds of the all_wells file
based on the name of the watersheds from the staticWellFile

the staticFile has the watershed names because we have
the x and y coordinates for it - using that we related 
it to the ICAs - we have the watershed names 

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\07-staticFile\\staticWellFile_WS"

os.chdir(dirHome)

# read files
allWells = pd.read_csv("ecftx_tr_20190329_GLRSTA_Counties_allWells.csv")
staticFile = pd.read_csv("staticWellFileByWS.csv")

# allocate a watershed column
allWells['watershed'] = 'nan'

# looping through the staticFile
for well in staticFile['wellID']:
    # print(well)
    
    watershed = staticFile[staticFile['wellID'] == well]['watershed'].values[0]
    
    # find corresponding allWells with this wellID
    allWells.loc[allWells['rowColPermit'] == well, 'watershed'] = watershed

allWells.to_csv("allWells_watershed.csv")


"""  
Created on Tue Sep 21 15:57:00 2021

to clean up the staticWellFile which is grouped
by watersheds

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\"\
                "extractedWellData\\07-staticFile\\gis"

os.chdir(dirHome)

dat = pd.read_csv("staticWellFile_ws_grouped.csv")

dat = dat[['wellID', 'x', 'y', 'level',
       'wellField', 'top', 'bottom', 'depth', 'fraction', 'dfs0File',
       'dfs0Item', 'NAME']]
dat.columns = ['wellID', 'x', 'y', 'level',
       'wellField', 'top', 'bottom', 'depth', 'fraction', 'dfs0File',
       'dfs0Item', 'watershed']

print(dat.columns)

dat.to_csv("staticWellFileCleaned.csv")
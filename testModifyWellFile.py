"""  
Created on Wed Sep 29 17:03:00 2021

testing script
modifying the staticWellFile for the .wel importing

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\07-staticFile"


os.chdir(dirHome)

dat = pd.read_csv("staticWellFileCleaned_ws_ICA.csv")

print(dat.columns)

dat = dat[['wellID', 'x', 'y', 'level', 'depth', 'wellField', 'top', 'bottom', 'dfs0File',
       'dfs0Item', 'fraction']]

# dat.to_csv('staticWellFileCleaned_ws_ICA_columReorganized.csv')

dat.to_csv('staticWellFileCleaned_ws_ICA_columReorganized.csv', 
            sep='\t', index = False,  header=False)
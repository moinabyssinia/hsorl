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

# remove the dfs0 extension from the dfs0File column

removeExt = lambda x: x.split('.dfs0')[0]
dat['dfs0File'] = pd.DataFrame(list(map(removeExt, dat['dfs0File'])))

print(dat['dfs0File'])


dat = dat[['wellID', 'x', 'y', 'level', 'depth', 'wellField', 'top', 'bottom', 'fraction', 
           'dfs0File', 'dfs0Item',]]

# dat.to_csv('staticWellFileCleaned_ws_ICA_columReorganized.csv')

dat.to_csv('staticWellFileCleaned_ws_ICA_columReorganized_v4.csv', 
            sep='\t', index = False,  header=False)
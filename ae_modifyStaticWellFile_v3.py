"""  
Created on Wed Sep 29 17:03:00 2021
modified on Sat Oct 02 17:09:00 2021

testing script
modifying the staticWellFile for the .wel importing

@author: Michael Getachew Tadesse

"""

import os 
import numpy as np
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\extractedWellData\\07-staticFile"

dirDfs0 = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByICA4Dfs0"


os.chdir(dirHome)

dat = pd.read_csv("staticWellFileCleaned_ws_ICA.csv")

# remove the dfs0 extension from the dfs0File column

removeExt = lambda x: x.split('.dfs0')[0]
dat['dfs0File'] = pd.DataFrame(list(map(removeExt, dat['dfs0File'])))

print(dat)


dat = dat[['wellID', 'x', 'y', 'level', 'depth', 'wellField', 'top', 'bottom', 'fraction', 
           'dfs0File', 'dfs0Item',]]

os.chdir(dirDfs0)




# get the dfs0 item number corresponding to each watershed
for well in range(len(dat)):
        print(dat['wellID'][well])
        
        currentWS = dat['dfs0File'][well] + ".csv"
        currentWell = dat['wellID'][well]
        
        os.chdir(dirDfs0)
        
        df = pd.read_csv(currentWS)
        df.drop('Unnamed: 0', axis = 1, inplace = True)
        
        newItemNum = list(df.columns).index(currentWell)

        dat['dfs0Item'][well] = newItemNum
        
        
os.chdir(dirHome)

dat.to_csv('staticWellFileCleaned_ws_ICA_dfs0Numbered_v8.csv', 
            sep='\t', index = False,  header=False)
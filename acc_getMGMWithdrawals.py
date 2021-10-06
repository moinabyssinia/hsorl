"""
created on Wed Oct 06 14:49:00 2021

this program gives the monthly total withdrawal in
million gallons by multiplying the monthly averages
by the number of days of each month

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByWS4Dfs0"
dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByWS4Dfs0_watervolume"


os.chdir(dirHome)

wsList = os.listdir()

for ws in wsList:
    os.chdir(dirHome)
    print(ws)
    
    dat = pd.read_csv(ws)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)
    
    # get the number of days in each month
    getNumDays = lambda x: pd.Period(x).days_in_month
    numDays = pd.DataFrame(list(map(getNumDays, dat['date'])), columns=['days'])
    
    print(dat)
    
    #######################################################
    # multiply by days and divide by million
    dat.iloc[:,1:] = (dat.iloc[:, 1:].multiply(numDays['days']/1000000, axis = "index"))
    #######################################################


    # save it
    os.chdir(dirOut)
    dat.to_csv(ws)    

"""
Created on Wed Aug 25 18:29:00 2021
modified on Wed Sep 29 18:07:00 2021

this program converts the csvs to a format that 
can be used in the dfs0 format

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByICA"
dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\07-staticFile\\wellsByICA4Dfs0"


os.chdir(dirHome)

icaList = os.listdir()

for ica in icaList:
    os.chdir(dirHome)

    print(ica)

    dat = pd.read_csv(ica)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)
    
    dat['mon'] = dat['mon'].replace("AVE", "DEC")
    
        
    # modify month and year format
    getStr = lambda x : str(int(x))
    dat['year'] = pd.DataFrame(list(map(getStr, dat['year'])))
    dat['date'] = dat['mon'] + "-" + dat['year']

#     print(dat['date'])

    # print(dat[['monYear', 'rowColPermit', 'withdrawal']])

    rcpUnique = dat['rowColPermit'].unique()
    # print(rcpUnique)


    dfs0File = pd.DataFrame(dat['date'].unique())
    dfs0File.columns = ['date']

    for rcp in rcpUnique:
        df = dat[dat['rowColPermit'] == rcp]
        newDf = df[['date', 'withdrawal']]
        newDf.columns = ['date', rcp]
        # print(newDf)

        # merge to rcpUnique
        dfs0File = pd.merge(dfs0File, newDf, on="date", how="left")

#     print(dfs0File)
    
    # change dat 'date' to date format
    dfs0File['date'] = pd.to_datetime(dfs0File['date'])
    
    # sort based on date
    dfs0File = dfs0File.sort_values(by = ["date"])
    
    # save ica dfs0 ready csv
    os.chdir(dirOut)
    dfs0File.to_csv(ica)
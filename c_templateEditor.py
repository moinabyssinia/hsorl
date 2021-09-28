"""  
Created on Thu Sep 09 16:42:00 2021

this script modifies the ica template file and saves
new text file per irrigation command areas

@author: Michael Getachew Tadesse

"""
import glob
import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                "ECFTX\\extractedWellData\\07-staticFile"

dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "irrigation-module\\00-scripts\\sampleICAFiles"

dirCombined = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "irrigation-module\\00-scripts\\combinedICAFiles"

dirDfs0 = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "irrigation-module\\01-data\\01-withdrawalsDFS0"

os.chdir(dirHome)

dat = pd.read_csv("staticWellFile.csv")

print(dat)

codeID = 1
for ii in range(len(dat)):
    os.chdir(dirHome)

    print(dat['wellID'][ii])

    saveName = "ica_{}.txt".format(dat['wellID'][ii])

    f = open('icaTemplateFile.txt', 'r')
    fileData = f.read()
    f.close()

    newData = fileData.replace('var_areaName', "'{}'".format(dat['wellID'][ii]))
    newData = newData.replace('var_areaCodeId', "'{}'".format(repr(codeID)))
    newData = newData.replace('var_areaCode', repr(codeID))
    newData = newData.replace('var_sourceType', '2') # single well
    newData = newData.replace('var_xPos', repr(dat['x'][ii]))
    newData = newData.replace('var_yPos', repr(dat['y'][ii]))
    newData = newData.replace('var_top', repr(dat['top'][ii]))
    newData = newData.replace('var_county', dat['dfs0File'][ii])
    newData = newData.replace('var_depth', repr(dat['depth'][ii]))
    newData = newData.replace('var_bottom', repr(dat['bottom'][ii]))
    codeID = codeID + 1


    os.chdir(dirOut)

    f = open(saveName, 'w')
    f.write(newData)
    f.close()


# combine individual ICA files
os.chdir(dirOut)

read_files = glob.glob("*.txt")

with open("combinedICA.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())


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
        "irrigation-module\\00-scripts"

dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "irrigation-module\\00-scripts\\sampleICAFiles"

dirCombined = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "irrigation-module\\00-scripts\\combinedICAFiles"

os.chdir(dirHome)

dat = pd.read_csv("sampleICAPlaceHolders.csv")

for ii in range(len(dat)):
    os.chdir(dirHome)

    print(ii)

    saveName = "ica{}.txt".format(ii)

    f = open('icaTemplateFile.txt', 'r')
    fileData = f.read()
    f.close()

    newData = fileData.replace('var_areaName', "'{}'".format(repr(dat['var_areaName'][ii])))
    newData = newData.replace('var_areaCodeId', "'{}'".format(repr(dat['var_areaCodeId'][ii])))
    newData = newData.replace('var_areaCode', repr(dat['var_areaCode'][ii]))
    newData = newData.replace('var_sourceType', repr(dat['var_sourceType'][ii]))
    newData = newData.replace('var_xPos', repr(dat['var_xPos'][ii]))
    newData = newData.replace('var_yPos', repr(dat['var_yPos'][ii]))
    newData = newData.replace('var_top', repr(dat['var_top'][ii]))
    newData = newData.replace('var_withdrawal', repr(dat['var_withdrawal'][ii]))
    newData = newData.replace('var_depth', repr(dat['var_depth'][ii]))
    newData = newData.replace('var_bottom', repr(dat['var_bottom'][ii]))


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


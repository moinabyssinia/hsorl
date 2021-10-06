import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\ECFTX\\"\
        "extractedWellData\\07-staticFile\\wellsByWS4Dfs0"
        
os.chdir(dirHome)        

dat = pd.read_csv("C-24.csv")

getNumDays = lambda x: pd.Period(x).days_in_month
numDays = pd.DataFrame(list(map(getNumDays, dat['date'])), columns = ["days"])
    
print(numDays)   

# print(dat) 

# df = dat.iloc[:,2:]

print(dat)

dat.iloc[:,2:] = dat.iloc[:,2:].multiply(numDays["days"], axis = "index")

print(dat)
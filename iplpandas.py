import pandas as pd
std=pd.read_csv("apandas/ipl.csv")
print(std[std['season']==2008])
print(std)
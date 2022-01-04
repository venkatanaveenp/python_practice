import pandas as pd
std=pd.read_csv("apandas/Students.csv")

#print(std[std['marks']>=50])
print(std['marks'].max())
print(std['marks'].min())
print(std['marks'].sum())
print(std['marks'].count())

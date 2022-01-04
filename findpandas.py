import pandas as pd
std=pd.read_csv("apandas/Students.csv")
print(std['Name'])
print(std[std['city']=='Pune'])
print(std[std['gender']=='female'])

print(std['marks'].max())
print(std['marks'].min())
print(std['marks'].sum())
print(std['marks'].count())
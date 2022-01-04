import pandas as pd
std=pd.read_csv("apandas/Students.csv")
print(std)
print("======================================================")
std1=pd.read_csv("apandas/Students2.tsv",sep="\t")
print(std1)
print(".................========================================================")
std2=pd.read_excel("apandas/Students3.xlsx")
print(std2)
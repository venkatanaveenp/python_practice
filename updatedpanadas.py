import pandas as pd
std=pd.read_csv("apandas/Students.csv")
data=std.head(5)
print(data)
data.to_csv("apandas/updatedfiles.csv",index=False,sep='\t')
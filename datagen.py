import os
import re
import pandas as pd
from collections import defaultdict
from numpy.random import randint
PATH = "/home/midhilesh/Documents/sem9/IR/corpus/"
queryDoc=[]
for file in os.listdir(PATH):
    queryDoc.append([" ".join(re.findall('[a-zA-Z]+',file[:-3])),file])
df = pd.DataFrame(queryDoc,columns=["Query","Document"])
print(df.head())

dataset=[]
for i in range(df.shape[0]):
    l = (i+10)%(df.shape[0])
    val = randint(l,df.shape[0],1)
    dataset.append([df.iloc[i,0],df.iloc[i,1],1])
    dataset.append([df.iloc[i,0],df.iloc[val,1],0])
dataset = pd.DataFrame(dataset,columns=["query","document","target"])
dataset.to_csv("/home/midhilesh/Documents/sem9/IR/Lab3/dataset.csv",index=False)

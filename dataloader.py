import pandas as pd
from torch import tensor
from torch.utils.data import DataLoader,Dataset
from vectorizer import vectorizer
class WebCorpus(Dataset):
    def __init__(self,dataset,TfIDF,dictonary,LSI):
        self.dataframe = pd.DataFrame(dataset)
        self.vectorizer = vectorizer(dictonary,TfIDF,LSI)
    def __len__(self):
        return self.dataframe.shape[0]
    def __getitem__(self,idx):
        query = self.dataframe.iloc[idx,0]
        document = self.dataframe.iloc[idx,1]
        target = tensor(self.dataframe.iloc[idx,2])
        tquery = tensor(self.vectorizer.transform(query))
        tdoc = tensor(self.vectorizer.transform(document))
        return tquery,tdoc,target
        
class WebDataLoader():
    def __init__(self,TfIDF,dictonary,LSI):
        self.TfIDF = TfIDF
        self.dictonary = dictonary
        self.LSI = LSI
    def getTrainLoader(self,dataset,batch_size):
        return DataLoader(WebCorpus(dataset,self.TfIDF,self.dictonary,self.LSI),batch_size=batch_size)
    def getTestLoader(self,dataset,batch_size):
        return DataLoader(WebCorpus(dataset,self.TfIDF,self.dictonary,self.LSI),batch_size=batch_size)
    def getValidationLoader(self,dataset,batch_size):
        return DataLoader(WebCorpus(dataset,self.TfIDF,self.dictonary,self.LSI),batch_size=batch_size)

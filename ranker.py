from model import MLP
from vectorizer import vectorizer
from tf_idf import TfIdfConverter
from latent_semantic_indexing import LSI
from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
import pandas as pd
class Ranker():
    def __init__(self,PATH,documentset):
        self.tfidf_model = TfIdfConverter().load(PATH+"tfidf")
        self.lsi_model = LSI(self.tfidf_model,6).load(PATH+"LSI")
        self.doc2vec = vectorizer(Dictionary,self.tfidf_model,self.lsi_model)
        self.rankerModel = MLP(6)
        self.rankerModel.load_state_dict(PATH+"MLP")
        self.documentset = pd.DataFrame(documentset)
    def getRelaventDocuments(self,query):
        queryVec = self.doc2vec.transform(simple_preprocess(query))
        for i in range(self.documentset.shape[0]):
            documentPath = self.documentset.iloc[i,0]
            docVec = self.doc2vec.transform(simple_preprocess(self.documentset.iloc[i,1]))
            print("Document:", documentPath, "Rank:", self.rankerModel(queryVec,docVec))
if __name__ == "__main__":
    searchEngine = Ranker("home/Document/sem9/IR/Lab3","home/Document/sem9/IR/Lab3/document")
    query = input("Enter input query:")
    searchEngine.getRelaventDocuments(query)


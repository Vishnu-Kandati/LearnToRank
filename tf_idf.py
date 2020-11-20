from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from preprocess import ReturnTokens
class TfIdfConverter(object):
    def __init__(self):
        self.tfidf=None
    def fit(self,dir_path):
        gensim_corpus = [Dictionary().doc2bow(token) for token in ReturnTokens(dir_path)]
        self.tfidf = TfidfModel(gensim_corpus,smartirs='npu')
        return self.tfidf
    def load(self,path):
        self.tfidf = TfidfModel.load(path)
        return self.tfidf
    def transform(self,BOW):
        return self.tfidf[BOW]


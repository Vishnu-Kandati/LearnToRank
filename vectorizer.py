from gensim.parsing.preprocessing import preprocess_string
from gensim.corpora import Dictionary
class vectorizer():
    def __init__(self,dictionary, TfIDF, LSI):
        self.dictionary = dictionary
        self.TfIDF= TfIDF
        self.LSI = LSI
    def transform(self,inputString):
        processed_string = preprocess_string(inputString)
        bow =  [self.dictionary.doc2bow(text) for text in processed_string]
        tfidf = self.TfIDF[bow]
        return self.LSI[tfidf]



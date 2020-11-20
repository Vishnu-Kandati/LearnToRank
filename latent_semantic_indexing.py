from gensim.models import LsiModel
class LSI():
    def __init__(self,tf_idf,num_topics):
        self.num_topics = num_topics
        self.tf_idf = tf_idf
        self.lsi=None
    def fit(self):
        self.lsi = LsiModel(self.tf_idf,self.num_topics)
        return self.lsi
    def load(self,path):
        self.lsi = LsiModel.load(path)
        return self.lsi
    def transform(self,tfidf_vector):
        return self.lsi[tfidf_vector]

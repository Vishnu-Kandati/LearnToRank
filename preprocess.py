from gensim.utils import simple_preprocess
import os

class ReturnTokens(object):
    def __init__(self, dir_path):
        self.dir_path = dir_path
    def __iter__(self):
        for file_name in os.listdir(self.dir_path):
            for sentence in open(os.path.join(self.dir_path, file_name)):
                yield simple_preprocess(sentence)


from model import MLP
from dataloader import WebDataLoader
from tf_idf import TfIdfConverter
from latent_semantic_indexing import LSI
from trainer import Trainer
from gensim.corpora import Dictionary
from torch.optim import Adam
from torch.nn import BCELoss
from torch import save

PATH = "home/Documents/sem9/IR/Lab3/"
tfidf = TfIdfConverter()
tfidf_model = tfidf.fit(PATH+"corpus")
tfidf_model.save(PATH+"tfidf")

lsi = LSI(tfidf_model,6)
lsi_model = lsi.fit()
lsi_model.save(PATH+"LSI")

dataloader = WebDataLoader(tfidf_model,Dictionary,lsi_model)
trainLoader = dataloader.getTrainLoader("train.csv",20)
validLoader = dataloader.getValidationLoader("valid.csv",20)
testLoader = dataloader.getTestLoader("test.csv",10)

NN = MLP(6)
optimizer = Adam(NN.parameters(),lr=0.001)
criterion = BCELoss()
modelTrainer = Trainer(NN,optimizer,criterion,device="cuda")
testOutput, validationOutput = modelTrainer.fit(trainLoader,validLoader,testLoader,1000,10)
save(modelTrainer.model.state_dict(),PATH+"MLP")




from sklearn.metrics import precision_score,recall_score,f1_score
class Trainer():
    def __init__(self,model,optimizer,loss_function,device):
        self.optimizer = optimizer
        self.criterion = loss_function
        self.device = device
        self.model = model.to(device)

    def train(self,trainLoader):
        self.model.train()
        trainLoss=0
        for query, document, target in trainLoader:
            query = query.to(self.device)
            document = document.to(self.device)
            target = target.to(self.device)
            output = self.model(query,document)
            loss = self.criterion(output,target)
            trainLoss+=loss.item()
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        trainLoss/=len(trainLoader.dataset)
        return trainLoss
    
    def evaluvate(self,dataloader):
        self.model.eval()
        eval_loss=0
        eval_precision=0
        eval_recall=0
        eval_f1score=0
        for query, document, target in dataloader:
            query = query.to(self.device)
            document = document.to(self.device)
            target = target.to(self.device)
            output = self.model(query,document)
            loss = self.criterion(output,target)
            eval_loss+=loss.item()
            eval_precision+=precision_score(target.item(),output.item(),average="micro")
            eval_recall+=recall_score(target.item(),output.item(),average="micro")
            eval_f1score+=f1_score(target.item(),output.item())
        eval_loss/=len(dataloader.dataset)
        eval_precision/=len(dataloader.dataset)
        eval_recall/=len(dataloader.dataset)
        eval_f1score/=len(dataloader.dataset)
        return eval_loss,eval_precision,eval_recall,eval_f1score
      

    def fit(self,trainLoader,validLoader,testLoader,epochs,checkpoint):
        testMetric={}
        validMetric={}
        for epoch in epochs:
            self.train(trainLoader)
            if(epoch%checkpoint==0):
                a,b,c,d=self.evaluvate(validLoader)
                validMetric[epoch]=[a,b,c,d]
                a,b,c,d=self.evaluvate(testLoader)
                testMetric[epoch]=[1,b,c,d]
        return testMetric,validMetric



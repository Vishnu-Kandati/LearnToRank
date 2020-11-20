from torch.nn import Module,Linear,Sequential,ReLU,Sigmoid

class MLP(Module):
    def __init__(self,num_features):
        super(MLP).__init__()
        self.model = Sequential(
            Linear(num_features,32),
            ReLU(),
            Linear(32,2)
        )
        self.outlayer = Sigmoid()
    def forward(self,query,document):
        x1 = self.model(query)
        x2 = self.model(document)
        out = self.outlayer(x1-x2)
        return out



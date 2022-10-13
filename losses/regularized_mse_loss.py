import torch

EPS = 1e-2
esp = 1e-8

class Regularized_MSE_Loss(torch.nn.Module):

    def __init__(self):
        super(Regularized_MSE_Loss, self).__init__()

    def forward(self, p, g):
        g = g.view(-1, 1)
        p = p.view(-1, 1)
        loss = 1 - (torch.sqrt(p * g + esp) + torch.sqrt((1 - p) * (1 - g) + esp))
        for i in nn.parameters:

        return torch.mean(loss)

import torch


class Network(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = torch.nn.Linear(3, 2, bias=False)
        self.fc2 = torch.nn.Linear(3, 1, bias=False)
        self.fc1.weight.data = torch.tensor([[1.5, 2.5, 1], [2, -1.5, -3]])
        self.fc2.weight.data = torch.tensor([-1, 1, 0.5])

    def forward(self, x):
        x = torch.cat([torch.ones((1)), x], dim=0)
        x = self.fc1(x)
        x = torch.sigmoid(x)
        print("h", x)
        x = torch.cat([torch.ones((1)), x], dim=0)
        x = self.fc2(x)
        y = torch.sigmoid(x)
        print("y", y)
        return y


net = Network()
print(list(net.parameters()))
optim = torch.optim.SGD(net.parameters(), lr=1)

y = net(torch.tensor([0, 1]))
loss = 0.5 * (1 - y) ** 2
optim.zero_grad()
loss.backward()
print(net.fc1.weight.grad)
print(net.fc2.weight.grad)
optim.step()
print(list(net.parameters()))
y = net(torch.tensor([0, 1]))
loss = 0.5 * (1 - y) ** 2
print(loss)

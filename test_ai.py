import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from random import randint

"""
def infinity(from_val: int):
    val = from_val
    while 1:
        yield val
        val += 1
    
five_to_inf = infinity(5)

losses = (x**2 for x in range(10))
print(next(losses))

"""

losses = []

model = nn.Sequential(
    *(nn.Linear(2, 2)       # unpaking
      for _ in range(20)),
    nn.Linear(2,1),
    nn.Sigmoid()
)

print(model)

loss_fn = nn.BCELoss()
optimizer = optim.Adam(model.parameters(),lr=0.01)

for i in range(1000):

    input_l = [randint(0,2), randint(0,2)]
    output_l = []

    if (input_l[0] == 0):
        output_l = [0]
    else:
        output_l = [1]

    input_l = torch.tensor(np.array(input_l), dtype=torch.float32)
    output_l = torch.tensor(np.array(output_l), dtype=torch.float32)

    pred_l = model(input_l)

    loss = loss_fn(pred_l,output_l)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    losses.append(loss.item())

plt.plot(losses)
plt.show()
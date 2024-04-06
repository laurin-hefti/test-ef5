import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import time

def generate_pol_func():
    pol_grad = randint(1,4)

    coef = [0,0,0,0]

    for i in range(pol_grad):
        coef[i] = randint(-5,5)

    return coef

def get_point_of_pol(x,coef):
    return coef[0] + coef[1]*x + coef[2]*(x*x) + coef[3]*(x*x*x)

def generate_points(coef):
    points = []

    for i in range(-2,3):
        points.append(i)
        points.append(get_point_of_pol(i,coef))

    return points

def conv_pol_to_img(coef, size=32, raw=False):
    size = int(size/2)
    img = []

    for x in range(-size,size):
        y = get_point_of_pol((x/size)*8,coef) # convert poly func to space -4, 4
        for y_h in range(-size,size):

            col = [0,0,0]

            if round(y)-0 <= round((y_h/size)*8) and round(y)+0 >= round((y_h/size)*8):
                col = [255,255,255]

            if raw:
                if col == [0,0,0]:
                    col = 0
                if col == [255,255,255]:
                    col = 100
            
            img.append(col)
    
    return img

def conv_img_to_arrimg(img,size=32):
    new_img = []

    for i in range(len(img)):
        if i % size == 0:
            new_img.append([])
        new_img[-1].append(img[i])

    return new_img

model = nn.Sequential(
    nn.Linear(10,10),
    nn.ReLU(),
    nn.Linear(10,10),
    nn.ReLU(),
    nn.ReLU(),
    nn.Linear(10,4)
)

model2 = nn.Sequential(
    nn.Conv2d(1, 1, kernel_size=(2,2),stride = 1),
    ##nn.ReLU(),
    nn.MaxPool2d(kernel_size=(2,2),stride=(1,1)),
    nn.ReLU(),
    nn.Flatten(),

    nn.Linear(900, 200),
    nn.ReLU(),
    nn.Linear(200,4)
    #nn.MaxPool2d(2, 2),
    #nn.Conv2d(16, 32, 3),
    #nn.ReLU(),
    #nn.MaxPool2d(2, 2),
    #nn.Linear(int(128 * 128 * 32 /2 /2 /2 /2) + 1, 4)
)

model2 = torch.load("C:/Users/l.hefti/Desktop/test-ef5/model2")
model2.eval()

loss_fn = nn.L1Loss()
optimizer = optim.Adam(model2.parameters(),lr=0.001)

# best for predicting polf l1loss with adam lr=0.0005 20000 steps

losses = []

show_image: bool = False

for i in range(10000):
    pol = generate_pol_func()
    img = conv_pol_to_img(pol,32, True)
    img = conv_img_to_arrimg(img, 32)
    #img = np.array(img).reshape(32, 32)
    #img.insert(0,1)
    #img.insert(0,0)

    input_l = torch.tensor(np.array(img), dtype=torch.float32)
    input_l = torch.unsqueeze(input_l,0)
    output_l = torch.tensor(np.array(pol), dtype=torch.float32)

    if show_image:
        plt.imshow(conv_img_to_arrimg(img,32))
        plt.show()
        time.sleep(5)

    pred_l = model2(input_l)

    loss = loss_fn(pred_l,output_l)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    if (i % 100 == 0):
        print(str(i/10)+"%")

for i in range(0):

    pol = generate_pol_func()
    points = generate_points(pol)

    input_l = torch.tensor(np.array([*points]), dtype=torch.float32)
    output_l = torch.tensor(np.array([*pol]), dtype=torch.float32)

    pred_l = model(input_l)

    loss = loss_fn(pred_l,output_l)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    #print(loss.item())
    if (i % 1000 == 0):
        print(str(i / 100)+"%")

#test_l = torch.tensor(np.array(generate_points([0,-3,2,4])), dtype=torch.float32)
#output = model(test_l)
#print(output)

"""
img = conv_pol_to_img([0,0,2,0], 256)
img = conv_img_to_arrimg(img,256)
plt.imshow(img)
plt.show()
"""

#img = conv_pol_to_img([2,-3,2,1],23,True)
#input_l = torch.tensor(np.array([*img]), dtype=torch.float32)
#output = model2(input_l)
#print(output)

#model2.state_dict()
torch.save(model2, "C:/Users/l.hefti/Desktop/test-ef5/model2")
plt.plot(losses)
plt.show()
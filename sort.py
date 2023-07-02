import pandas as pd
import torch

# Read the text file into a pandas DataFrame
df = pd.read_csv('sp2019.txt', delimiter=',')

# separating the data
def create_x():
    X = []

    start = [0] * 360

    X.append(start)

    for i in range(97740):
        if i  % 390 == 0:
            front = start
        else:
            front = X[i]
        front = front[1:] + [df['Open'][i]]
        front = front[1:] + [df['High'][i]]
        front = front[1:] + [df['Low'][i]]
        front = front[1:] + [df['Close'][i]]
        # front = front[1:] + [df['Open'][0]]
        X.append(front)
        # if i % 390 == 0:
            
    X.pop(0)
    return X

def create_y(X):
    Y = []
    for i in range(1): # make the Y variable list
        if df['Close'][i+10] > X[i][359]:
            Y.append(1)
        else:
            Y.append(0)

X = create_x()

Y = create_y(X)

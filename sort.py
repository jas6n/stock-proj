import pandas as pd
import torch

# Read the text file into a pandas DataFrame
df = pd.read_csv('sp2019.txt', delimiter=',')

col = df['Minute'] # every 390 indices it starts another day

# separating the data
X = []

start = [0] * 400

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

# test
t = 97739
print(X[t])
print(X[t][396:400])

print([df['Open'][t], df['High'][t], df['Low'][t], df['Close'][t]])



# Open the file in write mode
with open('usable_x.txt', 'w') as file:
    # Iterate over the list and write each element to a new line
    for item in X:
        file.write(str(item))
        file.write('/n')

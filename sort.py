import pandas as pd

# Read the text file into a pandas DataFrame
df = pd.read_csv('sp2019.txt', delimiter=',')
print(df)

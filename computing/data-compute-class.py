import pandas as pd

from  classes import ttAnalyzer

ds = pd.read_csv('/Users/excise/code/ML/computing/data.csv').to_numpy()

game = ttAnalyzer(ds)

print(game.combinations())
print("/n")
print(game.frequency())
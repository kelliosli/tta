import pandas as pd 
import numpy as np

import services

ds = pd.read_csv('/Users/excise/code/ML/computing/data.csv').to_numpy()

points = services.to_points(ds)
# print(points)
res = services.statsU(points,5)
print(services.average_len(points))
print(res)
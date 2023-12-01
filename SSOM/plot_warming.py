import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('input_data/warming_70years_japan.csv', index_col=0)

fig = plt.figure(figsize=(8, 4))
ax = plt.axes([.05,0.05,.9,.9] )


x = df.columns.astype(int)
y = df.values.T
ax.plot(x, y)
ax.set_xlabel('year')
ax.set_ylabel('warming rate ($^oC$)')























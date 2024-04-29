import pandas as pd
import matplotlib.pyplot as plt

amzn = pd.read_csv("data/Amzn.csv")
print(amzn.dtypes)
print(amzn)

#print(amzn['High'])
amzn.plot()
plt.show()

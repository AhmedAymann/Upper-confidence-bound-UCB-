# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing the Dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")


# implementing Random selecttion
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward


#visualising the results - histogram
plt.hist(ads_selected)
plt.title("histogram of ads selections")
plt.xlabel("ads")
plt.ylabel("number of times each ad was clicked")
plt.show()
    
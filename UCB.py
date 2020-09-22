# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing the Dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")


# implementing UCB
import math

round_number = 10000
Ad_number = 10
adds_selected = []



numbers_of_selections = [0] * Ad_number
sums_of_rewards = [0] * Ad_number
total_reward = 0
for n in  range(0, round_number):
    ad = 0
    max_upper_bound = 0
    for i in range(0, Ad_number):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    adds_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
    
# visualising the results
plt.hist(adds_selected)
plt.title("histogram of ads selections")
plt.xlabel("ads")
plt.ylabel("number of selections")
plt.show()


    

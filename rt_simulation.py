print("Reaction Time Simulation (trial)")

import numpy as np
import pandas as pd
import random

#Hick's law parameters

a=200   #base processing time (ms)
b=50    # decision complexity factor

# possible number of choices in eperiment
choices_list = [1,2,8,9]

trials=[]

#stimulate 1000 trials
for i in range (100):

    choices = random.choice(choices_list)

#Hick's law Formula
reaction_time = a+b* np.log2(choices)

#add human noise/variability
noise = np.random.normal(0,16)

reaction_time = reaction_time + noise

trials.append({
    "Choices": choices,
    "reaction_time": round(reaction_time,2)
})

#Create DataFrame
df = pd.DataFrame(trials)

print("/nAverage reaction time:", df["reaction_time"].mean())

#save dataset
df.to_csv("reaction_time.csv", index=False)

print("/nData saved to reaction_data.csv")



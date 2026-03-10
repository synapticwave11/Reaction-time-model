print("Reaction Time Simulation")

import numpy as np
import pandas as pd



# possible number of choices in eperiment
choices_list = [1,2,4,8,16]

data=[]

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







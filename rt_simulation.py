print("Reaction Time Simulation")

import numpy as np
import pandas as pd



# possible number of choices in eperiment
choices_list = [1,2,4,8,16]

data=[]
for choices in choices_list:
             for trial in range (50):  #generates 50 trials per condition
#Hick's law
reaction_time = 200 + 150 *  np.log2(choices)

#add random noise
reaction_time = np.random.normal(0,20)
data.append([choices,reaction_time])











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













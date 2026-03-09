import pandas as pd
import matplotlib.pyplot as plt

#load the dataset created by the simulation file.
df= pd.read_csv("reaction_time.csv")

# calculate average reaction time for each condition
avg_rt =df.groupby("choices")["reaction_time"].mean()

#plot
plt.figure(figsize=(6,4))
plt.plot(avg_rt.index, avg_rt.values, marker='o')

plt.title("Hick's Law Simulation")
plt.xlabel("Number of choices")
plt.ylabel("Reaction Time (ms)")


plt.show()




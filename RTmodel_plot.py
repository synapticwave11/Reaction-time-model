import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("reaction_time.csv")

# sort values so the graph connects properly
df = df.sort_values("choices")

# plot
plt.figure()
plt.plot(df["choices"], df["reaction_time"], marker='o')
plt.title("Reaction Time vs Number of Choices")
plt.xlabel("Number of Choices")
plt.ylabel("Reaction Time (ms)")
plt.grid(True)

plt.show()










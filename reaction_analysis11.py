print("reaction time model")

import pandas as pd
import numpy as np

data = {
    "choices": [1,2,3,4,8],
    "reaction_time": [210,240,270,330,240]
}

df = pd.DataFrame(data)

print(df)

print("Average reaction time:", np.mean(df["reaction_time"]))

print("Average per condition:" )
print(df.groupby("choices")["reaction_time"].mean())

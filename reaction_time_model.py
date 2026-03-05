print("reaction time model")

import pandas as pd
import numpy as np

data = {"reaction_time": [210,230,180,250,210]
}

df = pd.DataFrame(data)

print(df)
print("Average:", np.mean(df["reaction_time"]))


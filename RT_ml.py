import pandas as np
import numpy as np
from sklearn.linear_model import LinearRegression

#load dataset and analyisis
df = pd.read_csv("reaction_time.csv")

#Hick'slaw uses log2 of choices
df["log_choices"] = np.log2(df["choices"])

#Features and target
X = df[["log_choices"]]
y = df["reaction_time"]

#Train model
model = LinearRegression()
model.fit(X, y)

print("Model trained")

#prediction example
new_choices = 6
log_value = np.log2(new_choices)

new_data = pd.DataFrame({"log_choices": [log_value]})
prediction = model.predict(new_data)

print(f"Predicted reaction time for {new_choices} choices: {prediction[0]:.2f} ms")

#Measuring Model performance
from sklear.metrics import r2_score
predictions= model.predict (x)




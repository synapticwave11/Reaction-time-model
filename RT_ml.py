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

# Predict multiple values
print("\nPredictions:")
for i in (3,6,10,20):
    
    log_value = np.log2(i)
    new_data = pd.DataFrame({"log_choices":[log_value]})
    
    prediction= model.predict(new_data)
    print(f"Predicted reaction time for {i} choices: {prediction[0]:.2f} ms")            

#Measuring Model performance

from sklearn.metrics import r2_score

predictions= model.predict (X)

r2=r2_score(y,predictions)

print(f"Model R2 score: {r2:.3f}")




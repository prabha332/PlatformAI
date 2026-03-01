import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data/incidents.csv")

X = data[["cpu", "memory", "restarts"]]
y = data["incident"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(
    model,
    open("models/incident_model.pkl", "wb")
)

print("Model trained successfully")

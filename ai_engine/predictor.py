# Incident Prediction Model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("data/incidents.csv")

X = data[["cpu","memory","restarts"]]
y = data["incident"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/incident_model.pkl","wb"))

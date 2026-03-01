# Incident Prediction Model
# Train Model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("data/incidents.csv")

X = data[["cpu","memory","restarts"]]
y = data["incident"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/incident_model.pkl","wb"))

# Predict Failure
import pickle

model = pickle.load(
    open("models/incident_model.pkl","rb")
)

def predict(cpu, memory, restarts):
    result = model.predict([[cpu,memory,restarts]])
    return result[0]

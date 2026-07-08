import joblib

model = joblib.load("models/PHEA_Final_Model.pkl")

booster = model.get_booster()

print()

print("MODEL FEATURES")

print()

for i, f in enumerate(booster.feature_names):

    print(i + 1, f)

print()

print("TOTAL FEATURES =", len(booster.feature_names))
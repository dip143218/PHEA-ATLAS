import os
import pandas as pd

files = [
    "PHEA_ATLAS_V10_READY.csv",
    "PHEA_ATLAS_V8_5_FINAL_DATASET.csv",
    "phea_final_model_ready.csv",
    "phea_physics_informed_v6.csv",
    "phea_with_omega_lambda_v8.csv",
    "v10_selected_features.csv",
    "element_properties_verified.csv"
]

for file in files:

    path = os.path.join("data", file)

    print("=" * 90)
    print(file)

    try:

        df = pd.read_csv(path)

        print("Rows    :", len(df))
        print("Columns :", len(df.columns))

        print("\nColumn Names:")

        for i, c in enumerate(df.columns):
            print(f"{i+1:02d}. {c}")

        print("\nFirst Row:\n")
        print(df.head(1).T)

    except Exception as e:

        print("ERROR :", e)

    print("\n")
    import joblib

model = joblib.load("models/PHEA_Final_Model.pkl")

print(type(model))

print()

try:

    booster = model.get_booster()

    print("=== FEATURE NAMES ===")

    for i, f in enumerate(booster.feature_names):
        print(i+1, f)

except Exception as e:

    print(e)
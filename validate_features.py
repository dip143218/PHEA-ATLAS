import pandas as pd

from feature_calculator import FeatureCalculator

calc = FeatureCalculator()

df = pd.read_csv(
    "data/phea_with_omega_lambda_v8.csv"
)

row = df.iloc[0]

elements = [

    row["el1"],
    row["el2"],
    row["el3"],
    row["el4"],
    row["el5"]

]

compositions = [

    20,
    20,
    20,
    20,
    20

]

physics = calc.calculate(
    elements,
    compositions
)

print()

print("========== DATASET ==========")

print(row[[
    "Alloy_DeltaHmix_kJmol",
    "delta_radius",
    "Omega",
    "Lambda",
    "mean_atomic_radius_pm",
    "mean_density",
    "mean_melting_point_K",
    "mean_vec"
]])

print()

print("========== OUR ENGINE ==========")

for k,v in physics.items():

    print(k,v)
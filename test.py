import pandas as pd

df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\PHEA-ATLAS-AI\data\element_properties_verified.csv")

print(df.columns.tolist())

print(df.head())
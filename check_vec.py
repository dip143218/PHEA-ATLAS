import pandas as pd

props = pd.read_csv("data/element_properties_verified.csv")

print(props[["element","VEC"]])
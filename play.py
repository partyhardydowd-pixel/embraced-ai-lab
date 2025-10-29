import numpy as np, pandas as pd
a = np.arange(0,10,2)
df = pd.DataFrame({"x": a, "x2": a**2})
print(df.head())
df.to_csv("outputs/sample.csv", index=False)

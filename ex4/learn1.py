from pathlib import Path

import dataset1
from sklearn.linear_model import LinearRegression

df = dataset1.read_tsv(dataset1.PROJECT_ROOT / Path("tsv/output.tsv"))

model = LinearRegression()


print(df)

from pathlib import Path

import dataset1
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# %%

df = dataset1.read_tsv(dataset1.PROJECT_ROOT / Path("tsv/output.tsv"))

# %%

model = LinearRegression()

# %%

X = df["観測点"]
y = df["観測値"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, shuffle=False)


# %%

print(df)
# %%

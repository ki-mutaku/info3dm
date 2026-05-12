import dataset1
from sklearn.linear_model import LinearRegression

df = dataset1.read_tsv("./ex4/output.tsv")

model = LinearRegression()

print(df)

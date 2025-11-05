import polars as pl

data = pl.read_csv("bitcoin.csv")
print(data)
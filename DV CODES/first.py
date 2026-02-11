#first program to read csv file in python
import pandas as pd
filename = "records.csv"

data = pd.read_csv("records.csv")
print(data)


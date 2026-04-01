import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("questionS_1.csv")

df.columns = df.columns.str.strip()
df["STATE"] = df["STATE"].str.strip()

df["DATE"] = pd.to_datetime(df["DATE"], dayfirst=True)

print(df.head())

state_data = df.groupby("STATE")["CONFIRMED"].sum()

state_data.plot(kind="bar")
plt.title("Confirmed cases across states")
plt.xlabel("State")
plt.ylabel("Confirmed cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.boxplot(x=df["DEATHS"])
plt.title("Variation in death cases")
plt.show()

max_state = df.groupby("STATE")["CONFIRMED"].sum().idxmax()
print("State with highest confirmed cases:", max_state)

print(df[["CONFIRMED", "RECOVERED", "DEATHS"]].describe())

date_data = df.groupby("DATE")["CONFIRMED"].sum()

plt.figure(figsize=(10,5))
date_data.plot(kind="line", marker='o')
plt.title("Trend of Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.grid(True)
plt.tight_layout()
plt.show()
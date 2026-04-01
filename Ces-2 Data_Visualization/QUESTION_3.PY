import pandas as pd
import matplotlib.pyplot as plt
customers = ["C1","C2","C3","C4","C5","C6","C7","C8"]

account_type = ["Savings","Current","Savings","Savings",
                "Current","Savings","Current","Savings"]

balance = [50000,120000,75000,30000,150000,45000,110000,60000]

transactions = [15,25,18,10,30,12,28,20]

loan_status = ["No","Yes","No","No","Yes","No","Yes","No"]

df = pd.DataFrame({
    "Customer": customers,
    "Account_Type": account_type,
    "Balance": balance,
    "Transactions": transactions,
    "Loan_Status": loan_status
})

print(df)
plt.hist(df["Balance"], bins=5)
plt.title("Distribution of Account Balance")
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.show()
account_counts = df["Account_Type"].value_counts()

plt.pie(account_counts, labels=account_counts.index, autopct="%1.1f%%")
plt.title("Account Type Distribution")
plt.show()

high_balance = df[df["Balance"] > 100000]
print(high_balance[["Customer", "Balance"]])
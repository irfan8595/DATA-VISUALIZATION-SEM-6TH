import matplotlib.pyplot as plt
months = ['jan', 'feb','mar','april','may','june']
sales = [120, 150, 170,160,180,200]
plt.plot(months, sales)
plt.xlabel("months")
plt.xlabel("sales(in units)")
plt.title("Monthly sales trend")
plt.show()


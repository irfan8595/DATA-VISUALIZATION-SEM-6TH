import matplotlib.pyplot as plt
unit =[120,130,140,150,160,111,133,123,132,234,543,654,767,786,867,995,334,554,433,564,345,234,543,786,908,500,600,700,120,234,501,506,507,406,408]
plt.hist(unit, bins=4)
plt.xlabel("Electricity consumption (units)")
plt.ylabel("Number of households")
plt.title("Monthly Electricity Consumption Distribution")
plt.show()
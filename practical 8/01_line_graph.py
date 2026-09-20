# Plot a Line graph showing the monthly sales of a company. Add a title,
# x-axis label, y-axis label, and a legend.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_2023 = [12000, 15000, 14000, 18000, 22000, 24000, 21000, 26000, 28000, 31000, 35000, 42000]
sales_2024 = [14000, 17000, 16500, 21000, 25000, 28000, 27000, 30000, 33000, 37000, 41000, 48000]

plt.figure(figsize=(10, 5))
plt.plot(months, sales_2023, marker="o", color="blue", linewidth=2, label="Sales 2023")
plt.plot(months, sales_2024, marker="s", color="green", linestyle="--", linewidth=2, label="Sales 2024")

plt.title("Company Monthly Sales Trend", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales in USD ($)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()

print("Displaying Line Graph...")
plt.show()

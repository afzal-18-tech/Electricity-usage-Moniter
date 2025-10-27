import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take input from user
months = []
units_list = []
cost_list = []

n = int(input("Enter number of months: "))

for i in range(n):
    print(f"\nMonth {i+1}:")
    month = input("Enter month name: ")
    units = float(input("Enter units consumed: "))
    cost_per_unit = float(input("Enter cost per unit: "))

    months.append(month)
    units_list.append(units)
    cost_list.append(cost_per_unit)

# Step 2: Convert to NumPy arrays
units = np.array(units_list)
cost_per_unit = np.array(cost_list)

# Step 3: Calculate total and averages
monthly_cost = units * cost_per_unit
total_units = np.sum(units)
avg_units = np.mean(units)
total_cost = np.sum(monthly_cost)

# Step 4: Print analysis result
print("\nElectricity Usage Summary:")
print("----------------------------")
print(f"Total Units Consumed: {total_units}")
print(f"Average Monthly Usage: {avg_units:.2f}")
print(f"Total Cost: ₹{total_cost:.2f}")

# Step 5: Plot line chart for units
plt.figure(figsize=(8, 4))
plt.plot(months, units, marker='o', color='b', linewidth=2)
plt.title("Monthly Electricity Usage")
plt.xlabel("Month")
plt.ylabel("Units Consumed")
plt.grid(True)
plt.show()

# Step 6: Plot bar chart for monthly cost
plt.figure(figsize=(8, 4))
plt.bar(months, monthly_cost, color='green', edgecolor='black')
plt.title("Monthly Electricity Cost")
plt.xlabel("Month")
plt.ylabel("Cost (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

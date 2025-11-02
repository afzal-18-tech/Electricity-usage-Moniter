import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from datetime import date

# ---------- Database Connection Function ----------
def insert_into_db(month, units, cost_per_unit, total_cost):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="electricity_db"
        )
        cursor = conn.cursor()
        query = """
        INSERT INTO usage_data (month_name, units_consumed, cost_per_unit, total_cost, entry_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (month, units, cost_per_unit, total_cost, date.today()))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error inserting data:\n{e}")

# ---------- Data Lists ----------
months, units_list, cost_list = [], [], []

# ---------- Functions ----------
def add_data():
    month = month_entry.get()
    try:
        units = float(units_entry.get())
        cost_per_unit = float(cost_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values for units and cost.")
        return

    total = units * cost_per_unit
    months.append(month)
    units_list.append(units)
    cost_list.append(cost_per_unit)
    insert_into_db(month, units, cost_per_unit, total)

    tree.insert("", "end", values=(month, units, cost_per_unit, total))
    month_entry.delete(0, tk.END)
    units_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)

    messagebox.showinfo("Success", f"Data for {month} added successfully!")

def analyze_data():
    if not months:
        messagebox.showwarning("No Data", "Please add data before analyzing.")
        return

    units = np.array(units_list)
    cost_per_unit = np.array(cost_list)
    monthly_cost = units * cost_per_unit

    total_units = np.sum(units)
    avg_units = np.mean(units)
    total_cost = np.sum(monthly_cost)

    result_label.config(
        text=f"Total Units: {total_units}\nAverage Usage: {avg_units:.2f}\nTotal Cost: ₹{total_cost:.2f}"
    )

def show_graphs():
    if not months:
        messagebox.showwarning("No Data", "Please add data before viewing graphs.")
        return

    units = np.array(units_list)
    cost_per_unit = np.array(cost_list)
    monthly_cost = units * cost_per_unit

    # Line Chart
    plt.figure(figsize=(8, 4))
    plt.plot(months, units, marker='o', color='b', linewidth=2)
    plt.title("Monthly Electricity Usage")
    plt.xlabel("Month")
    plt.ylabel("Units Consumed")
    plt.grid(True)
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 4))
    plt.bar(months, monthly_cost, color='green', edgecolor='black')
    plt.title("Monthly Electricity Cost")
    plt.xlabel("Month")
    plt.ylabel("Cost (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Electricity Usage Monitor")
root.geometry("700x600")
root.config(bg="#f3f3f3")

title = tk.Label(root, text="Electricity Usage Monitor", font=("Arial", 18, "bold"), bg="#f3f3f3", fg="#333")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f3f3f3")
frame.pack(pady=5)

tk.Label(frame, text="Month Name:", font=("Arial", 12), bg="#f3f3f3").grid(row=0, column=0, padx=5, pady=5, sticky="e")
month_entry = tk.Entry(frame, width=25)
month_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Units Consumed:", font=("Arial", 12), bg="#f3f3f3").grid(row=1, column=0, padx=5, pady=5, sticky="e")
units_entry = tk.Entry(frame, width=25)
units_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Cost per Unit:", font=("Arial", 12), bg="#f3f3f3").grid(row=2, column=0, padx=5, pady=5, sticky="e")
cost_entry = tk.Entry(frame, width=25)
cost_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f3f3f3")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Data", command=add_data, width=15, bg="#0078D7", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Analyze Data", command=analyze_data, width=15, bg="#28A745", fg="white").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Show Graphs", command=show_graphs, width=15, bg="#17A2B8", fg="white").grid(row=0, column=2, padx=10)

# Table View
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("Month", "Units", "Cost per Unit", "Total Cost")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=6)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")
tree.pack()

# Results
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f3f3f3", fg="#333")
result_label.pack(pady=10)

root.mainloop()

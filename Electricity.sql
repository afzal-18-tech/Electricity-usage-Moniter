CREATE DATABASE electricity_db;
USE electricity_db;

CREATE TABLE usage_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month_name VARCHAR(20),
    units_consumed FLOAT,
    cost_per_unit FLOAT,
    total_cost FLOAT,
    entry_date DATE
);

-- View all data
SELECT * FROM usage_data;

-- Calculate total units and total cost
SELECT SUM(units_consumed) AS Total_Units, SUM(total_cost) AS Total_Cost FROM usage_data;

-- Average usage
SELECT AVG(units_consumed) AS Average_Units FROM usage_data;

-- Highest usage month
SELECT month_name, units_consumed FROM usage_data ORDER BY units_consumed DESC LIMIT 1;

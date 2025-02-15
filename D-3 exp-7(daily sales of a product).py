import numpy as np

# Assuming the daily_sales array is as follows:
daily_sales = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600])

# Calculate the variance of the daily sales
variance = np.var(daily_sales)
print("Variance of daily sales:", variance)

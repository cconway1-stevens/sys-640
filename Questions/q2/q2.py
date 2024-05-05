from scipy.optimize import linprog

# Costs matrix
costs = [4, 2, 3, 3, 2, 1]

# Coefficients for the constraints
A_eq = [
    [1, 1, 1, 0, 0, 0],  # Factory A supply
    [0, 0, 0, 1, 1, 1],  # Factory B supply
    [1, 0, 0, 1, 0, 0],  # Warehouse 1 demand
    [0, 1, 0, 0, 1, 0],  # Warehouse 2 demand
    [0, 0, 1, 0, 0, 1]   # Warehouse 3 demand
]

# Supply and demand
b_eq_a = [18, 22, 10, 20, 10]  # Part (a) supply and demand
b_eq_b = [18, 22, 14, 24, 14]  # Part (b) updated demand

# Bounds for each variable, all shipments must be non-negative
x_bounds = [(0, None)] * 6  # None implies no upper bound

# Solving part (a)
result_a = linprog(c=costs, A_eq=A_eq, b_eq=b_eq_a, bounds=x_bounds, method='highs')

# Solving part (b)
result_b = linprog(c=costs, A_eq=A_eq, b_eq=b_eq_b, bounds=x_bounds, method='highs')

result_a, result_b

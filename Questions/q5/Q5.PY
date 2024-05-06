
from scipy.optimize import linprog

# Define the costs matrix
costs = [
    6, 4, 8, 9,  # Lincoln to each market
    9, 3, 5, 6,  # Des Moines to each market
    9, 11, 6, 14, # Pierre to each market
    6, 5, 7, 9   # Omaha to each market
]

# Inequality constraints for supply
A_supply = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Lincoln
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Des Moines
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # Pierre
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]   # Omaha
]
b_supply = [750, 750, 500, 500]

# Equality constraints for demand
A_demand = [
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # Denver
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  # Kansas City
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # Minneapolis
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]   # St Louis
]
b_demand = [400, 700, 400, 500]

# Non-negativity constraints for all decision variables
x_bounds = [(0, None) for _ in range(16)]

# Solve the linear programming problem
result = linprog(
    c=costs,
    A_ub=A_supply,
    b_ub=b_supply,
    A_eq=A_demand,
    b_eq=b_demand,
    bounds=x_bounds,
    method='highs'
)

if result.success:
    optimal_solution = result.x
    optimal_cost = result.fun
else:
    optimal_solution = None
    optimal_cost = None

# Display the optimal solution and cost
print(optimal_solution)
print()
print("$",optimal_cost)
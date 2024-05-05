from scipy.optimize import linprog

# Part (a)

# Define the costs matrix
costs_a = [
    [4, 2, 3],  # Plant A to Warehouses 1, 2, 3
    [3, 2, 1]   # Plant B to Warehouses 1, 2, 3
]

# Supply from plants

supply_a = [18, 22]

# Demand at warehouses

demand_a = [10, 20, 10]

# Set up the bounds for the amount each route can carry, all routes are initially set from 0 to None
bounds_a = [(0, None)] * (2 * 3)

# Supply constraints (negative values because they are inequalities in the <= form)
supply_constraints_a = [
    [1, 1, 1, 0, 0, 0],  # Total sent out by Plant A
    [0, 0, 0, 1, 1, 1]   # Total sent out by Plant B
]

# Demand constraints
demand_constraints_a = [
    [1, 0, 0, 1, 0, 0],  # Demand at Warehouse 1
    [0, 1, 0, 0, 1, 0],  # Demand at Warehouse 2
    [0, 0, 1, 0, 0, 1]   # Demand at Warehouse 3
]

# Coefficients for supply and demand constraints
supply_eq_a = supply_a
demand_eq_a = demand_a

# Flatten cost matrix for the linprog function
c_flatten_a = [item for sublist in costs_a for item in sublist]

# Combine all constraints
A_eq_a = supply_constraints_a + demand_constraints_a
b_eq_a = supply_eq_a + demand_eq_a

# Solve the linear programming problem for part (a)
result_a = linprog(c=c_flatten_a, A_eq=A_eq_a, b_eq=b_eq_a, bounds=bounds_a, method='highs')

# Part (b) - updated demands
demand_b = [d + 4 for d in demand_a]  # Each warehouse has an increased demand by 4 units
b_eq_b = supply_a + demand_b

# Solve the linear programming problem for part (b)
result_b = linprog(c=c_flatten_a, A_eq=A_eq_a, b_eq=b_eq_b, bounds=bounds_a, method='highs')


# # Return the results for both parts
# result_a, result_b


#Print the results

print("Part (a) - Optimal cost: ", result_a.fun)
print("Part (a) - Optimal solution: ", result_a.x)
print("Part (b) - Optimal cost: ", result_b.fun)
print("Part (b) - Optimal solution: ", result_b.x)


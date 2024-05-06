from scipy.optimize import linprog

def solve_transportation_problem(demands):
    # Cost matrix for transportation from factories to warehouses
    cost = [4, 2, 3,   # Costs from Plant A to Warehouses 1, 2, 3
            3, 2, 1]   # Costs from Plant B to Warehouses 1, 2, 3

    # Supply constraints for factories A and B
    A_eq = [
        [1, 1, 1, 0, 0, 0],  # Total units from Plant A
        [0, 0, 0, 1, 1, 1]   # Total units from Plant B
    ]

    # Right hand side values for factory constraints
    b_eq = [18, 22]  # Total production units available at Plant A and B

    # Demand constraints for each warehouse
    A_eq_demand = [
        [1, 0, 0, 1, 0, 0],  # Demand at Warehouse 1
        [0, 1, 0, 0, 1, 0],  # Demand at Warehouse 2
        [0, 0, 1, 0, 0, 1]   # Demand at Warehouse 3
    ]

    # Add demand constraints to the matrix
    A_eq.extend(A_eq_demand)
    b_eq.extend(demands)

    # Bounds for each variable to ensure non-negative solutions
    bounds = [(0, None) for _ in range(6)]

    # Solve the linear programming problem
    result = linprog(c=cost, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    # Return results
    return result

# Solve part (a)
result_a = solve_transportation_problem([10, 20, 10])

# Solve part (b) with increased demands
result_b = solve_transportation_problem([14, 24, 14])

# Print the results for both parts
if result_a.success:
    print("Part (a) solution (shipments from A to W1, W2, W3 and from B to W1, W2, W3):")
    print(result_a.x)
    print("Minimum cost for part (a): $", result_a.fun)
else:
    print("No feasible solution found for part (a).")

if result_b.success:
    print("\nPart (b) solution (shipments from A to W1, W2, W3 and from B to W1, W2, W3):")
    print(result_b.x)
    print("Minimum cost for part (b): $", result_b.fun)
else:
    print("No feasible solution found for part (b).")

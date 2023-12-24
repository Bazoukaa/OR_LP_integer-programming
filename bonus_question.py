# Google's OR solving library including tools for linear problems like Integer Programming, 
from ortools.linear_solver import pywraplp

# Create the solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Data from question
sizes = [33, 30, 26, 24, 19, 18, 17]  # The size for each box
demand = [400, 300, 500, 700, 200, 400, 200]  # The demand for each box
fixed_cost = 1000
num_boxes = len(sizes)
M = sum(demand)  # A large number for the big-M method

# Decision variables
x = {}  # x[i,j] is the amount of box i's demand that is satisfied by box j
y = [solver.BoolVar(f'y[{i}]') for i in range(num_boxes)]  # y[i] is 1 if box i is produced, 0 otherwise

# Continuous non-negative variables for load transfer
for i in range(num_boxes):
    for j in range(i, num_boxes):
        x[i, j] = solver.IntVar(0, solver.infinity(), f'x[{i},{j}]')

# Objective: Minimize the total cost (variable cost + fixed cost)
objective_terms = []
for j in range(num_boxes):
    variable_cost = sum(sizes[i] * x[i, j] for i in range(j + 1))
    fixed_cost_term = fixed_cost * y[j]
    objective_terms.append(variable_cost + fixed_cost_term)

solver.Minimize(solver.Sum(objective_terms))

# Demand fulfillment constraints
for i in range(num_boxes):
    solver.Add(solver.Sum([x[k, i] for k in range(i + 1)]) >= demand[i])

# Fixed cost constraints using big-M method
for i in range(num_boxes):
    solver.Add(M * y[i] >= solver.Sum([x[i, j] for j in range(i, num_boxes)]))

# Solve the problem
status = solver.Solve()

# Output the results
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    for i in range(num_boxes):
        print(f'y[{i+1}] =', y[i].solution_value())
        for j in range(i, num_boxes):
            print(f'x[{i+1},{j+1}] =', x[i, j].solution_value())
else:
    print('The problem does not have an optimal solution.')
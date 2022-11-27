from scipy.optimize import linprog
objective = [-3, -4]

lhs_ineq = [[1, 1]]
rhs_ineq = [[4]] 

lhs_eq = [[0,0]]
rhs_eq= [0]

bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c=objective, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="simplex")

print(opt)
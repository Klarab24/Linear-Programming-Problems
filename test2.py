from scipy.optimize import linprog

obj = [-7, -10]

lhs_ineq = [[2, 3], [2, 1]]
rhs_ineq = [120, 80]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="simplex")

print(opt)

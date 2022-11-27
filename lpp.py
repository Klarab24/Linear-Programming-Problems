from scipy.optimize import linprog as lpp
import math
import matplotlib.pyplot as plt
import numpy as np

#########################################################################
obj = []
max_min = "n"
# Objective function
def obj_fun(obj):
    print("Objective function: ")
    obj_x = float(input("Enter the coefficient of x: "))
    obj_y = float(input("Enter the coefficient of y: "))
    global max_min
    max_min = input("Maximize or Minimize? (M/m): ")
    if max_min == "M":
        obj = [-obj_x, -obj_y]
        return obj
    elif max_min == "m":
        obj = [obj_x, obj_y]
        return obj
    else:
        print("Invalid input. Try again.")
        obj_fun(obj)

obj = obj_fun(obj)

##########################################################################
lhs_ineq = []
rhs_ineq = []
lhs_eq = []
rhs_eq = []
# Constraints
def constraints(lhs_ineq, rhs_ineq, lhs_eq, rhs_eq):
    print("Constraints: ")
    print("How many constraints do you want to add? ")
    num_constraints = int(input("Enter the number of constraints: "))
    for i in range(num_constraints):
        ineq = int(input("Enter 1 for <=, 2 for >=, 3 for =: "))
        print("Constraint", i+1)
        print("Enter the coefficients of the variables in the constraint: ")
        if ineq == 1:
            lhs_ineq.append([float(input("x: ")), float(input("y: "))])
            rhs_ineq.append(float(input("rhs: ")))
        elif ineq == 2:
            lhs_ineq.append([-float(input("x: ")), -float(input("y: "))])
            rhs_ineq.append(-float(input("rhs: ")))
        elif ineq == 3:
            lhs_eq.append([float(input("x: ")), float(input("y: "))])
            rhs_eq.append(float(input("rhs: ")))
        else:
            print("Invalid input. Try again.")
            constraints(lhs_ineq, rhs_ineq, lhs_eq, rhs_eq)

constraints(lhs_ineq, rhs_ineq, lhs_eq, rhs_eq)
if len(lhs_eq) == 0:
    lhs_eq = [[0,0]]
    rhs_eq = [[0]]

############################################################################
bnd = []
# Bounds
def bounds(bnd):
    print("Bounds:")
    #get lower and upper bounds allow the user to enter -inf and inf
    lower_bound = input("Enter the lower bound for x(-inf for infinity): ")
    if lower_bound == "-inf":
        lower_bound = -math.inf
    else:
        lower_bound = float(lower_bound)
    upper_bound = input("Enter the upper bound for x(inf for infinity): ")
    if upper_bound == "inf":
        upper_bound = math.inf
    else:
        upper_bound = float(upper_bound)
    bnd.append((lower_bound, upper_bound))
    lower_bound = input("Enter the lower bound for y(-inf for infinity): ")
    if lower_bound == "-inf":
        lower_bound = -math.inf
    else:
        lower_bound = float(lower_bound)
    upper_bound = input("Enter the upper bound for y(inf for infinity): ")
    if upper_bound == "inf":
        upper_bound = math.inf
    else:
        upper_bound = float(upper_bound)
    bnd.append((lower_bound, upper_bound))

bounds(bnd)

############################################################################
# Solve the problem
res = lpp(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method='highs')

############################################################################

if max_min == "M":
    print("Maximize: ", -res.fun)
    print("x: ", res.x[0])
    print("y: ", res.x[1])
elif max_min == "m":
    print("Minimize: ", res.fun)
    print("x: ", res.x[0])
    print("y: ", res.x[1])

def output(res):
    if res.success == True:
        #plot the constraints
        x1 = np.linspace(-10, 10, 100)
        x2 = np.linspace(-10, 10, 100)
        x1, x2 = np.meshgrid(x1, x2)
        for i in lhs_ineq:
            plt.contour(x1, x2, i[0]*x1 + i[1]*x2, [rhs_ineq[lhs_ineq.index(i)]], colors='r', linestyles='dashed')
        for i in lhs_eq:
            plt.contour(x1, x2, i[0]*x1 + i[1]*x2, [rhs_eq[lhs_eq.index(i)]], colors='r', linestyles='solid')
        #plot res.fun and res.x
        plt.plot(res.x[0], res.x[1], 'ro')
        if max_min == "M":
            plt.text(res.x[0], res.x[1], "Maximize: " + str(-res.fun) + " x: " + str(res.x[0]) + " y: " + str(res.x[1]))
        elif max_min == "m":
            plt.text(res.x[0], res.x[1], "Minimize: " + str(res.fun) + " x: " + str(res.x[0]) + " y: " + str(res.x[1]))
        plt.show()
        #save the plot

    else:
        print("The problem is infeasible.")

output(res)
############################################################################
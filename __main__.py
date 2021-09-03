# from scipy.optimize import linprog	
# import time
# start = time.time()
# c = [0.9, 1.7, 2.9, 2.8, 0.8,
#      1.3, 2.1, 2.7, 1.6, 2.9,
#      2.0, 3.0, 2.5, 0.7, 2.6,
#      1.1, 1.9, 3.0, 0.6, 0.2,]
# A_ub = [[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]] 
# b_ub = [200, 300, 200, 200] 
# b_eq = [100, 200, 150, 100, 300] 
# A_eq = [[0.9, 1.3, 2.0, 1.1],
#         [1.7, 2.1, 3.0, 1.9],
#         [2.9, 2.7, 2.4, 3.0],
#         [2.8, 1.6, 0.7, 0.6],
#         [0.8, 2.9, 2.6, 0.2]]
# print(linprog(c, A_ub, b_ub, A_eq, b_eq))
# stop = time.time()
# print ("Время :")
# print(stop - start)

from pulp import LpVariable, LpProblem, LpMaximize
import time
start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5", lowBound=0)
x6 = LpVariable("x6", lowBound=0)
x7 = LpVariable("x7", lowBound=0)
x8 = LpVariable("x8", lowBound=0)
x9 = LpVariable("x9", lowBound=0)
x10 = LpVariable("x10", lowBound=0)
x11 = LpVariable("x11", lowBound=0)
x12 = LpVariable("x12", lowBound=0)
x13 = LpVariable("x13", lowBound=0)
x14 = LpVariable("x14", lowBound=0)
x15 = LpVariable("x15", lowBound=0)
x16 = LpVariable("x16", lowBound=0)
x17 = LpVariable("x17", lowBound=0)
x18 = LpVariable("x18", lowBound=0)
x19 = LpVariable("x19", lowBound=0)
x20 = LpVariable("x20", lowBound=0)
problem = LpProblem('0',LpMaximize)
problem += (-0.9*x1 -1.7*x2 - 2.9* x3 - 2.8*x4 - 0.8*x5
             -1.3* x6-2.1*x7- 2.7*x8-1.6* x9 -2.9*x10 
             - 2.0*x11 - 3.0*x12 -2.4*x13 - 0.7*x14 -2.6*x15
             -1.1*x16 - 1.9*x17 - 3.0*x18 - 0.6*x19 - 0.2*x20), "Функция цели"
problem +=x1 + x2 +x3 + x4 + x5<= 200,"1" 
problem +=x6 +x7 +x8 +x9 +x10<= 300, "2"
problem +=x11 + x12+ x13 +x14 +x15 <= 200, "3"
problem +=x16 + x17+ x18 +x19 +x20 <= 36, "4"
problem +=x1+ x6+ x11 + x16 == 100, "5"
problem +=x2+x7+ x12 +x17 == 200, "6"
problem +=x3 + x8+x13 + x18 == 150, "7"  
problem +=x4 + x9+x14 + x19 == 100, "8"
problem +=x5 + x10+x15+x20 == 300, "9"                     
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Стоимость доставки:")
print (abs(problem.objective.value()))
stop = time.time()
print ("Время :")
print(stop - start)
import numpy as np
from numpy import linalg as LA
from sympy import *
import time
import random


def Gradient_Descent():
    learning_rate = 0.02
    J_values = []

#      Creating matrix A
    sizeA = int(input("Please enter size of Matrix A:"))

#      User input for matrix A
    print("Enter {} entries for matrix A in a single line (separated by space): ".format(sizeA*sizeA))
    entries = list(map(int, input().split()))

#    Insert values to Matrix A
    A = np.matrix(entries).reshape(sizeA, sizeA)
    print(np.all(np.linalg.eigvals(A)))
    if not np.all(np.linalg.eigvals(A)) > 0:
        raise Exception("Input is not valid")


#          Creating vector b
    print("Enter {} entries for vector b in a single line (separated by space): ".format(sizeA))
    entries = list(map(int, input().split()))

# Insert values to Matrix A
    b = np.matrix(entries).reshape(sizeA)

#            Creating scalar value c
    c = int(input("Enter value for c: "))



#            Create list of variables
    x = np.matrix(symbols('x0:%d' %sizeA)).reshape(sizeA)
    G = c + b * x.transpose() + x * A * x.transpose()



#       Choosing Initial values
    next = [0] * np.size(x)
    choose = input("Would you like to choose manual Initial Values or auto-generated?: 0: Manually 1: Auto-Generated ")
    repeat = int(input("How many times do you want run it? "))
    if repeat == 0:
        raise Exception("You have to run it atleast once")

    while(repeat!=0):  # For the batch Mode

    #Choosing Initial values
        J=G[0,0]
        if int(choose) == 0:
            for i in range(np.size(x)):
                next[i] = int(input("Choose Initial value number {}: ".format(i+1)))
        elif int(choose) == 1:
            for i in range(np.size(x)):
                next[i] = random.randint(1, 51)



        time_start = time.time()
        print("Initial value: {}".format(next))
        for iter in range(1000):
            previous = next.copy()
            for i in range(np.size(x)):  #differentiating for appropriate x
                J = diff(J,x[0,i])

                for j in range(np.size(x)):
                    J = J.subs(x[0,j], next[j])

                next[i] = next[i] - J * learning_rate
                J=G[0,0]

            if time.time() - time_start > 1.5 or LA.norm(np.subtract(next,previous), 1) < 10e-6: # Checking conditions - Running time and norm of (x1-x0)
                break

        for j in range(np.size(x)):
            J = J.subs(x[0,j], next[j])

        J_values.append(J)
        print("Iterations: {}".format(iter))
        print("x* = {}".format(next))
        print("J(x) = {}".format(J))
        print("********************************************\n")
        repeat = repeat - 1


    J_temp = np.array(J_values, dtype=np.float64)
    print("Mean Value = {}".format(np.mean(J_temp)))
    print("Standard Deviation = {}".format(np.std(J_temp)))


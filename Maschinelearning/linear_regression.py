import numpy as np

class LinearRegression:
  
   def fit( x, y, a0, a1, counter):
        N = len(x)
        y_predition = []
        
        for numbers in x:
            y_predition.append(a0 + (a1 * numbers))

        errors = []
        for numbers in range(len(y_predition)):
            errors.append(y_predition[numbers] - y[numbers])

        
        sq_errors = []
        for numbers in range(len(y_predition)):
            sq_errors.append(errors[numbers] ** 2)
        
        sq_errorshowl = 0.0
        for numbers in range(len(y_predition)):
            sq_errorshowl = sq_errorshowl + sq_errors[numbers]
        
        MSE = sq_errorshowl * 1/N
        if counter > 7:
            print(MSE)
            return
        sum_errors0 = 0
        for numbers in range(len(y_predition)):
            sum_errors0 = sum_errors0 + errors[numbers]
        gradiant_a0 = sum_errors0 * 2/N
        sum_errors1 = 0
        for numbers in range(len(y_predition)):
            sum_errors1 = sum_errors1 + (errors[numbers] * x[numbers])
        gradiant_a1 = sum_errors1 * 2/N
        print(a0 , a1)
        print(MSE)
        a0_new = round(a0 - (0.01 * gradiant_a0), 6)
        a1_new = round(a1 - (0.01 * gradiant_a1), 6)
        counter = counter+1
        LinearRegression.fit(x, y, a0_new, a1_new, counter)

LinearRegression.fit([1, 2, 3, 4], [2, 4, 5, 4], 0.0, 0.0, 0)

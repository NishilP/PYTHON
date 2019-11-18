# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:56:53 2019

@author: pnish
"""

print ('\n Welcome to the Quadratic Root calculator! \n')
a = eval(input("Enter the coeff. of (x^2): \n"))
b = eval(input("Enter the coeff. of (x): \n"))
c = eval(input("Enter the constant term: \n"))

d = (((b**2)-(4*a*c))**0.5)

if a == 0:
    print ('Invalid Input!')
    print ('This function is not Quadratic.')
elif (type (d) == complex):
    print ('\n This function has imaginery roots.')
else:
    ans1 = (-b + d)/(2*a)
    ans2 = (-b - d)/(2*a)
    print ()
    print ("The roots are: ", ans1, ",", ans2)

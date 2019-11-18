# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:25:38 2019

@author: pnish
"""

#A calculator:
def fact(x):
    if x > 1:
        return x * fact(x - 1)
    else:
        return 1

while(True):
    #check which operation is to be executed
    print ()
    print ("Operations offered:")
    o = input("Press 'A' for Addition. \n Press 'S' for Subtraction. \n Press 'M' for Multiplication. \n Press 'D' for Division. \n Press 'P' for %age. \n Press 'E' for Exponential Power. \n Press 'F' for ! . \n \n")
    ans = 0
    a = 0
    b = 0
    #the operations:
    if(o[0] == 'F'):
        c = eval(input("Enter a number: \n"))
        ans = fact(c)
        print (ans)
    else:
        a = eval(input("Enter the first number: \n"))
        b = eval(input("Enter the second number: \n"))
        if(o[0] == 'A'):
            ans = (a + b)
        elif o[0] == 'S':
            ans = (a - b)
        elif o[0] == 'M':
            ans = (a * b)
        elif o[0] == 'D':
            ans = (a / b)
        elif o[0] == 'P':
            ans = ((a / b) * 100)
        elif o[0] == 'E':
            ans = (a ** b)
        else:
            print ("Invalid Operation!")
    print ()
    print ("Answer:", ans)
    print ()
    print ("Do you wish to continue using the calculator?")
    print ()
    z = input("Press 'Y' for Yes. \n Press 'N' for No. \n")
    if(z == 'N'):
        break

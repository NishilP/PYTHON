# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:43:38 2019

@author: pnish
"""

"""
This code calculates the price of European 'Options' using the Black-Scholes
model. It gives the price of both a 'call' and a 'put' option.
"""
import math
from scipy.stats import norm

print ()
print ("Welcome to the 'Option' Price calculator! \n")
S = eval(input("Enter the 'current' spot price: \n"))
X = eval(input("Enter the 'strike' price: \n"))
T = (eval(input("Enter the 'time to maturity' (in days): \n")))/365
R = eval(input("Enter the relevant interest rate (as a decimal): \n"))
SD = eval(input("Enter the standard deviation (as a decimal): \n"))

d1 = ((math.log(S/X)) + ((R + ((SD**2)/2))*T))/(SD*(T**0.5))
d2 = d1 - (SD*(T**0.5))
Nd1 = norm.cdf(d1)
Nd2 = norm.cdf(d2)

call_price = (S*Nd1) - (X*((math.e)**(-R*T))*Nd2)
put_price = call_price + (X*((math.e)**(-R*T))) - S

print ()
print ("Price of Call: ", call_price)
print ()
print ("Price of Put: ", put_price)

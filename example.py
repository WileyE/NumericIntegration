from mathfunc import *

#create a mathfunc object
func = mathfunc('x**2*cos(x)')

#evaluating the function at a value
print(func.evaluate(1))


#integrating on a given interval using each of the 3 methods
#must provide: start of integration, end of integration, number of points in the discretization

#test print
print(func)

#Midpoint Rule
print(f'The result of the integral using the Midpoint Rule is: {func.midpoint_rule(0,1,10)}')

#Trapezoid Rule
print(f'The result of the integral using the Trapezoid Rule is: {func.trapezoidal_rule(0,1,10)}')

#Simpson's Rule
#must use an odd number of points in the discretization
print(f'The result of the integral using Simpson\'s rule is: {func.simpsons_rule(0,1,11)}')


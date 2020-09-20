import parser
from math import *
import numpy as np

class mathfunc:
    
    '''
    Create a mathfunc object by inputting a function of x in pythonic notation
    
    examples:
    
        2*x**2*sin(x)
        
        x**3+3*x**2+5
        
        3*pi*log(x)
    
    '''
    
    def __init__(self, equation):
        try:
            parser.expr(equation).compile()
        except:
            raise Exception('The mathematical expression could not be parsed')
            
        self.equation = equation

    def __str__(self):
        return self.equation

    def evaluate(self, value):
        
        '''
        Evaluates the mathfunc object at a given value
        
        returns float
        
        '''
        x = value
        formula = parser.expr(self.equation).compile() 
        return float(eval(formula))
    
    def midpoint_rule(self,a,b,num_points):
        
        '''
        Evaluates the integral of the mathfunc object using the midpoint method
        
        Integration start point: a
        
        Integration end point: b 
        
        Number of evenly spaced points from a to b: num_points
        
        returns float
        
        '''

        x_grid = np.linspace(a,b,num_points)
        midpoint = (x_grid[1]-x_grid[0])/2
        delta_x = x_grid[1]-x_grid[0]
        area = 0
        
        for i in range(0,len(x_grid)-1):
            area += (self.evaluate(x_grid[i]+midpoint))*delta_x

        return float(area)
    
    
    def trapezoidal_rule(self,a,b,num_points):
        
        '''
        Evaluates the integral of the mathfunc object using the trapezoid method
        
        Integration start point: a
        
        Integration end point: b 
        
        Number of evenly spaced points from a to b: num_points
        
        returns float
        
        '''
        x_grid = np.linspace(a,b,num_points)
        delta_x = x_grid[1]-x_grid[0]
        area = 0

        for i in range(0,len(x_grid)-1):
            area += (1/2)*(self.evaluate(x_grid[i])+self.evaluate(x_grid[i+1]))*delta_x
            
        return float(area)
    
    
    def simpsons_rule(self,a,b,num_points):
        
        '''
        Evaluates the integral of the mathfunc object using Simpson's method
        
        Integration start point: a
        
        Integration end point: b 
        
        Number of evenly spaced points from a to b: num_points
        
        num_points must be odd for simpsons rule
        
        returns float
        
        '''
        
        if num_points % 2 == 0:
            raise Exception('The number of points in the grid must be odd for Simpson\'s method')
        else:
            x_grid = np.linspace(a,b,num_points)
            
        delta_x = x_grid[1]-x_grid[0]
        area = delta_x*(self.evaluate(a)+self.evaluate(b))/3

        for i in range(1,len(x_grid)-1):
            if i % 2 == 1:
                area += 4*delta_x*self.evaluate(x_grid[i])/3
            elif i % 2 == 0:
                area += 2*delta_x*self.evaluate(x_grid[i])/3
                
        return float(area)
    
    
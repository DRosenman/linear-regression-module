import numpy as np
import matplotlib.pyplot as plt

def slope(x,y,through_origin = False):
    x = np.array(x)
    y = np.array(y)
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return ((x-x.mean())*y).sum()/((x-x.mean())**2).sum()
    else:
        return ((x*y).sum())/(x**2).sum()
    
def intercept(x,y,through_origin = False):
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return y.mean() - slope(x,y)*x.mean()
    else:
        return 0.0

def slope_error(x,y,through_origin = False):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    if through_origin == False:
        residuals_squared = (y - slope(x,y)*x - intercept(x,y))**2
        residuals_squared_sum = residuals_squared.sum()
        D = ((x-x.mean())**2).sum()
        return np.sqrt((1/(n-2))*residuals_squared_sum/D)
    else:
        residuals_squared = (y - slope(x,y,True)*x)**2
        return np.sqrt(residuals_squared.sum()/((n-1)*(x**2).sum()))
    
def intercept_error(x,y,through_origin = False):
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        n = len(x)
        D = ((x-x.mean())**2).sum()
        residuals_squared = (y - slope(x,y)*x - intercept(x,y))**2
        return np.sqrt(((1/n) + (x.mean()**2)/D)*residuals_squared.sum()/(n-2))

def plot_graph(x,y, through_origin = False):
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o', label='original data')
    if through_origin == False:
        plt.plot(x, intercept(x,y) + slope(x,y)*x, 'r', label='fitted curve')
    else:
        plt.plot(x,slope(x,y,True)*x, 'r', label = 'fitted line')
def plot_y_over_x(x,y):
    x = np.array(x)
    y = np.array(y) 
    plt.plot(x[x!=0],y[x!=0]/x[x!=0],'o',label = 'original data')
    plt.hlines(slope(x,y,True), x.min(), x.max(), colors='k', linestyles='solid', label = 'best fit line')
    
        
        
        
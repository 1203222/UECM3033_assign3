import numpy as np
from scipy import integrate
import pylab as p

def ode(y, t, a, b):
    y0, y1 = y
    dydt = [a * (y0 - y0*y1), b * (-y1 + y0*y1)] # differential equations
    return dydt
    
if __name__ == "__main__":
    a = 1.0
    b = 0.2
    Y0 = [0.1, 1.0] # initial conditions of y0 and y1
    t = np.linspace(0, 5, 50) # time
    ans = integrate.odeint(ode, Y0, t, args=(a,b))
    
    p.plot(t, ans[:, 0], 'b', label='y0')
    p.plot(t, ans[:, 1], 'g', label='y1')
    p.legend(loc='best')
    p.xlabel('t')
    p.ylabel('y')
    p.grid()
    p.title('Graph of y0 and y1 against t with y0 = 0.1')
    p.show()
    
    y0 = ans[:, 0]  
    p.plot(y0, ans[:, 1], 'r')
    p.xlabel('y0')
    p.ylabel('y1')
    p.grid()
    p.title('Graph of y1 against y0 with y0 = 0.1')
    p.show()
    
    Y1 = [0.11, 1.0]
    sol = integrate.odeint(ode, Y1, t, args=(a,b))
    
    p.plot(t, sol[:, 0], 'b', label='y0')
    p.plot(t, sol[:, 1], 'g', label='y1')
    p.legend(loc='best')
    p.xlabel('t')
    p.ylabel('y')
    p.grid()
    p.title('Graph of y0 and y1 against t with y0 = 0.11')
    p.show()
    
    y0 = sol[:, 0]  
    p.plot(y0, sol[:, 1], 'r')
    p.xlabel('y0')
    p.ylabel('y1')
    p.grid()
    p.title('Graph of y1 against y0 with y0 = 0.11')
    p.show()


#To show from limit 0 to infinity sin(x)/x dx =pi/2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.sin(x)/x
x=np.arange(1.0e-5,100,0.1)
plt.plot(x,f(x))
plt.grid(True)
plt.show()
s=0.0

for i in range(10):
    term=quad(f,1.0e-5+i*np.pi,(i+1)*np.pi)[0]
    s=s+term

print(s)
print((np.pi)/2)

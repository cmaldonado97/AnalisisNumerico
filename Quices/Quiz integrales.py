import numpy as np
from scipy import integrate
import math

# Define function and interval
a = 1.
b =  2.
f = lambda x: x*math.e

# Cuadratura de Gauss
deg = 6
x, w = np.polynomial.legendre.leggauss(deg)
gauss = sum(w * f(x))

# Comparando
quad, quad_err = integrate.quad(f, a, b)

print 'Solución y error'.format(quad, quad_err)
print 'Solución por gauss'.format(gauss)
print 'Diferencia: ', abs(gauss - quad)
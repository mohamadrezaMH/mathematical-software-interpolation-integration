import numpy as np
from scipy.integrate import simpson
from scipy.integrate import fixed_quad

f = lambda x: np.exp(x**2)

# ----------------
# Trapezoidal
# ----------------
x = np.linspace(0,1,1000)
y = f(x)

trap_result = np.trapz(y,x)

# ----------------
# Simpson
# ----------------
simpson_result = simpson(y,x)

# ----------------
# Gaussian
# ----------------
gauss_result, _ = fixed_quad(f,0,1,n=5)

print("Trapezoidal =", trap_result)
print("Simpson =", simpson_result)
print("Gaussian =", gauss_result)
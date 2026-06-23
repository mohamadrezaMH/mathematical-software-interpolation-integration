import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
import sympy as sp

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 3, 5, 8, 5, 2])

# ------------------------
# Lagrange Interpolation
# ------------------------
lagrange_poly = lagrange(x, y)

X = sp.Symbol('x')
poly_expr = sum(
    lagrange_poly.coef[i] * X**(len(lagrange_poly.coef)-i-1)
    for i in range(len(lagrange_poly.coef))
)

poly_expr = sp.expand(poly_expr)

print("Lagrange Polynomial:")
print(poly_expr)

# ------------------------
# Cubic Spline
# ------------------------
spline = CubicSpline(x, y)

print("\nCubic Spline Piecewise Equations:\n")

for i in range(len(spline.c.T)):
    a, b, c, d = spline.c[:, i]

    print(f"Interval [{x[i]}, {x[i+1]}]")

    print(
        f"S{i}(x) = "
        f"{a:.6f}(x-{x[i]})^3 + "
        f"{b:.6f}(x-{x[i]})^2 + "
        f"{c:.6f}(x-{x[i]}) + "
        f"{d:.6f}"
    )

    print()

x_new = np.linspace(1, 6, 500)

plt.figure(figsize=(10,6))

plt.plot(x, y, 'ro', label='Original Points')
plt.plot(x_new, lagrange_poly(x_new),
         label='Lagrange Interpolation')

plt.plot(x_new, spline(x_new),
         label='Cubic Spline Interpolation')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange vs Cubic Spline')
plt.legend()
plt.grid(True)

plt.savefig("interpolation.png", dpi=300)
plt.show()
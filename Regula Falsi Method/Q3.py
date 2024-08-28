import math

def f(x):
    return math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6

def regula_falsi(xl, xu, tol=1e-4, max_iter=100):
    fl = f(xl)
    fu = f(xu)

    if fl * fu > 0:
        raise ValueError("Function has the same signs at the endpoints.")

    for iteration in range(max_iter):
        # Compute the false position
        xr = xu - (fu * (xl - xu)) / (fl - fu)
        fr = f(xr)

        # Check if the result is within the desired tolerance
        if abs(fr) < tol or abs(xu - xl) < tol:
            return xr

        # Update intervals
        if fl * fr < 0:
            xu = xr
            fu = fr
        else:
            xl = xr
            fl = fr
    raise RuntimeError("Maximum number of iterations reached.")

xl = 1.0
xu = 2.0

root = regula_falsi(xl, xu)
print(f"The root of the equation is approximately {root:.4f}")

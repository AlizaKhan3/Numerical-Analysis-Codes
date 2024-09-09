def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

def newton_raphson(initial_guess, tol=1e-5, max_iter=100):
    x = initial_guess
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return round(x_new, 4)
        x = x_new
    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")

# Initial guess
initial_guess = 1.5

# Find the root
root = newton_raphson(initial_guess)
print(f"The root of the equation x^3 - x - 1 = 0, correct to 4 decimal places, is: {root}")

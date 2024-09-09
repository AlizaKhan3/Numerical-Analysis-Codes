import math

def f(x):
    return math.log(x - 1) + math.cos(x - 1)

def df(x):
    return 1 / (x - 1) - math.sin(x - 1)

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

# Initial guesses
initial_guesses = [1.2, 2]

# Find and print the root for each initial guess
for guess in initial_guesses:
    try:
        root = newton_raphson(guess)
        print(f"The root of the equation ln(x - 1) + cos(x - 1) = 0, starting from initial guess {guess}, correct to 4 decimal places, is: {root}")
    except ValueError as e:
        print(f"Error with initial guess {guess}: {e}")

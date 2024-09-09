import math

def f(x):
    return x - 0.8 - 0.2 * math.sin(x)

def df(x):
    return 1 - 0.2 * math.cos(x)

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

initial_guesses = [0, 1.57]

for guess in initial_guesses:
    try:
        root = newton_raphson(guess)
        print(f"The root of the equation x - 0.8 - 0.2sin(x) = 0, starting from initial guess {guess}, correct to 4 decimal places, is: {root}")
    except ValueError as e:
        print(f"Error with initial guess is {guess}: {e}")

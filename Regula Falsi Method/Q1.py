import math

def f(x):
    return 2 * x * math.cos(2 * x) - (x - 2)**2

# Initial root values
a = 2
b = 3

# Regula Falsi method parameters
max_iterations = 3
iteration = 0
c = a  # Initial c

results = []  # To store iteration results

while iteration < max_iterations:
    # Calculate the point of intersection (c) using Regula Falsi formula
    c = b - (f(b) * (b - a)) / (f(b) - f(a))

    # Store the result for this iteration
    results.append((iteration + 1, c, f(c)))
    
    # Update the interval based on the sign of f(c)
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    iteration += 1

print(results)
import math

def f(x):
    return x * math.log10(x) - 1.2

# Initial root values
a = 2
b = 3

# Regula Falsi method parameters
tolerance = 1e-6
max_iterations = 6
iteration = 0
c = a 

# Regula Falsi iterations
while iteration < max_iterations:
    # Calculate the point of intersection (c) using the Regula Falsi formula
    c = b - (f(b) * (b - a)) / (f(b) - f(a))
    
    # Check if the absolute value of f(c) is within the tolerance
    if abs(f(c)) < tolerance:
        break
    
    # Update the interval based on the sign of f(c)
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    iteration +=1

# Print the result 
print(f"Root: {c:.3f}, f(c): {f(c):.3f}, Iterations: {iteration}")

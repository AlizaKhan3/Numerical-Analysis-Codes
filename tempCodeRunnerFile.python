import math

a = -1
b = 0
iteration = 1
max_iterations = 15

while iteration <= max_iterations:
    c = (a + b) / 2
    print("Iteration:", iteration, "x =", c)
    
    z = 2 * c * math.cos(2 * c) - (c + 1)**2
    print("f(x) =", z)
    
    if z == 0:
        print("The root is", c)
        print("Total iterations:", iteration)
        break
    
    if (2 * a * math.cos(2 * a) - (a + 1)**2) * z < 0:
        b = c
    else:
        a = c
    
    iteration += 1
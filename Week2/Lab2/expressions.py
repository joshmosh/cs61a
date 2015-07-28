# Print 3
3

# Print 5
2 + 3

# Print 0
-16 - -16

# Print 13
3 * 4 + 1

# Print 15
3 * (4 + 1)

# Print 8 (2 to the power of 3)
2 ** 3

# Print 7
x = 4
3 + x

# Print NameError
x + y

# Print 4
x, y = 1, 2
3 + x

# Print 3
x + y

from operator import mul, add

# Print 12
mul(3, 4)

# Print 15
mul(3, add(4, 1))

# Print 8
pow(2, 3)

# Print 64
pow(pow(2, 3), abs(-2))

def double(x):
    return x * x

def square(y):
    return y * y

def f(z):
    add(square(double(z)), 1)

# Print None - No return value
f(4)

def welcome():
    print("Welcome to")
    return "hello"

def cs61a():
    print("cs61a")
    return "world"

# Print
# Welcome to
# cs61a
# hello world
print(welcome(), cs61a())

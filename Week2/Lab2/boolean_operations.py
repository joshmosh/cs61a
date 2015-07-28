a, b = 10, 6

# Prints True
a != 0 and b > 5

# Prints False
a < b or not a

# Prints True
not not a

# Prints False
not (not a or not not b)

# Prints ZeroDivisionError
True and 1 / 0 and False

# Prints True
True or 1 / 0 or False

# Prints 0
True and 0

# Prints 1
False or 1

# Prints 15
1 and 3 and 6 and 10 and 15

# Prints 2
0 or False or 2 or 1 / 0

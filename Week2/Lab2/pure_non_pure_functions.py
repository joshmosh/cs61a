# Print 10
x = print(9 + 1)

# Print False
x == 10

# Print
# 2
# None
print(print(2))

def om(foo):
    return -foo

def nom(foo):
    print(foo)

# Prints
# 4
# None
nom(4)

# Prints 4
om(-4)

# Prints Error
brian = nom(4)
brian + 1

# Prints 5
michelle = om(-4)
michelle + 1

x = 6

def beep(x):
    print(x)

def boop(x):
    y = x
    x = 7
    print(x)

# Prints 6
y = beep(x)

# Prints 7
boop(x)

# Prints
# 8
# Error
y + beep(8)

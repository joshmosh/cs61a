# Prints
# 2
# 1
# 0
# -1
n = 3
while n >= 0:
    n = n - 1
    print(n)

# Prints
# 2
# 4
# 6
# 8
n, i = 7, 0
while i < n:
    i = i + 2
    print(i)

# Prints
# 3
# 2
# 1
# 0
# -1
# Continues forever
n = 4
while True:
    n = n - 1
    print(n)

# Prints
# 64
# 32
# 16
# 8
# 4
# 2
# 1
n = 2
def exp_decay(n):
    if n % 2 != 0:
        return

    while n > 0:
        print(n)
        n = n // 2

exp_decay(64)

# Prints Nothing
exp_decay(5)

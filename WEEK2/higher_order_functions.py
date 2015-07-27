def make_adder(n):
    """ Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> add_five = make_adder(5)
    >>> add_five(5)
    10
    """
    def adder(k):
        return k + n

    return adder

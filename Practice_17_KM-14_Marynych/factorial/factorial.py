def fact(n):
    if n == 1:  # The termination condition
        return 1  # The base case
    else:
        res = n * fact(n - 1)  # The recursive call
        return res



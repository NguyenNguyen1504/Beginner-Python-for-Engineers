def fibonacci_sequence(n):
    # Define variables here
    result = []
    # Do something here
    i = 0
    a = 0
    b = 1
    while i <= n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


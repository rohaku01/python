def fibonacci(n):
    sequence = [0, 1]
    if n <= 1:
        return n

    for i in range(2, n+1):
        p = sequence[i-1] + sequence[i-2]
        sequence.append(p)
    return sequence[n]


print(fibonacci(5))

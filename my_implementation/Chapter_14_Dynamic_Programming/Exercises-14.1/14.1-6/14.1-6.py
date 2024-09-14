def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def test():
    for n in range(2, 2000):
        assert fibonacci(n) == fibonacci(n - 1) + fibonacci(n - 2)
    print("Passed all tests!")
    
    
if __name__ == '__main__':
    test()
def fibonacci(n):
    a = 0
    b = 1

    print(a)

    while b <= n:
        print(b)
        
        a, b = b, a + b

fibonacci(50)
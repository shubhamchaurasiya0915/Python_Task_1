def fibonacci(n):
    fib_series = [0,1]  

    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]  
        fib_series.append(next_fib)  

    return fib_series


n = int(input("Entr the number: "))  
result = fibonacci(n)
print("Fibonacci Series up to", n, "terms:", result)

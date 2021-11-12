def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
        

def get_fibonacci_series(n):
    fibonacci_series = []
    for i in range(n):
        term = fibonacci(i)
        fibonacci_series.append(term)
    return fibonacci_series

n = int(input())
result = get_fibonacci_series(n)
print(result)

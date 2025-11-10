import timeit

# Iterative Fibonacci
def fibo(n):
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Recursive Fibonacci
def fibo_recursive(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

N, RUNS = 20, 1000
print(f"Given N = {N}\n{RUNS} runs\n")

def callFibo(isRec):
    if isRec:
        result = fibo_recursive(N)
        time_taken = timeit.timeit(lambda: fibo_recursive(N), number=RUNS)
        space = "O(n)"
        mode = "Recursive"
    else:
        result = fibo(N)
        time_taken = timeit.timeit(lambda: fibo(N), number=RUNS)
        space = "O(1)"
        mode = "Non-Recursive"
    
    print(f"{mode} Fibonacci = {result}\nTime: {time_taken:.6f} sec\tSpace: {space}\n")

callFibo(True)
callFibo(False)

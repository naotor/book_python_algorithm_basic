memo = {1: 1, 2: 1}
def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
        return memo[n]

N = 10
print(fibonacci(N))
print(memo)
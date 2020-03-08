import math

def get_prime(n):
    if n <= 1:
        return []

    prime = [2]
    limit = int(math.sqrt(n))
    data = list(range(3, n+1, 2))

    while data[0] < limit:
        prime.append(data[0])
        data = [i for i in data if i % data[0] != 0]

    return prime + data

N = 100000
print(get_prime(N))
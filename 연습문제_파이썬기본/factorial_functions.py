def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

def fact_iter(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n= int(input())
t= int(input())
print(f"{n}! (재귀) = {fact_rec(n)}")
print(f"{n}! (반복) = {fact_iter(n)}")
print(f"{t}! (재귀) = {fact_rec(t)}")
print(f"{t}! (반복) = {fact_iter(t)}")
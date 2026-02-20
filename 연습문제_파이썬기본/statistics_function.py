import statistics

def cal(n):
    mean_v = sum(n) / len(n)
    max_v = max(n)
    min_v = min(n)
    std_v = statistics.stdev(n)

    return mean_v, max_v, min_v, std_v

nums = list(map(int,input().split()))
x,y,z,s = cal(nums)

print(f"숫자들: {nums}")
print(f"평균: {x}")
print(f"최댓값: {y}")
print(f"최솟값: {z}")
print(f"표준편차: {round(s,2)}")
n,p = map(int,input().split())
dic = {}
sales = []
dp = [int(1e8)]*(n+1)
dp[0] = 0

for _ in range(p):
    num,price = map(int,input().split())

    if num not in dic.keys():
        dic[num] = price
        dp[num] = price
    elif num in dic.keys() and dic[num] > price:
        dic[num] = price
        dp[num] = price

for key in dic.keys():
    sales.append((key,dic[key]))

sales.sort()

for i in range(1,n+1):
    for cost in dic.keys():
        if cost > i:
            continue
        else:
            dp[i] = min(dp[i],dp[i-cost] + cost)

print(dp[n])
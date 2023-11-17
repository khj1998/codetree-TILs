n,p = map(int,input().split())
sales = []
dp = [int(1e8)]*(n*100+1)
ans = int(1e8)
dp[0] = 0

for _ in range(p):
    num,price = map(int,input().split())
    sales.append((num,price))

sales.sort()

for i in range(1,n*100+1):
    for num,price in sales:
        if num > i:
            continue
        else:
            dp[i] = min(dp[i],dp[i-num]+price)
        
for i in range(n,n*100+1):
    ans = min(ans,dp[i])

print(ans)
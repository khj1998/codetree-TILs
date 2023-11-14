N = int(input())
ans = 1
array = []

for _ in range(N):
    a,b = map(int,input().split())
    array.append((a,b))

array.sort(key = lambda x:-x[0])
now_speed = array[0][1]

for i in range(1,len(array)):
    if array[i][1] <= now_speed:
        ans+=1
        now_speed = array[i][1]

print(ans)
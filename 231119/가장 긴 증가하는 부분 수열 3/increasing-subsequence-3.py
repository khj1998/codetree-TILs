from bisect import bisect_left,bisect_right

n = int(input())
array = list(map(int,input().split()))
ans = [array[0]]

for i in range(1,len(array)):
    if array[i] > ans[-1]:
        ans.append(array[i])
    else:
        idx = bisect_left(ans,array[i])
        ans[idx] = array[i]

print(len(ans))
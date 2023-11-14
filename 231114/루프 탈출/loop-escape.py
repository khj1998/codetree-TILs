n = int(input())
loop_map = [[] for _ in range(n+1)]
answer = 0

def dfs(start): 
    check[start] = True

    for x in loop_map[start]:
        if not check[x]:
            return dfs(x)
        else:
            return False

    return True

for i in range(1,n+1):
    a = int(input())

    if a== 0:
        continue
    
    loop_map[i].append(a)

for i in range(1,n+1):
    check = [False]*(n+1)
    if dfs(i):
        answer += 1

print(answer)
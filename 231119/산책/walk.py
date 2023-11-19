from collections import defaultdict
from itertools import combinations

ans = 0
N = int(input())
dic = defaultdict(list)

for _ in range(N):
    name,types = map(str,input().split())
    
    if types not in dic:
        dic[types] = [name]
    else:
        dic[types].append(name)

type_list = list(dic.keys())

for i in range(1,len(type_list)+1):
    if i==1:
        for key in type_list:
            ans += len(dic[key])
    else:
        temp = 1
        combination = list(combinations(type_list,i))

        for comb in combination:
            for c in comb:
                temp*=len(dic[c])
        
        ans += temp

print(ans)
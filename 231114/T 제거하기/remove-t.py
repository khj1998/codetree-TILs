S = str(input())
T = str(input())
stack = []
T_len = len(T)
stack_len = 0

for c in S:
    stack.append(c)
    stack_len += 1

    while stack_len >= T_len and ''.join(stack[-T_len:]) == T:
        del stack[-T_len:]
        stack_len -= T_len

print(''.join(stack))
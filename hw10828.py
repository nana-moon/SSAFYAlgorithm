import sys
tc = int(sys.stdin.readline())
s = []
for _ in range(tc):
    n = sys.stdin.readline().split()
    if n[0] == 'push':
        s.append(n[1])
    elif n[0] == 'pop':
        print(stack.pop()) if len(s) else print(-1)
    elif n[0] == 'size':
        print(len(s))
    elif n[0] == 'empty':
        print(0) if len(s) else print(1)
    elif n[0] == 'top':
        print(s[-1]) if len(s) else print(-1)
            

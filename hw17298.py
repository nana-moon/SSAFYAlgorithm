import sys
input = sys.stdin.readline
n = int(input())
st = ist(map(int, input().split()))
target = []
result = [-1]*n

st.reverse()
idx = 0
target.append((idx, st.pop()))

while st:
    t = st.pop()
    idx += 1
    while target and target[-1][1] < t:
        a, b = target.pop()
        result[a] = t

    target.append((idx, t))
for i in result:
    print(i, end = '')




# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# for x in range(0,n):
#     if x == n-1:
#         print(-1)
#     for y in range(x+1,n):
#         if arr[y] > arr[x]:
#             print(arr[y], end =' ')
#             break
#         elif max(arr[x:]) == arr[x]:
#             print(-1, end =' ')
#             break
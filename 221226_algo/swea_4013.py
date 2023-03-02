# 특이한 자석
def dfs(level, direction):
    global arr
    front, back = False, False
    if level+1 <= 3:
        if arr[level][2] + arr[level+1][6] == 1:
        	back = True
	# if level-1 >= 0:
	# 	if arr[level][6] + arr[level-1][2] == 1:
	# 		front = True
	# 돌리는 작업
	# 재귀함수


T = int(input())
for t in range(1, T+1):
    
	K = int(input())
	arr = [list(map(int, input().split())) for _ in range(4)]
	rotate = [list(map(int, input().split())) for _ in range(K)]
	for k in range(K):
		wheel, direction = rotate[k]
		wheel -= 1
	
		while wheel <= 3:
			if wheel != 3:
				keep = arr[wheel][2] + arr[wheel+1][6]
			if direction == 1: # 시계 방향 회전
				tmp = arr[wheel].pop(-1)
				arr[wheel].insert(0,tmp)
			else: # 반시계 방향 회전
				tmp = arr[wheel].pop(0)
				arr[wheel].insert(7, tmp)
			print(arr)
			if wheel == 3: break
			if keep != 1:
				break
			else:
				wheel += 1
				direction = -1*direction
	sum = 0
	for i in range(4):
		if arr[i][0] == 1:
			sum += 2**i
	print(f'#{t} {sum}')
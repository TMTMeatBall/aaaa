C, R = map(int, input().split())
k = int(input())

arr = [[0] * C for _ in range(R)]
direction = x = y = 0

for i in range(1,C*R+1):
    if i == k:
        print(y+1,x+1)
        break
    else:
        arr[x][y] = i
        x = dx[dire]

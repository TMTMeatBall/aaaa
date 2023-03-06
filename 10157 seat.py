C, R = map(int, input().split())
k = int(input())
arr = [[0] * C for _ in range(R)]
if k > C * R:
    print(0)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = x = y = 0

for i in range(1, C * R + 1):
    if i == k:
        print(y + 1, x + 1)
        break
    else:
        arr[x][y] = i
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= R or y >= C or arr[x][y]:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction + 1) % 4

            x += dx[direction]
            y += dy[direction]

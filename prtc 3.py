dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv1 = 0
    maxv2 = 0
    for i in range(N):
        for j in range(N):
            cntc = arr[i][j]
            cntx = arr[i][j]
            tmp = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l

                    nnx = i + ddx[k] * l
                    nny = j + ddy[k] * l
                    if -1 < nx < N and -1 < ny < N:
                        cntc += arr[nx][ny]
                    if -1 < nnx < N and -1 < nny < N:
                        cntx += arr[nnx][nny]
            if maxv1 < cntc:
                maxv1 = cntc
            if maxv2 < cntx:
                maxv2 = cntx
    if maxv1 > maxv2:
        print(f'#{tc} {maxv1}')
    else:
        print(f'#{tc} {maxv2}')

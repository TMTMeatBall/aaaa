T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maxv = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] #cnt tmp 초기화 위치는 지정한 곳과 맞춰 주기
            tmp = arr[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    cnt += arr[nx][ny]
            if maxv < cnt:
                maxv = cnt
    print(f'#{tc} {maxv}')

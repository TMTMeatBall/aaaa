T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    minv = 10000
    for a in range(0, N - 2):
        for b in range(a + 1, N - 1):
            cnt = 0
            for i in range(0, a + 1):
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a + 1, b + 1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b + 1, N):
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            if minv > cnt:
                minv = cnt
    print(f'#{tc} {minv}')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            mul = arr[i][j]
            for k in range(4):

                for l in range(1, mul+1): #mul따로 설정 안하고 cnt
                    # 일괄처리하면 cnt가 변한 값이 l 에 반환되는 오류 발생함

                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    if 0 <= nx < N and 0 <= ny < M:
                        cnt += arr[nx][ny]

            if cnt > maxv:
                maxv = cnt
    print(f'#{tc} {maxv}')

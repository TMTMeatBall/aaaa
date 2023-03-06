T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    minv = 10000
    # 3개 영역을 만들기
    for a in range(N - 2):  # W 영역 맨 아래 0~N-3
        for b in range(a + 1, N - 1):  # B영역 a+1~N-2, W영역보다는 밑에 있도록 최소 한 줄 이상을 갖도록
            cnt = 0
            for i in range(0, a + 1):  # W영역 안에서
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a + 1, b + 1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b + 1, N): #w,b제외 나머지 최소 1줄을 R영역으로
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1
            if minv > cnt:
                minv = cnt

    print(f'#{tc} {minv}')
    # cnt = 0
    #
    # for i in range(N):
    #     for j in range(M):
    #         if arr[0][j] != 'W':
    #             arr[0][j] = 'W'
    #             cnt += 1
    #
    #         if arr[N-1][j] != 'R':
    #             arr[N-1][j] = 'R'
    #             cnt += 1
    # for k in range(1,N-1):
    #     a = []
    #     for j in range(M):
    #         if arr[k]

    # arr 0:i+1 i:j+1 j:N

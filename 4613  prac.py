T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    minc = 5000
    for a in range(0, N - 2): #3분할 하는 최소의 조건, 나머지 색이 최소 1줄 이상 가질 것
        for b in range(a + 1, N - 1): #세 번째 색이 1줄을 갖게 하고, 첫 색이 끝난 이후 모두를 두번째 색으로 하는 최소조건
            cnt = 0 #각 경우마다 cnt초기화 해야하므로 여기에 배치
            for i in range(0, a + 1): #0~a까지 w영역
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a + 1, b + 1): #a+1~b까지 B영역
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b + 1, N): #b+1~N인 끝까지 R영역
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1
                        #이런 식으로 여러 cnt 가 나오는데, 그 cnt가 최소가 되는 순간이 minc에 반환된다.
                        #실제로는 전체 갯수를 세고, 그리고 큰 수와 비교해가면서  cnt를 감소시키면 되는 부분
            if minc > cnt:
                minc = cnt
    print(f'#{tc} {minc}')

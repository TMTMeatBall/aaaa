# 1. 같은 크기 당근은 같은 상자에
# 2. 빈상자는 없다
# 3. 한 상자에 N/2초과의 당근 수가 있으면 안된다
# 4. 상자 간 당근 갯수 차이는 최소가 되어야 한다

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ci = list(map(int, input().split()))
    ci.sort()
    minci = 1000
    for i in range(N - 2):  # 소 박스
        for j in range(i + 1, N - 1):  # 중 박스
            if ci[i] != ci[i + 1] and ci[j] != ci[j + 1]: #같은 크기의 당근은 같은 박스에
                #다음의 것과 다르면 같은 것끼리는 모두 담긴 것으로 해석 가능
                #실제 ci안의 요소를 따지는 문제가 아니고, 인덱스 넘버로 해결하는 문제이므로
                A = i + 1#위의 조건을 만족하는 상황에서
                B = j - i
                C = N - 1 - j
                if A*B*C !=0 and A<=N//2 and B<=N//2 and C<=N//2:
                    if minci > max(A,B,C) - min(A,B,C):
                        minci = max(A,B,C) - min(A,B,C)
    if minci == 1000: #포장 불가인 경우
        minci = -1
    print(f'#{tc} {minci}')

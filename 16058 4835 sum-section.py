T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    max = 0
    min = 10000 * 500

    for i in range(N - M + 1):  # idx로는 7까지 #리스트 인덱싱을 for 문 넣어서 돌릴거면, 1.범위 잘 잡기 2.초기화시키면서 계산할 변수 하나 제 위치에 지정하기
        add = 0
        for j in range(M):
            add += a[i + j]
        if max < add:
            max = add
        if min > add:
            min = add
    print(f'#{tc} {max-min}')

    # sort 하고 갯수대로 더해가는 방법

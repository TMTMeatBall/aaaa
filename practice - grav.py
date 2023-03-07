T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    max_v = 0
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if a[i] > a[j]:
                cnt += 1

        if cnt > max_v:
            max_v = cnt
    print(f'#{tc} {max_v}')
# 각 블럭 더미의 임의의 최상층 값을 받았을 때에, 나머지 열들에서 뽑은 값과 비교해야 하므로 2분할하는 셈이 된다.
    # 인덱스의 2분할 한 뒤에, 값들을 비교해서 처음의 값이 다음의 값보다 크면, cnt를 세고, 그 cnt의 최댓값을 기록함
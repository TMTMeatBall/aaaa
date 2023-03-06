T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    minv = 1000
    size = [0] * 31  # 당근의 무게 최대 30개 0번 인덱스를 사용하지 않음
    for c in arr:
        size[c] += 1

    for i in range(29):
        for j in range(30):
            A = sum(size[1:i + 1])
            B = sum(size[i + 1:j + 1])
            C = sum(size[j + 1:31])
            if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                diff = max(A, B, C) - min(A, B, C)
                if minv > diff:
                    minv = diff
    if minv == 1000:
        minv = -1

    print(f'#{tc} {minv}')
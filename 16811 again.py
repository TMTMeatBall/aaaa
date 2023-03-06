T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    minv = 10000
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            # j+1:N
            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:
                A = i + 1  # 0:i+1
                B = j - i  # i+1:j+1
                C = N - j - 1  # j+1:N 각각 빼주는것으로 idx갯수를 얻는다

                if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                    # ABC가 비어있지 않고, N//2보다 같거나 적게 가지면,
                    if minv > max(A, B, C) - min(A, B, C):
                        minv = max(A, B, C) - min(A, B, C)
    if minv == 10000:
        minv = -1
    print(f'#{tc} {minv}')

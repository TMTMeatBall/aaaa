T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    result = lst[-1] - lst[0]
    print(f'#{tc} {result}')
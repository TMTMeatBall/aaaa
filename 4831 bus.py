T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    a = list(map(int,input().split()))
    #K = 1회 충전으로 이동하는 수
    #N = 종점
    #M = 충전소 갯수
    #각 지점 i 에서 k만큼 빼거나 더했을 때에 이전 충전소, 다음 충전소에 닿을 수 있는가
    cnt=0 #갯수 세어줄 cnt
    min = 500
    for i in range(M-1):
        if a[i]+K >= a[i+1]:
            cnt+=1
    print(cnt)
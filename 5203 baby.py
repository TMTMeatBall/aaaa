T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(6):
        b.append(lst[2*i+1])
        a.append(lst[2*i])
    for i in range(len(a)):
        if a.count(i)==3:
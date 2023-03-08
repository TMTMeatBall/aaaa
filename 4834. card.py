T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(input())
    cards = [0] * 10
    result = 0
    for i in range(N):
        if a[i] == '0':
            cards[0] += 1
        elif a[i] == '1':
            cards[1] += 1
        elif a[i] == '2':
            cards[2] += 1
        elif a[i] == '3':
            cards[3] += 1
        elif a[i] == '4':
            cards[4] += 1
        elif a[i] == '5':
            cards[5] += 1
        elif a[i] == '6':
            cards[6] += 1
        elif a[i] == '7':
            cards[7] += 1
        elif a[i] == '8':
            cards[8] += 1
        else:
            cards[9] += 1
    for i in range(len(cards)):
        if result <= cards[i]:
            result = cards[i]
            idx = i
    print(f'#{tc} {idx} {max(cards)}')
    # 가장 큰 숫자의 인덱스, 가장 큰 숫자 출력

    # for i in range(len(a)):
    #     cards[int(a[i])] += 1
    #if-elif-else를 위와 같이 대체 가능함
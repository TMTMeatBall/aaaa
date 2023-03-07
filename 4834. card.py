T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(input())
    cards = [0] * 10
    for i in range(N):
        cards[a[i]] += 1
    # for i in cards:
    #
    print(cards)
import heapq


def solution(operations):
    heap = []
    max_heap = []

    for i in operations:
        a = i.split()
        print(a)
        if a[0] == 'I':
            num = int(a[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num * -1, num))
        else:
            if not heap:
                pass
            elif a[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif a[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value * -1, min_value))
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]


operations = input()
solution(operations)
#문제 인풋 형태가 뭔지 잘 모르겠음
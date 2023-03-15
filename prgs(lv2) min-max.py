def solution(s):
    a = list(map(int, s.split(' ')))


    return  str(min(a)) + " " + str(max(a))

s = '-1 -2 -3 -5 -1 -2 -3 -4 -9 -8'

solution(s)

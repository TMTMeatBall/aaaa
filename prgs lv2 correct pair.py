# s=input()
# stack = []
# result = []
# answer = 'true'
# for i in s:
#     if s[i] != '(':
#         stack.append(s[i])
#     elif s[i] == '(':
#         if len(stack) != 0:
#             result.append(s[i])
#             stack.pop(0)
#         else:
#             answer = 'false'
#
# if len(s) == len(result):
#     print(answer)
# #i=1인 경우에, '('로 시작한다면, true인 경우가 있을 것.

def solution(s):
    answer = True
    stack = list()
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:


    return True

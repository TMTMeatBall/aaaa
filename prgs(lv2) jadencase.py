def solution(s):
    a = s.split(' ')
    print(a)
    answer = []
    for i in a:
        i = i.capitalize()
        answer.append(i)

    return ' '.join(answer)


s = '3people unfollowed me'

print(solution(s))

# 대문자인지 아닌지 판단하기
# ' ' 기준으로 다음이 알파벳이면 대문자로
# 1. split 이 갖는 기준을 뭘로 하는가. split은 간격대로 부숴서 부숴진 조각들을 리스트 요소로 하는 리스트를 반환함
# 2. join  함수 쓰는 법. ''.join(list) ''안에 뭘 넣는가로 리스트 안의 요소 별 나열에 간격을 뭘로 할 지 정함
# 8-1 표준 입출력

print("Python", "Java", "JavaScript", sep=" vs ") # sep 은 중간에 들어가는것


print("Python", "Java", "JavaScript", sep=" vs ", end="?")
print("무엇이 더 재미있을까요?")


print("Python", "Java", "JavaScript", sep=" vs ")
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout) #표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

scores = {"수학":0, "영어":50, '코딩':100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 정수값은 str
# ljust : 왼쪽 정렬 8자리 확보 , rjust : 오른쪽 정렬 4자리확보


# 예제 은행 대기순번표
# 001, 002, 003, 


for num in range(1, 21):
    print('대기번호 :' + str(num).zfill(3)) # zfill : 3칸을 사용하는데 빈칸에는 0을 넣는 기능



answer = input('아무 값이나 입력하세요 : ')
print('입력하신 값은 ' + answer + '입니다.')

print(type(answer)) #인풋으로 숫자 10을 넣어도 문자열로 출력 str

answkduf = 10
print(type(answkduf)) # 숫자는 int





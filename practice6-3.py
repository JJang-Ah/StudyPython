# continue 와 break

absent = [2, 5] # 결석
no_book = [7] # 책이없음

for student in range(1,11): # 1~10 번
    if student in absent:
        continue #결석 학생이면 생략하고 계쏙 진행
    elif student in no_book:
        print("오늘 수업 안해. {0}은 교무실 따라와".format(no_book))
        break # 책없는 아이 있으면 모든 동작 그만
    print("{0}, 책을 읽어봐".format(student))


# 한줄 for
# 출석 번호가 1 2 3 4 앞에 100을 붙이기로 함 > 101, 102, 103
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # 학생들의 i란 숫자에 100을 더한다
print(students)

# 학생 이름을 길이로 변환
students = ["Iron mas", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)


# 학생 이름을 대문자로 변환

students = ["Iron mas", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


#퀴즈

from random import*
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51) # 5~ 50분 소요시간
    if 5<= time <= 15: # 5! 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))



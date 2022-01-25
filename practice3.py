print(abs(-5))
print(pow(4, 2)) # 4^2
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99)) # s내림
print(ceil(3.14)) #d올림
print(sqrt(16)) #제곱근


from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10)) # 0~10
print(int(random() * 10) + 1) # 1~ 10
print(int(random() * 45) + 1)

print(randrange(1, 45)) # 1~ 45 미만의 임의의 값 생성

print(randrange(4, 28))


# quiz

from random import *
date = randrange(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

a = randint(4, 28)
print(a)
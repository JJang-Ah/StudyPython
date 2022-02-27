# 5-3 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# # menu.add("생선까스")
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")


#5-4 집합 (set)
# 중복 안됨, 순서 없음
my_set = (1,2,3,3,3)
print(my_set)


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#  교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# gkqwlqgkq (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)


# 5-5 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# 퀴즈

# from random import *
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list, 1))

# print(list)



# print("치킨 당첨자 : ", sample(list, 1))
# print("커피 당첨자 :", sample(list, 3))


from random import *
# users = [1,2,3,...100]
users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))


print(users)

shuffle(users)
print(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:3]))











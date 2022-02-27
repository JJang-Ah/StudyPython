sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990812 - 1929292"
print("성별 : " + jumin[9])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 첨부터 6까지
print("뒤 7자리 : " + jumin[9:]) # 9부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])




# 문자열 처리 함수

python = "Python is Amzing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 포함안되면 -1 이 출력
#print(python.index("Java"))
print("hi")
print(python.count("n"))

# # 문자열 포맷 (주석단축키는 컨트롤 + /)

# print("a" + "b")
# # print("a", "b")
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해여." % "파이썬")
# print("Apple 은 %c로 시작행." % "A")


# print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법 3 
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
#f를 넣으면 미리입력한 변수값이 출력가능

print("백문이 불여일견 \n 백견이 불여일타")

# print("저는 '나도코딩'입니다.")
print("저는 \"나도코딩\"입니다.")
# \", \' : 문장 내에서 따옴표
#\\ : 문장내에서 \

print("C:\\Users\\장아현\\Desktop\\PythonWorkSpace>")

# \r : 커서를 맨 앞으로 이동

print("Red App;le \rPine ")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭

print("Red\t Apple")

# quiz

site = "http://google.com"
my_str = site.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")]

# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{site}의 비밀번호는 {password}입니다.")





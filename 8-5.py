# with
#따로 close 문을 쓸 필요가 없다.

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))



# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())




#퀴즈

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file: # str > 숫자를 문자열로 바꾸기
        report_file.write("{0}주차 주간보고".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 :\n")
        report_file.write("업무 요약 :\n")


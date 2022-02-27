# 8-3 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # w : 쓰기위한 것을 표현하기 위함
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf') # a : 뒤에 이어서 추가
# score_file.write("과학 : 80")
# score_file.write('\n코딩 : 90')
# score_file.close()



# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='') #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()




# 다른 사람에게 받은 파일이라 안에 몇줄인지 뭔지 모를때
score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
score_file.close()


# 다른 방법으로는
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end='')

score_file.close()






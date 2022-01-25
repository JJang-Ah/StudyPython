#가변인자


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
#     # end는 print 함수가 끝날때 어떻게 끝나는지 정하는것 
#     print(lang1, lang2, lang3, lang4, lang5)



def profile(name, age, *language): #가변인자 *
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()





profile("유재석", 20, "파이썬", "java", "c", "c++", "c#")

profile("김태호", 26, "아잉", "몰라", "", "", "")





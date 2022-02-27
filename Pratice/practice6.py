# 6 if

# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")



temp = int(input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요 나가면 더워죽음 ㄷㄷ")
elif 10 <= temp and temp < 30:
    print("나가도 괜춘할듯 ㄱㄱ")
elif 0 <= temp and temp < 10:
    print("패딩입어라 ㄷㄷ 죽어죽어")
else:
    print("마 니 알아서해라 죽든말든")
    

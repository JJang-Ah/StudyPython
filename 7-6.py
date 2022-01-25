#지역변수 전역변수


gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))




# 퀴즈

def std_weight(ki, gen):  # 키 m 단위 (실수,), 성별 "남자" / "여자"
    if gen == "남자":
        return ki * ki *22
    else:
        return ki * ki * 21

ki = 177 #cm 단위
gen = "남자"
wei = round(std_weight(ki / 100, gen), 2) # round(   , 2) 소수점 둘쨰자리까지
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(ki, gen, wei))
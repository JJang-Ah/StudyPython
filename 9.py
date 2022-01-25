# #클래스

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = '마린'
# hp = 40
# damage = 5 #유닛의 공격력

# print("{0} 유닛이 생성되었습니다. ".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈 모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35


# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다. ".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#__init__ : 생성자 클래스로 만들어지는 ex 마린 탱크를 객체라고 한다 
# 이때 마린과 탱크는 유닛클래스의 인스턴스라고 한다. 
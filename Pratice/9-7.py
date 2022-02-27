#메소드 오버로딩

#일반 유닛

class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))


#공격 유닛

class AttackUnit(Unit): # unit 자리에 두개 이상있으면 다중 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)

        self.damage = damage
        print("{0} 유닛이 생성 되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.\
            [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃/ 탱크 등을 수송 , 공격x

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 이동함수 불편해서 추가
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


#벌쳐 : 지상 유닛, 기동성이 좋음

vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀 크루져 : 공중 유닛, 체력 좋음, 공격력도좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시") 
# 같은 이동하는 함순데 지상 유닛은 move, 공중 유닛은 fly를 써야함 불편 ㅡㅡ
# 그래서 move() 재정의

battlecruiser.move("9시")

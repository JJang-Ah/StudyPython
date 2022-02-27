#패키지


# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()

trip_to.detail()


import inspect
import random
print(inspect.getfile(random)) # 이 랜덤이라는 모듈이 어디있는지 알려줌
print(inspect.getfile(thailand))

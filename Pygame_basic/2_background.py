import pygame

pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PyPyPyPy Game") # 게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/tw5hy/바탕 화면/혼공/StudyPython/Pygame_basic/background.png")



#이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가.
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) #배경 그리기 (0, 0)은 좌표
    # screen.fill((0, 0, 255)) # rgb 값을 넣고 배경을 만들수도 있따.
    pygame.display.update() #게임 화면을 계쏙 그리기
    # 이코드가 있어야 계쏙 배경이 나온다.




# pygame 종료
pygame.quit()




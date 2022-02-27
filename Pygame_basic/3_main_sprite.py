from turtle import delay, width
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

# 스프라이트(캐릭터) 불러오기
charactor = pygame.image.load("C:/Users/tw5hy/바탕 화면/혼공/StudyPython/Pygame_basic/charactor.png")
charactor_size = charactor.get_rect().size #이미지 크기를 구해옴
charactor_width = charactor_size[0] #캐릭터의 가로크기
charactor_height = charactor_size[1] #캐릭터의 세로 크기
charactor_x_pos = screen_width/2 - 35 #화면 가로크기의 중간에 위치
charactor_y_pos = screen_height-70 # 화면 세로크기 가장 아래에 위치

to_x = 0
to_y = 0

#이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가.
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
                
            
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    charactor_x_pos += to_x
    charactor_y_pos += to_y

    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width

        
    if charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - charactor_height:
        charactor_y_pos = screen_height - charactor_height

    screen.blit(background, (0, 0)) #배경 그리기 (0, 0)은 좌표
    screen.blit(charactor, (charactor_x_pos, charactor_y_pos))
    pygame.display.update() #게임 화면을 계쏙 그리기
    # 이코드가 있어야 계쏙 배경이 나온다.




# pygame 종료
pygame.quit()




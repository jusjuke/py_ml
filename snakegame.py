import pygame
import random
import sys

pygame.init()

# 화면 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("장애물 뱀 게임")

# 색상 정의
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 뱀의 초기 위치와 길이 설정
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_length = 1
snake_speed = 5
snake_direction = (10, 0)  # 초기 뱀의 방향을 오른쪽으로 설정

# 음식 생성 함수
def spawn_food():
    x = random.randint(0, SCREEN_WIDTH - 10)
    y = random.randint(0, SCREEN_HEIGHT - 10)
    return (x // 10) * 10, (y // 10) * 10

# 장애물 생성 함수
def spawn_obstacle():
    x = random.randint(0, SCREEN_WIDTH - 10)
    y = random.randint(0, SCREEN_HEIGHT - 10)
    return (x // 10) * 10, (y // 10) * 10

# 게임 오버 화면 출력 함수
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("게임 오버", True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 18))
    pygame.display.update()
    pygame.time.delay(2000)  # 2초 대기

# 게임 루프
running = True
clock = pygame.time.Clock()
food = spawn_food()
obstacles = [spawn_obstacle()]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 뱀 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: snake_direction = (0, -10)
    if keys[pygame.K_DOWN]: snake_direction = (0, 10)
    if keys[pygame.K_LEFT]: snake_direction = (-10, 0)
    if keys[pygame.K_RIGHT]: snake_direction = (10, 0)
    
    # 뱀 머리 위치 계산
    x, y = snake[0]
    dx, dy = snake_direction
    new_x, new_y = x + dx, y + dy

    # 게임 오버 조건 체크
    if (
        new_x < 0 or new_x >= SCREEN_WIDTH or
        new_y < 0 or new_y >= SCREEN_HEIGHT or
        (new_x, new_y) in snake or
        (new_x, new_y) in obstacles
    ):
        game_over()
        pygame.quit()
        sys.exit()

    # 뱀 머리 위치 추가
    snake.insert(0, (new_x, new_y))

    # 뱀 길이 조정
    if len(snake) > snake_length:
        snake.pop()

    # 음식과 충돌 여부 확인
    if snake[0] == food:
        food = spawn_food()
        snake_length += 1

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (food[0], food[1], 10, 10))

    # 장애물 그리기
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], 10, 10))

    # 뱀 그리기
    for segment in snake:
        pygame.draw.rect(screen, RED, (segment[0], segment[1], 10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()

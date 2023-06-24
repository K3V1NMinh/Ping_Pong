from pygame import *
import random

# Initialize Pygame
init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game clock
clock = time.Clock()

# Define the paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

# Define the ball dimensions
BALL_RADIUS = 10

paddle1_pos = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_pos = (HEIGHT - PADDLE_HEIGHT) // 2
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([-1, 1]), random.choice([-1, 1])]

paddle_speed = 5
ball_speed = 5

score1 = 0
score2 = 0

# Function to reset ball position and velocity
def reset_ball():
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [random.choice([-1, 1]), random.choice([-1, 1])]

# Function to update the game state
def update():
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, score1, score2

    # Update paddle position
    keys = key.get_pressed()
    if keys[K_w] and paddle1_pos > 0:
        paddle1_pos -= paddle_speed
    if keys[K_s] and paddle1_pos < HEIGHT - PADDLE_HEIGHT:
        paddle1_pos += paddle_speed
    if keys[K_UP] and paddle2_pos > 0:
        paddle2_pos -= paddle_speed
    if keys[K_DOWN] and paddle2_pos < HEIGHT - PADDLE_HEIGHT:
        paddle2_pos += paddle_speed

    # Update ball position
    ball_pos[0] += int(ball_vel[0] * ball_speed)
    ball_pos[1] += int(ball_vel[1] * ball_speed)

    # Ball collision with paddles
    if ball_pos[0] <= PADDLE_WIDTH and paddle1_pos <= ball_pos[1] <= paddle1_pos + PADDLE_HEIGHT:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] < PADDLE_WIDTH:
        score2 += 1
        if score2 >= 5:
            return "Player 2"
        else:
            reset_ball()
    if ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_pos <= ball_pos[1] <= paddle2_pos + PADDLE_HEIGHT:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] > WIDTH - PADDLE_WIDTH - BALL_RADIUS:
        score1 += 1
        if score1 >= 5:
            return "Player 1"
        else:
            reset_ball()

    # Ball collision with walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    return None

# Game loop
running = True
winner = None
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    winner = update()

    win.fill(BLACK)
    draw.rect(win, WHITE, (PADDLE_WIDTH, paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    draw.rect(win, WHITE, (WIDTH - 2 * PADDLE_WIDTH, paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    draw.circle(win, WHITE, ball_pos, BALL_RADIUS)

    font1 = font.Font(None, 36)
    text1 = font1.render("Player 1: {}".format(score1), True, WHITE)
    text2 = font1.render("Player 2: {}".format(score2), True, WHITE)
    win.blit(text1, (50, 50))
    win.blit(text2, (WIDTH - 150, 50))

    if winner:
        font1 = font.Font(None, 36)
        text = font1.render("{} wins!".format(winner), True, WHITE)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        display.flip()
        time.wait(3000)
        running = False

    display.flip()
    clock.tick(60)

quit()

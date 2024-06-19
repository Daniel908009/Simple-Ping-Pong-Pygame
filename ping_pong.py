import pygame 
import math
import random

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([1000, 800])
pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("ball.png")
pygame.display.set_icon(icon)


running = True


# Function to check collisions
def checkcollision():
    if ballx >= playerx and ballx <= playerx + playerwith:
        if bally >= playery and bally <= playery + playerheight:
            return True
    return False



def create_player():
    player = pygame.image.load("player.png")
    return player

def create_ball():
    ball = pygame.image.load("ball.png")
    return ball
    

# Creating a player
player1 = create_player()
playerwith = player1.get_width()
playerheight = player1.get_height()
playerx = 0
playery = screen.get_height() / 2 - playerheight / 2
changeinspeed = 0

# Creating a ball
ball = create_ball()
ballwidth = ball.get_width()
ballheight = ball.get_height()
ballx = screen.get_width() / 2 - ballwidth / 2
bally = screen.get_height() / 2 - ballheight / 2
ballxspeed = 2
ballyspeed = random.randint(-2, 2)

# Main loop
while running: 
    
     # Fill the background with black color
    screen.fill((0, 0, 0))
    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the player
            if event.key == pygame.K_UP:
                changeinspeed = -5
            elif event.key == pygame.K_DOWN:
                changeinspeed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeinspeed = 0

    playery += changeinspeed

    # Move the ball
    ballx += ballxspeed
    bally += ballyspeed

    # Check for collision of the ball with the player
    if checkcollision():
        ballxspeed *= -1

    # Check for win
    if ballx <= 0:
        text = pygame.font.Font(None, 74)
        text = text.render("You Lost", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        

    # Check for boundaries of the ball    
    if ballx >= screen.get_width() - ballwidth:
        ballx = screen.get_width() - ballwidth
        ballxspeed *= -1
    elif bally <= 0:
        bally = 0
        ballyspeed *= -1
    elif bally >= screen.get_height() - ballheight:
        bally = screen.get_height() - ballheight
        ballyspeed *= -1

    # Check for boundaries of the player
    if playery <= 0:
        playery = 0
    elif playery >= screen.get_height() - playerheight:
        playery = screen.get_height() - playerheight

  

    # Draw the player
    screen.blit(player1, (playerx, playery))
    # Draw the ball
    screen.blit(ball, (ballx, bally))

    # Update the screen
    pygame.display.update()

pygame.quit()
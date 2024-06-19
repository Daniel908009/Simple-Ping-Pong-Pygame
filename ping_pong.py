import pygame 
import random

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([1000, 800], pygame.RESIZABLE)
pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("ball.png")
pygame.display.set_icon(icon)


running = True


# Function to check collisions of the ball with the players
def checkcollision():
    for i in range(2):
        if ballx <= playerx[i] + playerwith and ballx + ballwidth >= playerx[i] and bally <= playery[i] + playerheight and bally + ballheight >= playery[i]:
            return True
    return False

# Function to reset the game
def reset():
    global ballx, bally, ballyspeed, ballxspeed, playerx
    ballx = screen.get_width() / 2 - ballwidth / 2
    bally = screen.get_height() / 2 - ballheight / 2
    ballyspeed = random.choice([-1, 1, 2, -2])
    ballxspeed = random.choice([-1, 1, 2, -2])
    playerx = [0, screen.get_width() - playerwith]
    for i in range(2):
        playery[i] = screen.get_height() / 2 - playerheight / 2

# Function to create players and ball
def create_player():
    player = pygame.image.load("player.png")
    return player

def create_ball():
    ball = pygame.image.load("ball.png")
    return ball
    

# Creating a player list
players = []

for i in range(2):
    player = create_player()
    players.append(player)
playerwith = player.get_width()
playerheight = player.get_height()

playerx = [0, screen.get_width() - playerwith]
playery = [screen.get_height() / 2 - playerheight / 2, screen.get_height() / 2 - playerheight / 2]

changeinspeed = [0, 0]

# Creating a ball
ball = create_ball()
ballwidth = ball.get_width()
ballheight = ball.get_height()
ballx = screen.get_width() / 2 - ballwidth / 2
bally = screen.get_height() / 2 - ballheight / 2
ballxspeed = random.choice([-1, 1, 2, -2])
ballyspeed = random.choice([-1, 1, 2, -2])
collisions = 0

# Main loop
while running: 
    
     # Fill the background with black color
    screen.fill((0, 0, 0))
    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            # Move the players
            elif event.key == pygame.K_UP:
                changeinspeed[0] = -5
            elif event.key == pygame.K_DOWN:
                changeinspeed[0] = 5
            elif event.key == pygame.K_w:
                changeinspeed[1] = -5
            elif event.key == pygame.K_s:
                changeinspeed[1] = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeinspeed[0] = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                changeinspeed[1] = 0
        

    # Move the players
    for i in range(2):
        playery[i] += changeinspeed[i]

    # Move the ball
    ballx += ballxspeed
    bally += ballyspeed
     

    # Check for collision of the ball with the players
    if checkcollision():
        ballxspeed *= -1
        collisions += 1
        if collisions % 5 == 0:
            ballxspeed *= 1.5
            ballyspeed *= 1.5
            

    # Check for win
    if ballx <= 0 or ballx >= screen.get_width() - ballwidth:
        ballyspeed = 0
        ballxspeed = 0
        text = pygame.font.Font(None, 74)
        if ballx <= 0:
            text = text.render("Player 1 Lost", True, (255, 255, 255))
        else:
            text = text.render("Player 2 Lost", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))
        

    # Check for boundaries of the ball    
    if bally <= 0:
        bally = 0
        ballyspeed *= -1
    elif bally >= screen.get_height() - ballheight:
        bally = screen.get_height() - ballheight
        ballyspeed *= -1

    # Check for boundaries of the players
    for i in range(2):
        if playery[i] <= 0:
            playery[i] = 0
        elif playery[i] >= screen.get_height() - playerheight:
            playery[i] = screen.get_height() - playerheight

  

    # Draw the players
    for i in range(2):
        screen.blit(players[i], (playerx[i], playery[i]))

    # Draw the ball
    screen.blit(ball, (ballx, bally))

    # Update the screen
    pygame.display.update()

pygame.quit()

    # Update the screen
    pygame.display.update()

pygame.quit()

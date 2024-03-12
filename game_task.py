# Importing "pygame" to use functions in accordance with games
# Importing "random" to use random numbers generated
# Importing "Mixer" to add music/ sounds to the game
# Importing "time" to add time functions to the game

import pygame
import random
from pygame import mixer
import time
pygame.init() 

#allocating a resoltution to the game (Full HD)

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))

#added my music/ sounds as variables from the game folder

RIP_Sound = pygame.mixer.Sound('PyGameDeath.wav')
Victory = pygame.mixer.Sound('PyGameVictory.wav')
mixer.music.load('PyGameMusic3.wav')
mixer.music.play(-1)

#allocating each image from Game folder to a variable

background_image = pygame.image.load("Background.jpg")
player = pygame.image.load("Warrior.png")
enemy1 = pygame.image.load("Dragon1.png")
enemy2 = pygame.image.load("Dragon2.png")
enemy3 = pygame.image.load("Dragon3.png")
prize1 = pygame.image.load("Prize.png")

#images original resolutions were too big so resized them using transform.scale function

player = pygame.transform.scale(player, (200, 150))
prize1 = pygame.transform.scale(prize1, (100, 100))
enemy1 = pygame.transform.scale(enemy1, (200, 150))
enemy2 = pygame.transform.scale(enemy2, (200, 150))
enemy3 = pygame.transform.scale(enemy3, (200, 150))

#allocating each images height & width to variables by finding them through the "get" function

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize1_height = prize1.get_height()
prize1_width = prize1.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

#allocating the X/Y position of the player/prize/enemy's images for the start of
#the game to show where the image is placed at the beginning

playerXPosition = 100
playerYPosition = 500

prize1XPosition = 1700
prize1YPosition = 500

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height) #enemys use "random" placement function
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
 
#using boolean as a means of using the arrow keys for the movement of the Player

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

#start of the game loop

while 1:
    
    screen.fill(0)
    screen.blit(background_image, [0, 0])
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize1, (prize1XPosition, prize1YPosition))
    
    
    pygame.display.flip() #used to update the screen
    
    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # These events check if the user presses the arrow keys down "KEYDOWN"
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
                
        # These events check if the user releases the arrow keys "KEYUP"
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # These events are to maneuver to players X/Y positions (Up, Down, Left & Right)
            
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1         

    #this is a bounding box for the player, prize & enemys used to put a box around them while they move
    
    playerBox = pygame.Rect(player.get_rect())
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prize1Box = pygame.Rect(prize1.get_rect())
    prize1Box.top = prize1YPosition
    prize1Box.left = prize1XPosition


    #adding in collisions when the players box touches the other boxes causing an effect of winning or loosing  

    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):

        pygame.mixer.music.stop() #Background music stops & defeat sound plays 
        RIP_Sound.play()
        time.sleep(13)            #Time.sleep lets the music play until it's finnished then the program quits
        
        print("You lose!") 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prize1Box):

        pygame.mixer.music.stop()
        Victory.play()
        time.sleep(13)
        
        print("You Win!")       

        pygame.quit()
        exit(0)
    
    #the rate at which the enemys move
    
    enemy1XPosition -= 0.30
    enemy2XPosition -= 0.30
    enemy3XPosition -= 0.30


#Refernces:

#Pictures royalty free from cleanPNG.com & background picture from Pexels.com 08.03.2021
#Music slef made by Ryan Jonathan Cox 08.03.2021

#Time & Sounds from Stackoverflow.com
#https://stackoverflow.com/questions/23247159/how-to-get-pygame-to-quit-after-playing-a-song 03.08.2021

from ast import If
from pydoc import plain
from re import X
from tkinter import Y
from turtle import left, ycor
import pygame
import os.path
from pygame import mixer
import math

# vars
def GetFullFilePath(fileName):
    return os.path.join(os.path.dirname(__file__), fileName)
global window, coin_list, gravity_on, chosen_one_y, right_value, left_value,level_one,portal_one_rect,a,b,level_three,level_four,level_five
character_chosen = False
chosen_one_y = 0
chosen_one_x = 50 
chosen_one_width = 0
chosen_one_length = 0
coin_counter = 0 
coin_list = pygame.sprite.Group()
done = False
coin_collected = False
clock = pygame.time.Clock()
pygame.init()
window_x = 980
size = (980, 440)
window = pygame.display.set_mode(size)
font_button = pygame.font.Font(GetFullFilePath("Daydream.ttf"), 18)
value = 0 
sky_list = []
speed = 0
on = True
tiles = math.ceil(window_x/600) + 1
chosen_one = []
gravity = 0 
moving = False
exit_surf = pygame.image.load(GetFullFilePath("exit_button.png")).convert_alpha()
exit_surf = pygame.transform.scale(exit_surf, (60,60 ))
exit_rect = exit_surf.get_rect(center=(950, 410))
dead = False
collected_coins = []
platy = 0 
collide_top = False
gravity_on = True 
left_value = True
right_value = True
level_one = False
level_two = False
level_three = False
level_four = False
level_five = False
font = pygame.font.Font(GetFullFilePath("Daydream.ttf"), 17)
font_button = pygame.font.Font(GetFullFilePath("Daydream.ttf"), 15)
# pictures
bunny_sprite = [pygame.image.load(("bunny1.png")),
               pygame.image.load(("bunny2.png")),
               pygame.image.load(("bunny3.png")),
               pygame.image.load(("bunny4.png"))]
redbunny_sprite = [pygame.image.load(("redbunny1.png")),
               pygame.image.load(("redbunny2.png")),
               pygame.image.load(("redbunny3.png")),
               pygame.image.load(("redbunny4.png"))]
goat_sprite = [pygame.image.load(("goat1.png")),
               pygame.image.load(("goat2.png")),
               pygame.image.load(("goat3.png")),
               pygame.image.load(("goat4.png"))]
purplegoat_sprite = [pygame.image.load(("purplegoat1.png")),
               pygame.image.load(("purplegoat2.png")),
               pygame.image.load(("purplegoat3.png")),
               pygame.image.load(("purplegoat4.png"))]
cat_sprite = [pygame.image.load(("cat1.png")),
               pygame.image.load(("cat2.png")),
               pygame.image.load(("cat3.png")),
               pygame.image.load(("cat4.png"))]


#background
back1_surf = pygame.image.load(GetFullFilePath("back.png.jpg")).convert_alpha()
back1_surf = pygame.transform.scale(back1_surf, (800, 450))
back1_rect = back1_surf.get_rect(center=(-1600, 225))


# spikes

#lightning_event = pygame.USEREVENT + 1

# box that hovers on top of sprites when player is choosing the charecter
def hover_box(box_x,box_y):
    global character_chosen, scope_var,chosen_one,chosen_one_width,chosen_one_length,chosen_one_y,level_one,b,level_two,level_five
    rectangle = pygame.Rect(box_x,box_y,80,100)
    mouse_pos = pygame.mouse.get_pos()
    if rectangle.collidepoint(mouse_pos):
        rectangle = pygame.draw.rect(window,(230,237,251),pygame.Rect(box_x,box_y,80,110),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            character_chosen = True
            level_one = True
            if box_x == 150:
                chosen_one = bunny_sprite
                chosen_one_width = 55
                chosen_one_length = 85
                chosen_one_y = 300
                b = 27
            if box_x == 307:
                chosen_one = redbunny_sprite
                chosen_one_width = 55
                chosen_one_length = 85
                chosen_one_y = 300
                b = 27
            if box_x == 475:
                chosen_one = goat_sprite
                chosen_one_width = 65
                chosen_one_length = 90
                chosen_one_y = 300
                b = 27
            if box_x == 635:
                chosen_one = purplegoat_sprite
                chosen_one_width = 65
                chosen_one_length = 90
                chosen_one_y = 300
                b = 27
            if box_x == 780:
                chosen_one = cat_sprite
                chosen_one_width = 55
                chosen_one_length = 85
                chosen_one_y = 300
                b = 27
            
# animations with animals
def animal_animation(sprite,sprite_x,sprite_y,sprite_width,sprite_length):
    global sprite_rect
    sprite_animation = sprite[value]
    mouse_pos = pygame.mouse.get_pos()
    sprite_animation = pygame.transform.scale(sprite_animation,(sprite_width,sprite_length))
    sprite_rect = sprite_animation.get_rect(center=(sprite_x,sprite_y))
    window.blit(sprite_animation,sprite_rect)

def spikes(spike_x,spike_y):
    global spike_rect
    spike_animation = pygame.image.load(GetFullFilePath("spike.png")).convert_alpha()
    spike_animation = pygame.transform.scale(spike_animation, (40, 40))
    spike_rect = spike_animation.get_rect(center=(spike_x, spike_y))
    window.blit(spike_animation, spike_rect)
    if spike_rect.colliderect(sprite_rect):
        global dead
        dead = True

def spikes_flip(spike_x,spike_y):
    global spike_flip_rect
    spike_flip_animation = pygame.image.load(GetFullFilePath("spike_upsidedown.png")).convert_alpha()
    spike_flip_animation = pygame.transform.scale(spike_flip_animation, (40, 40))
    spike_flip_rect = spike_flip_animation.get_rect(center=(spike_x, spike_y))
    window.blit(spike_flip_animation, spike_flip_rect)
    if spike_flip_rect.colliderect(sprite_rect):
        global dead
        dead = True
def coins(coin_x, coin_y):
    global coin_rect, coin_counter,coin_collected, coin_list, coin_animation,stuff
    coin_animation = pygame.image.load(GetFullFilePath("coin.png")).convert_alpha()
    coin_animation = pygame.transform.scale(coin_animation, (35, 35))
    coin_rect = coin_animation.get_rect(center=(coin_x, coin_y))
    window.blit(coin_animation, coin_rect)


def platform (platform_x,platform_y,plat_y):
    global platform_rect, collide_top, gravity_on,platy,chosen_one_y, gravity, chosen_one_x, chosen_one_length, chosen_one_width, left_value, right_value
    platform_surf = pygame.image.load(GetFullFilePath("platform.png")).convert_alpha()
    platform_surf = pygame.transform.scale(platform_surf, (100,40))
    platform_rect = platform_surf.get_rect(center=(platform_x,platform_y))
    #
    window.blit(platform_surf, platform_rect)     
    if sprite_rect.colliderect(platform_rect): 

        a = 1
        if (plat_y - a) <= chosen_one_y <= (plat_y + 1):
                chosen_one_y = plat_y 
                gravity = 0
                if pygame.key.get_pressed()[pygame.K_UP]:                
                    gravity -= 12

def bounce (bounce_x,bounce_y):
    global chosen_one_y,gravity, a
    bounce_surf = pygame.image.load(GetFullFilePath("bounce.png")).convert_alpha()
    bounce_surf = pygame.transform.scale(bounce_surf, (80,20))
    bounce_rect = bounce_surf.get_rect(center=(bounce_x,bounce_y))
    window.blit(bounce_surf, bounce_rect)
    if sprite_rect.colliderect(bounce_rect):
        gravity -= b

def portal(portal_x,portal_y):
    global portal_one_rect
    portal_one = pygame.image.load(GetFullFilePath("hole.png")).convert_alpha()
    portal_one = pygame.transform.scale(portal_one, (30, 70))
    portal_one_rect = portal_one.get_rect(center=(portal_x, portal_y))
    window.blit(portal_one,portal_one_rect)
def portal_flip(portal_x,portal_y):
    global portal_flip_rect
    portal_flip = pygame.image.load(GetFullFilePath("hole_upsidedown.png")).convert_alpha()
    portal_flip = pygame.transform.scale(portal_flip, (80, 20))
    portal_flip_rect= portal_flip.get_rect(center=(portal_x, portal_y))
    window.blit(portal_flip,portal_flip_rect)


soundFile = GetFullFilePath('song.mp3')
mixer.init()
mixer.music.load(soundFile)
mixer.music.play()

# code stuffc

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       
         # jumping
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:           
            if 300 <= chosen_one_y <= 301:
                chosen_one_y = 300
                gravity -= 12
                print("jump")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and left_value == True:
            if chosen_one_x > 0:
                chosen_one_x -= 40
                print ("left")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and right_value == True:       
            if chosen_one_x < 920:
                chosen_one_x += 40        
                print("right")

               
                                  
    # gravity 
    #if gravity_on == True:
    gravity += 1
    chosen_one_y += gravity
    if chosen_one_y > 300:
       gravity = 0
       chosen_one_y = 300

    speed_sprite = 10
    #animations of the sprites
    value += 1
    if value >= len(bunny_sprite):
        value = 0
    if value >= len(redbunny_sprite):
        value = 0
    if value >= len(goat_sprite):
        value = 0
    if value >= len(purplegoat_sprite):       
        value = 0
    if value >= len(cat_sprite):    
        value =0
        
    # hover box for "choose your charecter"

    for i in range(0,tiles):
        window.blit(back1_surf,(i * 600 + speed, 0))
    speed -= 3
    if abs(speed) > 600:
        speed = 0

    # backgrounds
    if on:
        window.blit(exit_surf, exit_rect)

     # exit button 
    if event.type == pygame.MOUSEBUTTONDOWN:
       mouse_pos = pygame.mouse.get_pos()
       if exit_rect.collidepoint(mouse_pos):
          pygame.quit()
          exit()       

    # choose your charecter animations:
    if character_chosen is False:
        text = font.render("choose your character", True, (250, 250, 250))
        window.blit(text, (300, 170))
        hover_box(150,245)
        hover_box(307,245)
        hover_box(475,245)
        hover_box(635,245)
        hover_box(780,245)   
        animal_animation(bunny_sprite,190,300,60,87)
        animal_animation(redbunny_sprite,350,300,60,87)
        animal_animation(goat_sprite,515,300,70,87)
        animal_animation(purplegoat_sprite,675,300,70,87)
        animal_animation(cat_sprite,815,300,56,87)     
        pygame.time.wait(100)


        
    #
    # after choosing charecter 
    # level one    
    if level_one is True:
        text = font.render("level one", True, (250, 250, 250))
        window.blit(text, (17, 10))
        animal_animation(chosen_one,chosen_one_x,chosen_one_y,chosen_one_width,chosen_one_length)
        spikes(120,325)
        spikes(300,325)
        spikes(440,325)
        spikes(600,325)
        spikes(770,325)
        portal(900,300)
        if sprite_rect.colliderect(portal_one_rect):
            chosen_one_x = 50 
            level_two = True
            level_one = False
        
        twotext = font.render(" restart", True, (250, 250, 250))
        window.blit(twotext, (10, 400))
        rectangle= pygame.draw.rect(window,(230,237,251),pygame.Rect(3,385,150,50),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(mouse_pos):
                level_one = False
                character_chosen = False
     #level 3   
    if level_three is True:
        text = font.render("level three", True, (250, 250, 250))
        window.blit(text, (17, 10))
        animal_animation(chosen_one,chosen_one_x,chosen_one_y,chosen_one_width,chosen_one_length)
        #pygame.time.wait(100)
        bounce(170,330)
        spikes(320,325)
        spikes(270,325)
        spikes(360,325)
        spikes(550,325)
        platform(630,310,250)
        platform(730,310,250)
        spikes(670,270)
        bounce(740,280)
        portal(900,80)
     #   
        if sprite_rect.colliderect(portal_one_rect):
            chosen_one_x = 50
            level_four = True
            level_three = False
        
        twotext = font.render(" restart", True, (250, 250, 250))
        window.blit(twotext, (10, 400))
        rectangle= pygame.draw.rect(window,(230,237,251),pygame.Rect(3,385,150,50),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(mouse_pos):
                level_three = False
                character_chosen = False
    #level 4
    if level_four is True:
        text = font.render("level four", True, (250, 250, 250))
        window.blit(text, (17, 10))
        animal_animation(chosen_one,chosen_one_x,chosen_one_y,chosen_one_width,chosen_one_length)
        spikes(200,326)
        spikes(160,326)
        spikes(120,326)
        bounce(285,310)
        bounce(400,260)
        spikes_flip(500,20)
        spikes_flip(540,20)
        spikes_flip(580,20)
        spikes_flip(620,20)
        spikes_flip(660,20)
        spikes(500,326)
        spikes(540,326)
        spikes(580,326)
        spikes(620,326)
        spikes(660,326)
        bounce(540,285)
        bounce(690,230)
        bounce(850,326)
        portal_flip(930,20)

        if sprite_rect.colliderect(portal_flip_rect):
            chosen_one_x = 50 
            chosen_one_y = 300
            level_four = False
            level_five = True
        
        twotext = font.render(" restart", True, (250, 250, 250))
        window.blit(twotext, (10, 400))
        rectangle= pygame.draw.rect(window,(230,237,251),pygame.Rect(3,385,150,50),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(mouse_pos):
                level_four = False
                character_chosen = False
     # level 2
    if level_two is True:     
        text = font.render("level two", True, (250, 250, 250))
        window.blit(text, (17, 10))
        animal_animation(chosen_one,chosen_one_x,chosen_one_y,chosen_one_width,chosen_one_length)
        spikes(220,326)
        spikes(260,326)
        spikes(300,326)
        spikes(340,326)
        spikes(380,326)
        spikes(420,326)
        spikes(460,326)
        spikes(500,326)
        spikes(540,326)
        spikes(580,326)
        spikes(620,326)
        spikes(660,326)
        spikes(700,326)
        spikes(740,326)
        spikes(780,326)
        spikes(820,326)
        spikes(860,326)
        spikes(900,326)
        spikes(940,326)
        spikes(980,326)
        spikes_flip(220,20)
        spikes_flip(260,20)
        spikes_flip(300,20)
        spikes_flip(340,20)
        spikes_flip(380,20)
        spikes_flip(420,20)
        spikes_flip(460,20)
        spikes_flip(500,20)
        spikes_flip(540,20)
        spikes_flip(580,20)
        spikes_flip(620,20)
        spikes_flip(660,20)
        spikes_flip(700,20)
        spikes_flip(740,20)
        spikes_flip(780,20)
        spikes_flip(820,20)
        spikes_flip(860,20)
        spikes_flip(900,20)
        spikes_flip(940,20)
        spikes_flip(980,20)
        bounce(140,330)
        bounce(300,280)
        bounce(500,280)
        bounce(700,280)
        bounce(900,280)
        portal(950,200)

        if sprite_rect.colliderect(portal_one_rect):
            chosen_one_x = 50 
            level_two = False
            level_three = True
        
        twotext = font.render(" restart", True, (250, 250, 250))
        window.blit(twotext, (10, 400))
        rectangle= pygame.draw.rect(window,(230,237,251),pygame.Rect(3,385,150,50),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(mouse_pos):
                level_two = False
                character_chosen = False
    if level_five is True:    
        text = font.render("level five", True, (250, 250, 250))
        window.blit(text, (17, 10))
        animal_animation(chosen_one,chosen_one_x,chosen_one_y,chosen_one_width,chosen_one_length)
        spikes(220,326)
        spikes(260,326)
        spikes(300,326)
        spikes(340,326)
        spikes(380,326)
        spikes(420,326)
        spikes(460,326)
        spikes(500,326)
        spikes(540,326)
        spikes(580,326)
        spikes(620,326)
        spikes(660,326)
        spikes(700,326)
        spikes(740,326)
        spikes(780,326)
        spikes(820,326)
        spikes(860,326)
        spikes(900,326)
        spikes(940,326)
        spikes(980,326)
        spikes_flip(220,20)
        spikes_flip(260,20)
        spikes_flip(300,20)
        spikes_flip(340,20)
        spikes_flip(380,20)
        spikes_flip(420,20)
        spikes_flip(460,20)
        spikes_flip(500,20)
        spikes_flip(540,20)
        spikes_flip(580,20)
        spikes_flip(620,20)
        spikes_flip(660,20)
        spikes_flip(700,20)
        spikes_flip(740,20)
        spikes_flip(780,20)
        spikes_flip(820,20)
        spikes_flip(860,20)
        spikes_flip(900,20)
        spikes_flip(940,20)
        spikes_flip(980,20)
        bounce(140,330)
        portal(950,200)
        if sprite_rect.colliderect(portal_one_rect):
            print("you won!")

        twotext = font.render(" restart", True, (250, 250, 250))
        window.blit(twotext, (10, 400))
        rectangle= pygame.draw.rect(window,(230,237,251),pygame.Rect(3,385,150,50),4 )
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(mouse_pos):
                level_five = False
                character_chosen = False

        


    # if hitting spikes
    if dead is True:
           chosen_one_x = 50
           chosen_one_y = 325
    if chosen_one_y == 325:
        dead = False


        
    clock.tick(20)
    pygame.display.update()
    pygame.display.flip()
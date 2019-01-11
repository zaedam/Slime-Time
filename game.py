# Benny Le (bl6ra) and Zaeda Meherin (zm5du)

#ADD A "LEVEL UP" AFTER IT GETS FAST
import pygame
import gamebox
import random

camera = gamebox.Camera(550, 500)

slimeball = gamebox.load_sprite_sheet("https://i.imgur.com/aJXqmD6.png", 1, 10)
slimeball_hit = gamebox.load_sprite_sheet('https://i.imgur.com/gRzI7vl.png', 1, 10)
all_berries = gamebox.load_sprite_sheet("https://i.imgur.com/Tx6oYo2.png", 4, 4)
health_msg = gamebox.from_text(300, 20, 'health:', 25, "White")
fireball = gamebox.load_sprite_sheet('https://i.imgur.com/bSSpTwq.png', 4, 8)
all_coins = gamebox.load_sprite_sheet('https://i.imgur.com/OLq6nrN.png', 1, 1)


coin = gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(0, 450), all_coins[0])



hit = False
speedup = False

slime = gamebox.from_image(camera.x, camera.y, slimeball[1])
slime.scale_by(1.5)
score = 0
scorebox = 0

fires = [gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(0, 50),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(0, 50),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 650), camera.y - random.randint(100, 150),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 450), camera.y - random.randint(150, 200),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(0, 50),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 750), camera.y - random.randint(200, 250),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 570), camera.y - random.randint(125, 175),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 750), camera.y - random.randint(170, 230),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 750), camera.y - random.randint(230, 280),
                            fireball[1]),
         gamebox.from_image(camera.x - random.randint(50, 750), camera.y - random.randint(300, 350),
                            fireball[1]),
         ]

for fire in fires:
    fire.speedy = 5

berries = [gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(0, 50), all_berries[9]),
           gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(170, 230), all_berries[13]),
           gamebox.from_image(camera.x - random.randint(50, 490), camera.y - random.randint(75, 280), all_berries[15])
           ]

for berry in berries:
    berry.speedy = 5

background = gamebox.from_image(camera.x, 500, "https://i.imgur.com/VCh0VE7.png")
background.scale_by(1.5)

game_on = False
ticks = 0
harm = 0
hit_ticks = 0
count = 0
Lspeed = -5
Rspeed = 5
doublescore = 500


def tick(keys):
    global ticks
    global game_on
    global harm
    global score
    global scorebox
    global hit
    global hit_ticks
    global speedup
    global count
    global Lspeed
    global Rspeed
    global doublescore

    ticks += 1
    slime.move(0, 0.5)

    if game_on:
        camera.clear('#6E59BB')
        camera.draw(background)
        camera.draw(health_msg)
        slime.move_speed()
    else:
        camera.clear('#6E59BB')
        camera.draw(background)
        name = gamebox.from_text(camera.x, camera.y - 100, "SLIME TIME", 40, '#78A0F8')
        user_name = gamebox.from_text(camera.x, camera.y - 170, "Benny Le (bl6ra) and Zaeda Meherin (zm5du)", 25,
                                      '#FFFFFF')
        instructions = gamebox.from_text(camera.x, camera.y - 20,
                                         "Press arrow keys to move left and right", 25,
                                         '#FFFFFF')
        instructions2 = gamebox.from_text(camera.x, camera.y, "Collect berries and avoid red fire", 25,
                                          '#FFFFFF')
        start_box = gamebox.from_color(camera.x, camera.y - 100, '#DEE2FF', 175, 50)
        image = gamebox.from_image(camera.x, camera.y - 130, slimeball[2])
        image.scale_by(2)
        camera.draw(start_box)
        camera.draw(name)
        camera.draw(user_name)
        camera.draw(instructions)
        camera.draw(instructions2)
        camera.draw(image)
        camera.draw(gamebox.from_text(camera.x, camera.y + 50, 'Press SPACE!', 50, "#FFFFFF"))

    slime.bottom = camera.bottom - 50

    if pygame.K_SPACE in keys:
        game_on = True

    if pygame.K_LEFT in keys and speedup == False:
        slime.move(Lspeed, 0)

    if pygame.K_RIGHT in keys and speedup == False:
        slime.move(Rspeed, 0)

    if ticks // 6:
        score += 1


    camera.display()


gamebox.timer_loop(30, tick)

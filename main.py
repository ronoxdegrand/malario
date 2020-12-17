import pygame
import os
import time

_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
pygame.display.set_caption('Malario')
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()

x_player1 = 570
y_player1 = 650
flip_line = False

x_raft1 = 5
x_raft2 = 805
x_raft3 = 165
x_raft4 = 965
flip_raft1 = False
flip_raft2 = False
flip_raft3 = False
flip_raft4 = True

score1 = 0
score2 = 0

exp = 3
base = 2
check = 1

pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN and pressed[pygame.K_UP]:
        y_player1 -= 80
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('move.wav'))
    if event.type == pygame.KEYDOWN and pressed[pygame.K_DOWN]:
        y_player1 += 80
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('move.wav'))
    if event.type == pygame.KEYDOWN and pressed[pygame.K_LEFT]:
        x_player1 -= 80
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('move.wav'))
    if event.type == pygame.KEYDOWN and pressed[pygame.K_RIGHT]:
        x_player1 += 80
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('move.wav'))

    bg = pygame.image.load('bg.jpg')
    screen.blit(bg, (0, 0))

    pygame.draw.rect(screen, (112, 84, 62), pygame.Rect(0, 560, 1200,
                     80))
    pygame.draw.rect(screen, (112, 84, 62), pygame.Rect(0, 400, 1200,
                     80))
    pygame.draw.rect(screen, (112, 84, 62), pygame.Rect(0, 240, 1200,
                     80))
    pygame.draw.rect(screen, (112, 84, 62), pygame.Rect(0, 80, 1200,
                     80))

    screen.blit(get_image('raft.png'), (x_raft1, 565))
    if x_raft1 > 1125:
        flip_raft1 = True
    if x_raft1 < 5:
        flip_raft1 = False
    if flip_raft1 is False:
        x_raft1 += 80
    else:
        x_raft1 -= 80

    screen.blit(get_image('raft.png'), (x_raft2, 405))
    if x_raft2 > 1125:
        flip_raft2 = True
    if x_raft2 < 5:
        flip_raft2 = False
    if flip_raft2 is False:
        x_raft2 += 80
    else:
        x_raft2 -= 80

    screen.blit(get_image('raft.png'), (x_raft3, 245))
    if x_raft3 > 1125:
        flip_raft3 = True
    if x_raft3 < 5:
        flip_raft3 = False
    if flip_raft3 is False:
        x_raft3 += 80
    else:
        x_raft3 -= 80

    screen.blit(get_image('raft.png'), (x_raft4, 85))
    if x_raft4 > 1125:
        flip_raft4 = True
    if x_raft4 < 5:
        flip_raft4 = False
    if flip_raft4 is False:
        x_raft4 += 80
    else:
        x_raft4 -= 80

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(85, 165, 70, 70))
    if x_player1 - 5 == 85 and y_player1 - 5 == 165:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 30
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 10
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(245, 165, 70, 70))
    if x_player1 - 5 == 245 and y_player1 - 5 == 165:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 30
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 10
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(645, 165, 70, 70))
    if x_player1 - 5 == 645 and y_player1 - 5 == 165:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 30
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 10
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(885, 165, 70, 70))
    if x_player1 - 5 == 885 and y_player1 - 5 == 165:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 40
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 10
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(165, 325, 70, 70))
    if x_player1 - 5 == 165 and y_player1 - 5 == 325:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 20
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 20
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(405, 325, 70, 70))
    if x_player1 - 5 == 405 and y_player1 - 5 == 325:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 20
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 20
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(565, 325, 70, 70))
    if x_player1 - 5 == 565 and y_player1 - 5 == 325:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 20
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 20
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(965, 325, 70, 70))
    if x_player1 - 5 == 965 and y_player1 - 5 == 325:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 20
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 20
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(5, 485, 70, 70))
    if x_player1 - 5 == 5 and y_player1 - 5 == 485:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 10
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 30
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(485, 485, 70, 70))
    if x_player1 - 5 == 485 and y_player1 - 5 == 485:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 10
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 30
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(725, 485, 70, 70))
    if x_player1 - 5 == 725 and y_player1 - 5 == 485:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 10
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 30
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1045, 485, 70, 70))
    if x_player1 - 5 == 1045 and y_player1 - 5 == 485:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 10
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 30
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)

    if y_player1 == 10:
        if flip_line is False:
            flip_line = True
            score1 += 40
    if y_player1 == 650:
        if flip_line is True:
            flip_line = False
            score2 += 40
            check = 0

    font = pygame.font.Font('freesansbold.ttf', 36)
    text = font.render('FINISH LINE', True, (255, 255, 255))
    textRect = text.get_rect()
    if flip_line is False:
        textRect.center = (600, 40)
        screen.blit(get_image('player1.png'), (x_player1, y_player1))
    else:
        textRect.center = (600, 680)
        screen.blit(get_image('player2.png'), (x_player1, y_player1))
    screen.blit(text, textRect)

    if x_player1 > 1130:
        x_player1 = 1130
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bump.wav'))
    if x_player1 < 10:
        x_player1 = 10
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bump.wav'))
    if y_player1 > 650:
        y_player1 = 650
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bump.wav'))
    if y_player1 < 10:
        y_player1 = 10
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bump.wav'))

    if x_player1 - 5 == x_raft1 and y_player1 - 5 == 565:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 5
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 35
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    if x_player1 - 5 == x_raft2 and y_player1 - 5 == 405:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 15
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 25
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    if x_player1 - 5 == x_raft3 and y_player1 - 5 == 245:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        x_player1))
            score1 += 25
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        x_player1))
            score2 += 15
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)
    if x_player1 - 5 == x_raft4 and y_player1 - 5 == 85:
        if flip_line is False:
            flip_line = True
            textRect.center = (600, 680)
            x_player1 = 570
            y_player1 = 10
            screen.blit(get_image('player2.png'), (x_player1,
                        y_player1))
            score1 += 35
        else:
            flip_line = False
            textRect.center = (600, 40)
            x_player1 = 570
            y_player1 = 650
            screen.blit(get_image('player1.png'), (x_player1,
                        y_player1))
            score2 += 5
            check = 0
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.wav'))
        screen.blit(text, textRect)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1200, 0, 80, 720))

    def score():
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('MARIO', True, (255, 255, 255))
        textRect.center = (1320, 700)
        screen.blit(text, textRect)
        text = font.render('LUIGI', True, (255, 255, 255))
        textRect.center = (1325, 40)
        screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render(str(score1), True, (255, 255, 255))
        textRect.center = (1330, 640)
        screen.blit(text, textRect)
        text = font.render(str(score2), True, (255, 255, 255))
        textRect.center = (1330, 80)
        screen.blit(text, textRect)

    score()
    pygame.display.flip()

    if flip_line is False and check == 0:
        base += exp
        check = 1

    if base >= 21:
        done = True
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1280,
                         720))
        if score1 > score2:
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render('MARIO HAS WON', True, (255, 255, 255))
            textRect.center = (600, 330)
        elif score2 > score1:
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render('LUIGI HAS WON', True, (255, 255, 255))
            textRect.center = (600, 330)
        else:
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render('ITS A TIE', True, (255, 255, 255))
            textRect.center = (600, 330)
        screen.blit(text, textRect)
        pygame.display.update()
        time.sleep(6)

    clock.tick(base)

pygame.quit()
quit()

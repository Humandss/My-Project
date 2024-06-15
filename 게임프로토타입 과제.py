# C177014 반욱현, C177022 이승노

import pygame
import random
from objects import Background, Player, Enemy, Bullet, Explosion, Fuel, HealthUp, Button, Message

#스크린 설정

pygame.init()
SCREEN = WIDTH, HEIGHT = 400, 700

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

else:
    win = pygame.display.set_mode(SCREEN,pygame.NOFRAME, pygame,SCALED | pygame.FULLSCREEN)

#프레임 설정
    
clock = pygame.time.Clock()
FPS = 24

#색

WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLACK = (25, 25, 25)
ORANGE = (255,100,10)
YELLOW = (255,255,0)
NAVY_BLUE = (0,0,100)

#폰트

game_over_font = 'Assets/Fonts/ghostclan.ttf'
score_font = 'Assets/Fonts/DalelandsUncialBold-82zA.ttf'
final_score_font = 'Assets/Fonts/DroneflyRegular-K78LA.ttf'
final_score1_font = 'Assets/Fonts/ghostclan.ttf'
maximum_score_font = 'Assets/Fonts/DroneflyRegular-K78LA.ttf'
maximum_score1_font = 'Assets/Fonts/ghostclan.ttf'
coin_font = 'Assets/Fonts/DalelandsUncialBold-82zA.ttf'
total_coin_font = 'Assets/Fonts/ghostclan.ttf'
total_coin1_font = 'Assets/Fonts/DroneflyRegular-K78LA.ttf'

game_over_msg = Message(WIDTH//2, 300, 50, 'Game Over', game_over_font, WHITE, win)
score_msg = Message(WIDTH-50, 28, 30, '0', score_font, NAVY_BLUE, win)
final_score_msg = Message(300, 350, 30, '0', final_score_font, WHITE, win)
final_score1_msg = Message(150, 350, 25, 'Your score : ', final_score1_font, WHITE, win)
maximum_score_msg = Message(330, 400, 30, '0', maximum_score_font, WHITE, win)
maximum_score1_msg = Message(150, 400, 25, 'Your max_score : ', maximum_score1_font, WHITE, win)
coin_msg = Message(70, 70, 25, '0', coin_font, WHITE, win)
coin1_msg = Message(210, 440, 25, '0',maximum_score_font, WHITE, win)
total_coin_msg = Message(115, 70, 25, 'Total coin :', total_coin_font, WHITE, win)
total_coin1_msg = Message(300, 70, 25, '0',total_coin1_font, WHITE, win)
plane1_msg = Message(275, 100, 18, 'Spitfire Mk.XIVe',total_coin_font, WHITE, win)
plane1_1_msg = Message(280, 120, 25, '(British)',total_coin_font, WHITE, win)
plane2_msg = Message(275, 300, 23, 'P-47D-28',total_coin_font, WHITE, win)
plane2_1_msg = Message(275, 320, 25, '(U.S.A)',total_coin_font, WHITE, win)
plane3_msg = Message(275, 500, 23, 'P-51D-30',total_coin_font, WHITE, win)
plane3_1_msg = Message(275, 520, 25, '(U.S.A)',total_coin_font, WHITE, win)

#사운드

plyaer_bullet_fx = pygame.mixer.Sound('Assets/Sounds/gunshot.mp3')
click_fx = pygame.mixer.Sound('Assets/Sounds/click.mp3')
collision_fx = pygame.mixer.Sound('Assets/Sounds/mini_exp.mp3')
blast_fx = pygame.mixer.Sound('Assets/Sounds/blast.wav')
fuel_fx = pygame.mixer.Sound('Assets/Sounds/fuel.wav')
plane_fx = pygame.mixer.Sound('Assets/Sounds/plane.mp3')

pygame.mixer.music.load('Assets/Sounds/main_bgm.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


#이미지

health_img = pygame.image.load('Assets/health.png')
health_img = pygame.transform.scale(health_img, (20,20))

fuel_img = pygame.image.load('Assets/fuel.png')
fuel_img = pygame.transform.scale(fuel_img, (20,20))

coin_img = pygame.image.load('Assets/coin.png')
coin_img = pygame.transform.scale(coin_img, (40,40))

clouds_img = pygame.image.load('Assets/clouds.png')
clouds_img = pygame.transform.scale(clouds_img, (WIDTH, 350))

logo_img = pygame.image.load('Assets/logo.png')
logo_img = pygame.transform.scale(logo_img, (350, 200))

start_img = pygame.image.load('Assets/buttons/start.png')
start_img = pygame.transform.scale(start_img, (120, 90))

tutorial_img = pygame.image.load('Assets/buttons/tutorial.png')
tutorial_img = pygame.transform.scale(tutorial_img, (120, 90))

shop_img = pygame.image.load('Assets/buttons/shop.png')
shop_img = pygame.transform.scale(shop_img, (120, 90))

exit_img = pygame.image.load('Assets/buttons/exit.png')
exit_img = pygame.transform.scale(exit_img, (120, 90))

exit1_img = pygame.image.load('Assets/buttons/exit.png')
exit1_img = pygame.transform.scale(exit1_img, (120, 90))

exit2_img = pygame.image.load('Assets/buttons/exit.png')
exit2_img = pygame.transform.scale(exit2_img, (120, 90))

exit3_img = pygame.image.load('Assets/buttons/exit.png')
exit3_img = pygame.transform.scale(exit3_img, (120, 90))

restart_img = pygame.image.load('Assets/buttons/restart.png')
restart_img = pygame.transform.scale(restart_img, (90, 90))

mbg_img = pygame.image.load('Assets/mbg.png')

tutorial1_img = pygame.image.load('Assets/tutorial1.png')

store_img = pygame.image.load('Assets/store.png')

choice_img = pygame.image.load('Assets/buttons/choice.png')
choice_img = pygame.transform.scale(choice_img, (70, 50))
choice1_img = pygame.image.load('Assets/buttons/choice.png')
choice1_img = pygame.transform.scale(choice1_img, (70, 50))
choice2_img = pygame.image.load('Assets/buttons/choice.png')
choice2_img = pygame.transform.scale(choice2_img, (70, 50))

price1_img = pygame.image.load('Assets/price1.png')
price1_img = pygame.transform.scale(price1_img, (120, 90))

price2_img = pygame.image.load('Assets/price2.png')
price2_img = pygame.transform.scale(price2_img, (120, 90))



#버튼

start_btn = Button(start_img, (120,90),140, 270)
tutorial_btn = Button(tutorial_img, (120,90),140, 370)
shop_btn = Button(shop_img, (120,90),140, 470)
exit_btn = Button(exit_img, (120,90),140, 570)

restart_btn = Button(restart_img, (90,90),80,470)
exit1_btn = Button(exit1_img, (90,90), 230,470)

choice_btn = Button(choice_img, (70,50),102,230)
choice1_btn = Button(choice1_img, (70,50),102,420)
choice2_btn = Button(choice2_img, (70,50),102,610)

exit2_btn = Button(exit2_img, (90,90), 300,600)

exit3_btn = Button(exit3_img, (90,90), 300,600)

#오브젝트

bg = Background(win)
p = Player(200, HEIGHT - 70, 4)


enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
healthup_group = pygame.sprite.Group()




def shoot_bullet():
     x, y = p.rect.center[0], p.rect.y
     b= Bullet(x-30, y, p.type)
     player_bullet_group.add(b)
     b= Bullet(x+30, y, p.type)
     player_bullet_group.add(b)
     plyaer_bullet_fx.play()
     
#리셋 함수
def reset():
    enemy_group.empty()
    player_bullet_group.empty() 
    enemy_bullet_group.empty() 
    explosion_group.empty() 
    fuel_group.empty() 
    healthup_group.empty()

    p.reset(p.x, p.y)
    
level = 1
score = 0
max_score = 0
Coin = 0
total_coin = 0
plane_destroy_count = 0
plane_frequency = 3000
start_time = pygame.time.get_ticks()

player2_plane = False
player3_plane = False

moving_left = False
moving_right = False

home_page = True
game_page = False
tutorial_page = False
shop_page = False
ending_page = False

#게임 루프 및 프레임 설정

running = True
while running:
  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN: # q 누르면 게임 종료
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
        #조작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True

            if event.key == pygame.K_d:
                moving_right = True

            if event.key == pygame.K_SPACE:
                shoot_bullet()
                
        if event.type == pygame.KEYUP:
            moving_left = False
            moving_right = False
            
        
                
    #메인화면 페이지
    if home_page:
        win.blit(mbg_img, (0,0))
        win.blit(logo_img, (30, 10))
        win.blit(start_img, (140, 270))
        win.blit(tutorial_img, (140, 370))
        win.blit(shop_img, (140, 470))
        win.blit(exit_img, (140, 570))

    
        
        if start_btn.draw(win):
            home_page = False
            game_page = True
            click_fx.play()

        if tutorial_btn.draw(win):
            tutorial_page = True
            home_page = False
            click_fx.play()

        if shop_btn.draw(win):
            home_page = False
            shop_page = True
            click_fx.play()

        if exit_btn.draw(win):
            click_fx.play()
            running= False

    #튜토리얼 페이지 
    if tutorial_page:
        win.blit(tutorial1_img, (0,0))
        

        if exit2_btn.draw(win):
            click_fx.play()
            tutorial_page =False
            home_page = True
        
    #엔딩 페이지 
    if ending_page:
        
        
        if score > max_score:
            max_score = score
        
        win.blit(mbg_img,(0, 0))
        win.blit(logo_img, (30, 10))
        win.blit(coin_img, (140, 420))
        
        game_over_msg.update()
        final_score_msg.update(score)
        final_score1_msg.update()
        maximum_score_msg.update(max_score)
        maximum_score1_msg.update()
        coin1_msg.update(Coin)

       

        if exit1_btn.draw(win):
            click_fx.play()
            ending_page = False
            game_page = False
            home_page = True
            reset()

            total_coin += Coin
            plane_destory_count = 0
            level = 1
            score = 0
            Coin = 0
 
        if restart_btn.draw(win):
            click_fx.play()
            ending_page = False
            game_page = True
            reset()
            
            total_coin += Coin
            plane_destory_count = 0
            level = 1
            score = 0
            Coin = 0
    
    #스토어 페이지
    if shop_page:
        win.blit(store_img, (0, 0))
        win.blit(choice_img, (102, 230))
        win.blit(choice1_img, (102, 420))
        win.blit(choice2_img, (102, 610))
        win.blit(price1_img, (220, 330))
        win.blit(price2_img, (220, 530))
        total_coin_msg.update()
        total_coin1_msg.update(total_coin)
        plane1_msg.update()
        plane1_1_msg.update()
        plane2_msg.update()
        plane2_1_msg.update()
        plane3_msg.update()
        plane3_1_msg.update()

        if choice_btn.draw(win):
            click_fx.play()
            p = Player(200, HEIGHT - 70, 4)

        if choice1_btn.draw(win):
            click_fx.play()
            if total_coin >= 150 and player2_plane == False:
                player2_plane = True
                p = Player(200, HEIGHT - 70, 5)
                total_coin -= 150
                print(total_coin)

            if player2_plane == True:
                p = Player(200, HEIGHT - 70, 5)
                
                
        if choice2_btn.draw(win):
             click_fx.play()
             if total_coin >= 300 and player3_plane == False:
                 player3_plane = True
                 p = Player(200, HEIGHT - 70, 6)
                 total_coin -= 300
                

             if player3_plane == True:
                 p = Player(200, HEIGHT - 70, 6)     
            

        if exit3_btn.draw(win):
            click_fx.play()
            shop_page = False
            home_page = True
        

    #인게임 페이지 
    if game_page:
        current_time = pygame.time.get_ticks()
        delta_time = current_time - start_time
        if delta_time >= plane_frequency:
            #레벨 시스템
            if level == 1:
                type = 1
            if level == 2:
                type = random.randint(1,2)
            if level == 3:
                type = 2
            if level == 4:
                type = random.randint(2,3)
            if level == 5:
                type = 3
                
            x = random.randint(10, WIDTH - 100)
            e = Enemy(x, -150, type)
            enemy_group.add(e)
            plane_fx.play()
            start_time = current_time
           
        if plane_destroy_count:
            if plane_destroy_count % 7 ==0 and level <= 5:
                level += 1
                plane_destroy_count += 1
    #배경 업데이트
        bg.update(3)
        win.blit(clouds_img, (0, 70))
    
    #총알 업데이트
        player_bullet_group.update()
        player_bullet_group.draw(win)
        enemy_bullet_group.update()
        enemy_bullet_group.draw(win)
    
    #폭발 업데이트
        explosion_group.update()
        explosion_group.draw(win)
    
    #적 업데이트 
        enemy_group.update(enemy_bullet_group, explosion_group)
        enemy_group.draw(win)
    
    #연료 아이템  업데이트
        p.fuel -= 0.05
        fuel_group.update()
        fuel_group.draw(win)

    #체력 추가 아이템 업데이트
        healthup_group.update()
        healthup_group.draw(win)
    
    
    #캐릭터 업데이트
        p.update(moving_left,moving_right, explosion_group)
        p.draw(win)
        
        if p.alive:
                
           player_hit = pygame.sprite.spritecollide(p, enemy_bullet_group, False)
           for bullet in player_hit:
              p.health -= bullet.damage
              print(p.health)

              x, y = bullet.rect.center
              explosion = Explosion(x, y, 1)
              explosion_group.add(explosion)
        
              bullet.kill()
              collision_fx.play()
        
    #총알 피격시 폭발 
           for bullet in player_bullet_group:
               planes_hit = pygame.sprite.spritecollide(bullet, enemy_group, False)
               for plane in planes_hit:
                   plane.health -= bullet.damage
                   #연료 추가 
                   if plane.health <=0:
                       x, y =plane.rect.center
                       rand = random.random()
                       if rand >= 0.9:
                           health = HealthUp(x, y)
                           healthup_group.add(health)
                        
                       elif rand >= 0.3:
                           fuel = Fuel(x,y)
                           fuel_group.add(fuel)

                       plane_destroy_count +=1
                       blast_fx.play()
                       score += e.score
                       Coin += e.coin
                       

                   x, y = bullet.rect.center
                   explosion = Explosion(x, y, 1)
                   explosion_group.add(explosion)
    
                   bullet.kill()
                   collision_fx.play()

    #플레이어 충돌시 폭발
           player_collide = pygame.sprite.spritecollide(p, enemy_group, True)
           if player_collide:
        
               x, y = p.rect.center
               explosion = Explosion(x, y, 2)
               explosion_group.add(explosion)

               x, y = player_collide[0].rect.center
               explosion = Explosion(x, y, 2)
               explosion_group.add(explosion)
        
               p.health -= 10
               blast_fx.play()


           if pygame.sprite.spritecollide(p, fuel_group, True):
               p.fuel += 5
               if p.fuel >= p.fuel_max:
                   p.fuel = p.fuel_max
               fuel_fx.play()
        
           if pygame.sprite.spritecollide(p, healthup_group, True):
               p.health += 20
               if p.health >= p.health_max:
                    p.health = p.health_max
               fuel_fx.play()

        if not p.alive or p.fuel <= -10:
            if len(explosion_group) == 0:
                game_page = False
                ending_page = True

                reset()
        score += 1
        score_msg.update(score)
        coin_msg.update(Coin)
        
        
    #체력 UI
        health_color = YELLOW if p.health <= p.health_max / 2 else ORANGE
        pygame.draw.rect(win, health_color,(30, 20, p.health, 10), border_radius = 4)
        pygame.draw.rect(win, WHITE,(30, 20, p.health_max, 10), 2, border_radius = 4)
    #연료 UI
        fuel_color = RED if p.fuel <= p.fuel_max / 3 else GRAY
        pygame.draw.rect(win, fuel_color,(30, 32, p.fuel, 10), border_radius = 4)
        pygame.draw.rect(win, WHITE,(30, 32, p.fuel_max, 10), 2, border_radius = 4)

        win.blit(health_img, (8,8))
        win.blit(fuel_img, (8,28))
        win.blit(coin_img, (8, 50))
       
    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT),5, border_radius = 5 )
    clock.tick(FPS)
    pygame.display.update()
     
pygame.quit()

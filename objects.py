import pygame

SCREEN = WIDTH, HEIGHT = 400, 700

pygame.mixer.init()

# 배경 클래스(배경 관련된 것을 총괄)

class Background():
    def __init__(self, win):
        self.win = win

        self.image = pygame.image.load('Assets/bg.png')
        self.image = pygame.transform.scale(self.image,(WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        
        self.reset()
        self.move = True
    #배경이 밑으로 이동하게끔 만드는 함수
    def update(self, speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed

            if self.y1 >= HEIGHT:
                self.y1 = -HEIGHT
            if self.y2 >= HEIGHT:
                self.y2 = -HEIGHT

        self.win.blit(self.image,(self.x,self.y1))
        self.win.blit(self.image,(self.x,self.y2))
        
    #리셋 함수, 배경이 밑으로 내려가면 다시 위로 올림.
    def reset(self):
        self.x = 0
        self.y1 = 0
        self.y2 = -HEIGHT
        
# 플레이어 클래스

class Player():
    #플레이어 이미지 디폴트 
    def __init__(self, x, y,type_):
        self.image_list = [ ]
        self.type=type_
        
        for i in range(2):
           if type_ == 4:
                img = pygame.image.load(f'Assets/Players/player1.png')
                self.health = 60
                self.health_max = 60
                self.fuel = 60
                self.fuel_max = 60
                self.price = 0
                
                
           if type_ == 5:
                img = pygame.image.load(f'Assets/Players/player2.png')
                self.health = 100
                self.health_max = 100
                self.fuel = 80
                self.fuel_max = 80
                self.price = 150

           if type_ == 6:
                img = pygame.image.load(f'Assets/Players/player3.png')
                self.health = 140
                self.health_max = 140
                self.fuel = 100
                self.fuel_max = 100
                self.price = 300

          #플레이어 이미지 스케일 조정
           w, h = img.get_width(), img.get_height()
           height = (100*h)// w
           img = pygame. transform.scale(img, (100,height))
            
           self.image_list.append(img)

           self.x = x
           self.y = y
           self.reset(self.x, self.y)
           
    def reset(self, x, y):
        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(center = (x, y))
        self.health = self.health_max
        self.fuel = self.fuel_max
        self.speed = 5
        self.alive = True
        self.width = self.image.get_width()
        

        
    #플레이어 위치 업데이트 함수
    def update(self,moving_left, moving_right, explosion_group):
        
        if self.alive:
            if moving_left and self.rect.x > 2:
                self.rect.x -= self.speed

            if moving_right and self.rect.x  < WIDTH - self.width:
                self.rect.x += self.speed


            if self.health <= 0:
                self.alive = False
                x, y = self.rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)
          
        
    #플레이어 그리는 함수
    def draw(self, win):
        if self.alive:
            win. blit(self.image, self.rect)
        

    
#적 클래스
        
class Enemy(pygame.sprite.Sprite):
    #적 이미지 디폴트 
    def __init__(self, x, y,type_):

        super(Enemy, self).__init__()

        self.type=type_
        self.image_list = [ ]
        for i in range(2):

           if type_ == 1:
                img = pygame.image.load(f'Assets/Enemies/enemy1.png')
                self.health = 100
                self.score = 100
                self.coin = 1
                
           if type_ == 2:
                img = pygame.image.load(f'Assets/Enemies/enemy2.png')
                self.health = 140
                self.score = 300
                self.coin = 3

           if type_ == 3:
                img = pygame.image.load(f'Assets/Enemies/enemy3.png')
                self.health = 200
                self.score = 500
                self.coin = 5

          #적 이미지 스케일 조정
           w, h = img.get_width(), img.get_height()
           height = (100*h)// w
           img = pygame. transform.scale(img, (100,height))
            
           self.image_list.append(img)


        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed=5
        self.width = self.image.get_width()
        self.bullet_counter=0
        # 죽고나서도 계속 비행기 소리가 플레이 되서 main 파일로 끌고 감.
        #if self.type in (1, 2, 3):
            #self.fx = pygame.mixer.Sound('Assets/Sounds/plane.mp3')

        #self.fx.play(-1)
            
    def enemy_shoot(self, enemy_bullet_group):
        if self.type in (1, 2):
            x, y = self.rect.center
            b = Bullet(x, y, self.type)
            enemy_bullet_group.add(b)

        if self.type in [3]:
            x, y = self.rect.center
            b = Bullet(x-25, y, self.type)
            enemy_bullet_group.add(b)
            b = Bullet(x+25, y, self.type)
            enemy_bullet_group.add(b)
        
            
        
    #적 위치 업데이트 함수
    def update(self,enemy_bullet_group, explosion_group):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.kill()

        if self.health <= 0:
            x, y = self.rect.center
            explosion = Explosion(x, y, 2)
            explosion_group.add(explosion)
           
            self.kill()
            
          

        self.bullet_counter += 1
        if self.bullet_counter >=60:
            self.enemy_shoot(enemy_bullet_group)
            self.bullet_counter = 0
        pass
    #적 그리는 함수
    def draw(self, win):
        win. blit(self.image, self.rect)

#총알 클래스
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, type_):
        super(Bullet, self).__init__()

        #적 총알
        if type_ == 1:
            self.image = pygame.image.load('Assets/Bullets/1.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed = 10
        if type_ == 2:
            self.image = pygame.image.load('Assets/Bullets/2.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed = 10
        if type_ == 3:
            self.image = pygame.image.load('Assets/Bullets/3.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed = 10
        #플레이어 총알
        if type_ == 4:
            self.image = pygame.image.load('Assets/Bullets/4.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed= -10
            
        if type_ == 5:
            self.image = pygame.image.load('Assets/Bullets/5.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed= -10
            
        if type_ == 6:
            self.image = pygame.image.load('Assets/Bullets/6.png')
            self.image = pygame.transform.scale(self.image, (20,40))
            self.speed= -10
        
        self.rect = self.image.get_rect(center = (x, y))

        

        
        # 총알 데이터 구현하기
        self.damage_dict = {1:20, 2:30, 3:60, 4:20, 5:30, 6:60 }
        self.damage = self.damage_dict[type_]
        


    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom <= 0:
            self.kill()

        if self.rect.top >= HEIGHT:
            self.kill()

    def draw(win):
        win.blite(self.image, self.rect)


#폭발 클래스           
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, type_):
        super(Explosion, self).__init__()

        self.img_list =[]
        if type_ == 1:
            self.length = 3
        elif type_ == 2:
            self.length = 4
            
        for i in range(self.length):
            img = pygame.image.load(f'Assets/Explosion{type_}/{i+1}.png')
            w, h = img.get_size()
            width = int(w*0.40)
            height = int(w*0.40)
            img = pygame.transform.scale(img, (width, height))
            self.img_list.append(img)

        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect(center = (x, y))

        self.counter = 0

    def update(self):
        self.counter +=1
        if self.counter >= 7:
            self.index += 1
            
            if self.index >= self.length:
                self.kill()
            else:   
                self.image = self.img_list[self.index]
                self.counter = 0
       

    def draw(win):
        win.blite(self.image, self.rect)
            

#연료 아이템 클래스
class Fuel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Fuel,self).__init__()

        self.image = pygame.image.load('Assets/fuel.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        self.rect.y += 3
        if self.rect.top >= HEIGHT:
            self.kill()

    def draw(self, win):
        win.blit(self.image, self.rect)


# 체력 회복 아이템 클래스
class HealthUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(HealthUp,self).__init__()

        self.image = pygame.image.load('Assets/health.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        self.rect.y += 3
        if self.rect.top >= HEIGHT:
            self.kill()

    def draw(self, win):
        win.blit(self.image, self.rect)


#버튼 클래스
class Button(pygame.sprite.Sprite):
    def __init__(self, img, scale, x, y):
        super(Button, self).__init__()

        self.scale = scale
        self.image = pygame.transform.scale(img, self.scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False


    def update_image(self, img):
        self.image = pygame.transform.scale(img, self.scale)

    def draw(self, win):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        win.blit(self.image, self.rect)
        return action
    


class Message():
    def __init__(self, x, y, size, text, font, color, win):
        self.win = win
        self.color = color
        self.x , self.y = x, y

        if not font:
            self.font = pygame.font.SysFont('Verdana', size)
            anti_alias = True

        else :
            self.font = pygame.font.Font(font, size)
            anti_alias = False


        self.image = self.font.render(text, anti_alias, color)
        self.rect = self.image.get_rect(center = (x, y))
        self.shadow = self.font.render(text, anti_alias, (54, 69, 79))
        self.shadow_rect = self.image.get_rect(center = (x+2, y+2))

    def update(self, text = None, shadow = True):
        if text:
             self.image = self.font.render(f'{text}', False, self.color)
             self.rect = self.image.get_rect(center = (self.x, self.y))
             self.shadow = self.font.render(f'{text}', False, (54, 69, 79))
             self.shadow_rect = self.image.get_rect(center = (self.x+2, self.y+2))

        
        if shadow:
            self.win.blit(self.shadow, self.shadow_rect)
            
        self.win.blit(self.image, self.rect)
        





        

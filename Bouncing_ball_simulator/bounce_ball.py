import time, random, pygame

pygame.init()

screen = pygame.display.set_mode((1200,768))
background = pygame.image.load('bg.png')

pygame.display.set_caption('Симулятор прыгающего мяча')

class Ball:
    ball_image = pygame.image.load('ball1.jpeg')
    g = 1

    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=random.randint(0,1100)
        self.Y=random.randint(0,750)
    
    def render_ball(self):
        screen.blit(Ball.ball_image, (self.X, self.Y))
    
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY += Ball.g
        #changing position based on velocity
        self.X += self.velocityX
        self.Y += self.velocityY

        if self.X < 0 or self.X > 960:
            self.velocityX *= -1
        
        if self.Y < 0 and self.velocityY < 0:
            self.velocityY *= -1
            self.Y = 0

        if self.Y > 568 and self.velocityY > 0:
            self.velocityY *= -1
            self.Y = 568

ball_list = [Ball(), Ball(), Ball(), Ball(), Ball()]

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        
    time.sleep(0.02)
    screen.blit(background, (0,0))

    for ball_item in ball_list:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()

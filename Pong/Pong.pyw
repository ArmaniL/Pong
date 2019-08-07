import pygame
import sys
import random
width,height=500,400

#The class for the ball
class Ball:
 radius=10
 limitx=width-radius# The limit the ball has to hit the screen
 limity=height-radius
 vx,vy=0.15,0.15   #The vertical and horizontal velocity of the ball
 def __init__(self,x,y):
  self.x=x
  self.y=y
 def draw(self,display):  
  pygame.draw.circle(display,(255,255,255,255),(int(self.x),int(self.y)),Ball.radius)
	
 def update(self,paddle,opp_Paddle):
          self.x+=Ball.vx
          self.y+=Ball.vy
          if self.x<=Ball.radius: #Checks to see if the ball hit the left edge of the screen or is off the screen. It then increases opponent score and resets everything
           Ball.vx=0.15
           opp_Paddle.score+=1
           ball.x,ball.y=width/2,height/2
           Opp_Paddle.speed=random.uniform(0.01,0.2)
          elif self.x>=Ball.limitx: #Checks to see if the ball hit the right edge of the screen or is off the screen. It then increases player score and resets everything
             Ball.vx=-0.15
             paddle.score+=1
             ball.x,ball.y=width/2,height/2
             Opp_Paddle.speed=random.uniform(0.01,0.2)
          if self.y<=Ball.radius:#Checks to see that the ball is on the top of the screen and flips the velocity
          	 Ball.vy=0.15
          elif self.y>=Ball.limity: #Checks to see that the ball is on the bottom of the screen and flips the velocity
             Ball.vy=-0.15
          l=2*Ball.radius
          ball_hitbox=pygame.Rect(self.x-Ball.radius,self.y-Ball.radius,l,l)
          paddle_hitbox=pygame.Rect(paddle.x,paddle.y,Paddle.w,Paddle.h)
          opp_Paddle_hitbox=pygame.Rect(opp_Paddle.x,opp_Paddle.y,Opp_Paddle.w,Opp_Paddle.h)
          if (paddle_hitbox.colliderect(ball_hitbox)):#checks to see if the ball has collided with the players paddle
          	  Ball.vx=0.15
          if (opp_Paddle_hitbox.colliderect(ball_hitbox)):#checks to see if the ball has collided with the players paddle
          	  Ball.vx=-0.15
          	  


class Opp_Paddle:
 speed=0.1
 vy=0.1
 w=10
 h=50

 def __init__(self,x,y):
  self.x=x
  self.y=y
  self.score=0
 def draw(self,display):  
  pygame.draw.rect(display,(255,255,255,255),(self.x,self.y,Opp_Paddle.w,Opp_Paddle.h))
	
 def update(self,ball):
  #allows the opponents paddle to follow the ball but at diffrent speed so as to have variable diffculty
  y=self.y+Opp_Paddle.h/2
  if ball.y<y  :
   Opp_Paddle.vy=-Opp_Paddle.speed
  elif ball.y>y:
   Opp_Paddle.vy=Opp_Paddle.speed
  self.y+=Opp_Paddle.vy


class Paddle:
 vy=0
 basespeed=0.2
 w=10
 h=50
 limit=height-h #limit set to make sure no part of the players paddle goes off the screen
 def __init__(self,x,y,score=0):
  self.x=x
  self.y=y
  self.score=score
 def draw(self,display):  
  pygame.draw.rect(display,(255,255,255,255),(self.x,self.y,Paddle.w,Paddle.h))
	
 def update(self):
        #moves the playes paddle  
  	 	  self.y+=Paddle.vy
  	 	  if self.y<0:
  	 	  	  self.y=1
  	 	  elif self.y>Paddle.limit:
  	 	  	  self.y=Paddle.limit-1

  

paddle=Paddle(10,120)
opp_Paddle=Opp_Paddle(width-20,120)
ball=Ball(int(width/2),int(height/2))
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 20)
pygame.display.set_caption("Pong By Armani Weise")
DISPLAY=pygame.display.set_mode((width,height+50),0,32)
icon=pygame.Surface((32,32))#black square for icon
pygame.display.set_icon(icon)
DISPLAY.fill((1,1,1,255))
while True:
 textsurface = myfont.render("Player:{0}        Opponent:{1}".format(str(paddle.score),str(opp_Paddle.score)), False, (220, 220, 200))
 DISPLAY.fill((10,10,10,255))
 paddle.draw(DISPLAY)
 pygame.draw.line(DISPLAY,(255,255,255,230),(0,height),(width,height),2)#draws the bottom of the screen
 ball.draw(DISPLAY)
 opp_Paddle.draw(DISPLAY)
 DISPLAY.blit(textsurface,(30,height))
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
    pygame.quit()#quits the game 
    sys.exit(0)
  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_w or event.key==pygame.K_UP :#points the paddle upward if up or w is pressed
      if Paddle.vy<=-Paddle.basespeed:
      	   Paddle.vy-=1
      else:
           Paddle.vy= -Paddle.basespeed

    elif event.key==pygame.K_s or event.key==pygame.K_DOWN:#points the paddle downward if down or s is pressed
     if Paddle.vy>=Paddle.basespeed:
      	   Paddle.vy+=1
     else:
           Paddle.vy= Paddle.basespeed
       
  if event.type==pygame.KEYUP:
    if event.key==pygame.K_s or event.key==pygame.K_w or event.key==pygame.K_UP or event.key==pygame.K_DOWN :#resets the velocity to zero in the cae that no button is pressed
     Paddle.vy=0	
 
 paddle.update()
 ball.update(paddle,opp_Paddle)
 opp_Paddle.update(ball)
 pygame.display.flip()

import pygame

class Obstacle():
    """障碍物精灵"""
    def __init__(self,screen,speed=1):
        #初始化障碍物并设置其起始位置
        
        
        self.screen = screen
      
        
        
        
        
        self.obstacle = pygame.image.load('images/obstacle.bmp').convert_alpha()
        self.obstacle_width,self.obstacle_height=self.obstacle.get_size()
        self.obstacle_rect = self.obstacle.get_rect()
       
       
       
        # 每个障碍物最初都在屏幕右下角附近
       

        
        
        self.obstacle_speed = speed
        
    
    
        #设置向左的移动标志
        self.obstacle_moving_left=True
        
        
        
    def obstacleblit(self):
        """ 在指定位置绘制障碍物"""
        self.screen.blit(self.obstacle,(2000-self.obstacle_width,1000-self.obstacle_height))
        
    def obstacledate(self):
        """根据移动位置调整障碍物位置"""
        #在屏幕水平方向上移动
        if self.obstacle_moving_left:
            self.obstacle_rect.centerx-= self.obstacle_speed
            
    
            
      
        
        
            
"""class Background(Obstacle):
 
    
    def backgrounddate(self):
        
        #判断是否移出屏幕，若移出屏幕，应该将图像设置到图像右边
        if self.obstacle_rect.x<0:
            self.obstacle_rect.x = self.obstacle_rect.width
            
            
    def createSprites(self):

        #创建背景精灵和精灵组
        
         
        self.backGround = pygame.image.load('images/backend.bmp').convert_alpha()
        self.backGround_rect = self.backGround.get_rect()
        
        
    def backGroundSpritesblit(self):
       
        self.screen.blit(self.backGround, self.backGround_rect)
       """ 
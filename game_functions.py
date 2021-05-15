import sys
from turtle import back
from  sprites import Obstacle

import pygame

          
def check_events(ship,obstacle):
    """响应障碍物的鼠标事件"""
    """响应背景和鼠标事件"""
    
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                #向左移动障碍物
                obstacle_moving_left=True
                
                
            
    
        # 按下一个键代表开
        # 按下与松开不同的键，代表了人物的不同状态
            if event.key==pygame.K_UP:
                #向上移动人物
                ship.moving_up=True
            if event.key==pygame.K_DOWN:
                #向下移动人物
                ship.moving_down=True
            
        elif event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    ship.moving_up=False 
                if event.key==pygame.K_DOWN:
                    ship.moving_down=False
                
                       
def update_screen(role_settings,screen,ship,backend,obstacle,obstacles):
    """更新屏幕上的图片并切换到新屏幕"""
    #每次循环时都重新绘制屏幕
    screen.fill(role_settings.bg_color)
    #调用绘制人物的函数,在这之前要创建一个实例
    
    
    
    for obstacle in obstacles:
        obstacle.draw_obstacle()
    
    #ship 是实例化的人物
    backend.blitBackend()
    
    ship.blitme()
    ship.update()
    
    
    
    #obstacle是实例化的障碍物
    obstacle.obstacleblit()
    obstacle.obstacledate()
    
    
    
    #一群实例化的障碍物obstacles.draw在屏幕上绘制编组中的每个障碍物
    obstacles.draw(screen)
    
    
    #background是实例化的移动背景
    
    
    
    
    pygame.display.flip()


def create_obstacles(role_settings, screen, obstacles):  
    obstacle= Obstacle(role_settings, screen)
    obstacle.width=obstacle.obstacle_width
    available_space_x=role_settings.screen_width-2*obstacle.width
    number__obstacle_x=int(available_space_x/(2*obstacle.width))
    for alien_number in range(number__obstacle_x):
        obstacle= Obstacle(role_settings, screen)
        

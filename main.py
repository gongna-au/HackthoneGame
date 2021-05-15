

import pygame 
from pygame.sprite import Group



from settings import Settings
from ship import Ship
from ship import BackendImage
from sprites import Obstacle


import game_functions as gf



def run_game():
    pygame.init()
    
    
    
    #创建一群障碍物
    obstacles=Group()
    
    
    
    #角色设置的实例化
    role_settings=Settings()
    
    
    screen=pygame.display.set_mode((role_settings.screen_width,role_settings.screen_height),)
    
    screen =pygame.display.set_mode((2000,1000))
    
    pygame.display.set_caption("天天跑酷")
   
    
    #创建一个背景
    backend=BackendImage(screen)
    
    #创建一个实例化的人物
    
    ship=Ship(screen,role_settings) 
    
    #创建障碍物的实例
    obstacle=Obstacle(screen)
    
    
    #创建移动背景的实例
    
    
    
    
   
    while True:
        #调用game_functions模块的check_events实现对事件的监听
        gf.check_events(ship,obstacle)
        gf.update_screen(role_settings,screen,ship,backend,obstacle,obstacles)
        gf.create_obstacles(role_settings, screen, obstacles)
        
        #调用绘制人物的函数,在这之前要创建一个实例
        #ship 是实例化的人物
        #backend 是实例化的背景
        #obstacle 是实例化的障碍物
        #background 是实例化的移动背景
        
        

run_game()
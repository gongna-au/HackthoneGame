
import pygame 
from settings import Settings
from ship import Ship
from ship import BackendImage
import game_functions as gf

def run_game():
    pygame.init()
    
    #角色设置的实例化
    role_settings=Settings()
    
    screen=pygame.display.set_mode((role_settings.screen_width,role_settings.screen_height),)
    
    screen =pygame.display.set_mode((2000,1000))
    
    pygame.display.set_caption("天天跑酷")
   
    
    #创建一个背景
    backend=BackendImage(screen)
    
    #创建一个实例化的人物
    ai_settings=1.5
    ship=Ship(screen,ai_settings)
    
  
    
    
    
    while True:
        #调用game_functions模块的check_events实现对事件的监听
        gf.check_events(ship)
        gf.update_screen(role_settings,screen,ship,backend)
        
        
        #调用绘制人物的函数,在这之前要创建一个实例
        #ship 是实例化的人物

run_game()
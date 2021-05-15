import sys

import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        # 按下与松开不同的键，代表了人物的不同状态
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            
                
    
            
            
def update_screen(role_settings,screen,ship,backend):
    """更新屏幕上的图片并切换到新屏幕"""
    
    #每次循环时都重新绘制屏幕
    screen.fill(role_settings.bg_color)
    #调用绘制人物的函数,在这之前要创建一个实例
    #ship 是实例化的人物
    backend.blitBackend()
    ship.blitme()
    pygame.display.flip()

    
    
    
    
import pygame

class Ship():
    
    def __init__(self,screen):
        """初始化设置人物的位置"""
        # 加载人物图像并获取其外接矩形,变量screen、image
        self.screen=screen
        self.screen_rect =self.screen.get_rect()

    
        
        
        #缩小人物照片
        #pygame.image.load('images/manRole.bmp').convert_alpha()
        #convert_alpha相对于convert，保留了图像的Alpha 通道信息，可以认为是保留了透明的部分，实现了透明转换
        self.man=pygame.image.load('images/manRole.bmp').convert_alpha()
        self.man_width,self.man_height=self.man.get_size()
        self.man=pygame.transform.smoothscale(self.man,(self.man_width//5,self.man_height//5))
        self.man_rect=self.man.get_rect()
        
        #将人物放在屏幕左下角
        self.man_rect.centerx=self.screen_rect.centerx
        self.man_rect.bottom=self.screen_rect.bottom
        self.man_rect.left=self.screen_rect.left
        
    def blitme(self):
        """在指定位置绘制人物"""
        self.screen.blit(self.man,self.man_rect)
        
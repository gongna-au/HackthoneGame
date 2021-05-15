import pygame
class BackendImage():
    def __init__(self,screen):
        """设计背景的初始位置"""
        # 加载背景图像并获取其外接矩形,变量screen、image
        self.screen=screen
        self.screen_rect =self.screen.get_rect()
        
        
        
        #将背景照片设计为与screen相同的尺寸大小
        self.backend=pygame.image.load('images/backend.bmp').convert_alpha()
        self.backend_width,self.backend_height=self.backend.get_size()
        self.backend=pygame.transform.smoothscale(self.backend,(self.backend_width*2,self.backend_height*2))
        self.backend_rect=self.backend.get_rect()
        #将背景放在合适的地方
        self.backend_rect.centerx=self.screen_rect.centerx
        self.backend_rect.bottom=self.screen_rect.bottom
        self.backend_rect.left=self.backend_rect.left
       
        
    def blitBackend(self):
        self.screen.blit(self.backend,self.backend_rect)
        


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



from wsgiref.util import setup_testing_defaults


class Settings():
    """存储所有的类"""
    def __init__(self):
        """初始化"""
        # 屏幕设置
        self.screen_width=2000
        self.screen_height=1000
        self.bg_color=(111,111,111)
        self.ship_speed_factor=1.5
        # 背景设置
        self.backend_speed_factor = 1
        self.backend_width = 2000
        self.backend_height= 1000

        
        
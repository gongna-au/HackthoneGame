from wsgiref.util import setup_testing_defaults


class Settings():
    """存储所有的类"""
    def __init__(self):
        """初始化"""
        # 屏幕设置
        self.screen_width=2000
        self.screen_height=1000
        self.bg_color=(0,245,225)
    
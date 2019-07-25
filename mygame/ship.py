# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:45:13 2018

@author: zhangyushun
"""

import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen=screen#屏幕的实例
        self.ai_settings=ai_settings#设置的实例
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load("C:\\Users\\ZYS\\Desktop\\python_learning\\mygame\\images\\ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #将每艘新的飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom       
        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)
        #移动标志
        self.moving_right=False
        self.moving_left=False
       
    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right<self.screen_rect.right:#只要标志位为真就一直移位
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:#只要标志位为真就一直移位
            self.center-=self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx=self.center
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """将飞船放置屏幕中央"""
        self.center=self.screen_rect.centerx
        
        
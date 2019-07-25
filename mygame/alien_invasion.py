# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:53:32 2018

@author: zhangyushun
"""

import sys
sys.path.append('C:\\Users\\zhangyushun\\Desktop\\python_learning\\mygame')
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init() 
    #screen = pygame.display.set_mode((1200, 800))
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    play_button=Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #设置背景色
    #bg_color=(230,230,230)
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    
    #创建一个用于存储子弹的编组
    bullets=Group()
    
    
    #创建一个外星人
    #alien=Alien(ai_settings,screen)
    #创建一个外星人编组
    aliens=Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏的主循环
    while True:
    # 监视键盘和鼠标事件
#      for event in pygame.event.get(): 
#          if event.type == pygame.QUIT:
#              pygame.quit()
#              sys.exit()
      #gf.check_events(ship)
      gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)   
      if stats.game_active:          
          ship.update()#根据事件的变换在update中更新ship的位置
    
        # 每次循环是都重绘屏幕
          #screen.fill(bg_color)
    #      screen.fill(ai_settings.bg_color)
    #      ship.blitme()
          gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
          gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
      gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
          
        # 让最近绘制的屏幕可见
          #pygame.display.flip()
run_game()


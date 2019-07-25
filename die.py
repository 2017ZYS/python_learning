# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:24:31 2018

@author: zhangyushun
"""

from random import randint

class Die():
    """表示一个筛子的类"""
    def __init__(self, num_sides=6):
        """筛子默认为6面"""
        self.num_sides=num_sides
        
    def roll(self):
        """返回一个位于1和筛子面数之间的随机值"""
        return randint(1,self.num_sides)

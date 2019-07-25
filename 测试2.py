# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:40:49 2017

@author: zhangyushun
"""
import numpy as np
import matplotlib.pyplot as plt

greyhounds=500
labs=500

grey_height =28 + 4 * np.random.randn(greyhounds)
lab_height =24 + 4 * np.random.randn(labs)

plt.hist([grey_height,lab_height],stacked=True,color=['r','b'])

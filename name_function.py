# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:04:12 2018

@author: zhangyushun
"""

def get_formatted_name(first,last):
    """Gennerate a neatly formatted full name."""
    full_name=first+' '+last
    return full_name.title()
get_formatted_name('janis','joplin')
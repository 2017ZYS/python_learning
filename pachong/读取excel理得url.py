# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:57:24 2019

@author: ZYS
"""
#读取excel文档
import openpyxl as xl
wb=xl.load_workbook("exportData.xlsx")#workbook数据类型
type(wb)

a=wb.sheetnames#工作簿中所有表（sheet）名得列表

sheet=wb.get_sheet_by_name("")

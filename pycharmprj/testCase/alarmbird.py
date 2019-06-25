# !/usr/bin/env python3
# -*-coding:utf-8-*-
# author:super


# from module import *
# from package.module import *

'''
智能小管家1.0
功能1：本地天气、气温
功能2：定时任务提醒、新建提醒（时间、地点、事项）
功能3：每日要事流程、习惯强化
功能4：
'''

import time  # module time

# 学习各个module的使用方法记录下来，可根据【关键字】进行查询


def m_find():
	key=0
	print('请输入所有查找的模块名称：\n')
	key=int(input())
	if key == 0:
		m_time()
		print('Hi，First keywords is blank.')
	else:
		print('warning, input error!')


def m_time():
	print('''
	# contents
	
	''')


if __name__ == '__main__':
	m_find()
	print("智能小管家1.0")


import cv2
import pyautogui
import time
import aircv as ac
import numpy as np
import ops_util
import screen
import gcf
import logging

MINI_MAP_SLOT_SIZE = 18
MINI_MAP_SLOT_COUNT = 7
FINISH_MODE_MINI_MAP= 'MINI_MAP'
FINISH_MODE_DOOR = 'DOOR'
FINISH_MODE_QUESTION= 'QUESTION'
FINISH_MODE_BOSS= 'BOSS'
FINISH_MODE_UPGATE= 'UPGATE'

HOME_X=500
HOME_Y=470

SPEED_X=140
SPEED_Y=110

MINI_MAP_X=793
MINI_MAP_Y=29

FIGHT_UP=230
FIGHT_DOWN=424
FIGHT_MIDDLE=327
FIGHT_MIDDLE=440

ITEM_X=489
ITEM_Y=277
ITEM_SIZE=30

# xy = (667, 29, 126, 126)

MY_IMG = None

PAD1 = cv2.imread(ops_util.resource_path('task', 'fill1.png'))
QUESTION = cv2.imread(ops_util.resource_path('task', 'wenhao.png'))
ME = cv2.imread(ops_util.resource_path('task', 'me.png'))
ME18 = cv2.imread(ops_util.resource_path('task', 'me18.png'))
ME4X10 = cv2.imread(ops_util.resource_path('task', 'me4x10.png'))
FINAL = cv2.imread(ops_util.resource_path('task', 'final.png'))
TASK_JIANQI = cv2.imread(ops_util.resource_path('task', 'jianqi.png'))
TASK_JIANQI2 = cv2.imread(ops_util.resource_path('task', 'jianqi2.png'))
ITEM = cv2.imread(ops_util.resource_path('task', 'ic.png'))
ITEM_USED = cv2.imread(ops_util.resource_path('item', 'chuandai.png'))
ITEM_SWITCHED = cv2.imread(ops_util.resource_path('item', 'switch.png'))
ITEM_XIYOU = cv2.imread(ops_util.resource_path('item', 'xiyou.png'))
ITEM_XIYOU2 = cv2.imread(ops_util.resource_path('item', 'xiyou2.png'))
ITEM_WODE = cv2.imread(ops_util.resource_path('item', 'wode.png'))
ITEM_FENJIE0 = cv2.imread(ops_util.resource_path('item', 'fenjie0.png'))
ITEM_FENJIE = cv2.imread(ops_util.resource_path('item', 'fenjie.png'))
ITEM_FENJIE1 = cv2.imread(ops_util.resource_path('item', 'fenjie1.png'))
ITEM_SPACE = cv2.imread(ops_util.resource_path('item', 'click_space.png'))
ITEM_QUANBUFENJIE = cv2.imread(ops_util.resource_path('item', 'quanbufenjie.png'))
ITEM_PAGE = cv2.imread(ops_util.resource_path('item', 'item_page.png'))


ITEM_LEFT = cv2.imread(ops_util.resource_path('item', 'left.png'))
ITEM_RIGHT = cv2.imread(ops_util.resource_path('item', 'right.png'))
ITEM_DOWN = cv2.imread(ops_util.resource_path('item', 'down.png'))
ITEM_UP = cv2.imread(ops_util.resource_path('item', 'up.png'))
ITEM_UP11 = cv2.imread(ops_util.resource_path('item', 'up1.1.png'))

SKILL_PAGE = cv2.imread(ops_util.resource_path('item', 'skill_page.png'))
SKILL_LEARN = cv2.imread(ops_util.resource_path('item', 'skill_learn.png'))


ITEM_XIULI = cv2.imread(ops_util.resource_path('item', 'xiuli.png'))
ITEM_XIULI1 = cv2.imread(ops_util.resource_path('item', 'xiuli1.png'))

TASK_JIEJIN = cv2.imread(ops_util.resource_path('task', 'task_jiejin.png'))
TASK_CLOSE = cv2.imread(ops_util.resource_path('task', 'task_close.png'))


CLEAR_CONFIRM = cv2.imread(ops_util.resource_path('clear', 'confirm.png'))

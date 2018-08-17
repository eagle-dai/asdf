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

ITEM_X=489
ITEM_Y=277
ITEM_SIZE=30

# xy = (667, 29, 126, 126)

PAD1 = cv2.imread(ops_util.resource_path('task', 'fill1.png'))
QUESTION = cv2.imread(ops_util.resource_path('task', 'wenhao.png'))
ME = cv2.imread(ops_util.resource_path('task', 'me.png'))
ME18 = cv2.imread(ops_util.resource_path('task', 'me18.png'))
ME4X10 = cv2.imread(ops_util.resource_path('task', 'me4x10.png'))
FINAL = cv2.imread(ops_util.resource_path('task', 'final.png'))
ITEM = cv2.imread(ops_util.resource_path('task', 'ic.png'))
ITEM_USED = cv2.imread(ops_util.resource_path('item', 'chuandai.png'))
ITEM_SWITCHED = cv2.imread(ops_util.resource_path('item', 'switch.png'))
ITEM_XIYOU = cv2.imread(ops_util.resource_path('item', 'xiyou.png'))
ITEM_WODE = cv2.imread(ops_util.resource_path('item', 'wode.png'))
ITEM_FENJIE0 = cv2.imread(ops_util.resource_path('item', 'fenjie0.png'))
ITEM_FENJIE = cv2.imread(ops_util.resource_path('item', 'fenjie.png'))
ITEM_FENJIE1 = cv2.imread(ops_util.resource_path('item', 'fenjie1.png'))
ITEM_SPACE = cv2.imread(ops_util.resource_path('item', 'click_space.png'))
ITEM_QUANBUFENJIE = cv2.imread(ops_util.resource_path('item', 'quanbufenjie.png'))
ITEM_PAGE = cv2.imread(ops_util.resource_path('item', 'item_page.png'))

ITEM_XIULI = cv2.imread(ops_util.resource_path('item', 'xiuli.png'))
ITEM_XIULI1 = cv2.imread(ops_util.resource_path('item', 'xiuli1.png'))

TASK_JIEJIN = cv2.imread(ops_util.resource_path('task', 'task_jiejin.png'))
TASK_CLOSE = cv2.imread(ops_util.resource_path('task', 'task_close.png'))


CLEAR_CONFIRM = cv2.imread(ops_util.resource_path('clear', 'confirm.png'))

M0 = {
    'mission_name':'M0',
    'size': (5, 3),
    'start_point':(0,2),
    'end_point':(4,1),
    'room_count':6,
    'room_path':('r','r','u','r','r'),
}

M0R0 = {
    'room_name':'M0R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep':0,
}

M0R1 = {
    'room_name':'M0R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M0R2 = {
    'room_name':'M0R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M0R3 = {
    'room_name':'M0R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M0R4 = {
    'room_name':'M0R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}
M0R5= {
    'room_name':'M0R5',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': False,
    'sleep': 0,

}

M1 = {
    'mission_name':'M0',
    'size': (5, 3),
    'start_point':(0,2),
    'end_point':(4,2),
    'room_count':5,
    'room_path':('r','r','r','r'),
}

M1R0 = {
    'room_name':'M1R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M1R1 = {
    'room_name':'M1R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M1R2 = {
    'room_name':'M1R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M1R3 = {
    'room_name':'M1R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}

M1R4 = {
    'room_name':'M1R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': False,
    'sleep': 0,

}

M2 = {
    'mission_name':'M2',
    'size': (6, 2),
    'start_point':(0,1),
    'end_point':(5,1),
    'room_count':6,
    'room_path':('r','r','r','r','r'),
}

M2R0 = {
    'room_name':'M2R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M2R1 = {
    'room_name':'M2R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M2R2 = {
    'room_name':'M2R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M2R3 = {
    'room_name':'M2R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M2R4 = {
    'room_name':'M2R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}
M2R5= {
    'room_name':'M2R5',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': False,
    'sleep': 0,

}

M3 = {
    'mission_name':'M3',
    'size': (4, 3),
    'start_point':(0,2),
    'end_point':(3,2),
    'room_count':6,
    'room_path':('u','r','d','r','r'),
}

M3R0 = {
    'room_name':'M3R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M3R1 = {
    'room_name':'M3R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M3R2 = {
    'room_name':'M3R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M3R3 = {
    'room_name':'M3R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M3R4 = {
    'room_name':'M3R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': True,
    'sleep': 0,

}
M3R5= {
    'room_name':'M3R5',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': True,
    'sleep': 0,

}

M4 = {
    'mission_name':'M4',
    'size': (4, 3),
    'start_point':(0,2),
    'end_point':(3,2),
    'room_count':6,
    'room_path':('u','r','r','r','d'),
}

M4R0 = {
    'room_name':'M4R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_UPGATE,
    'esc_needed': False,
    'sleep': 0,

}

M4R1 = {
    'room_name':'M4R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M4R2 = {
    'room_name':'M4R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M4R3 = {
    'room_name':'M4R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M4R4 = {
    'room_name':'M4R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}
M4R5= {
    'room_name':'M4R5',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': True,
    'sleep': 0,

}

M5 = {
    'mission_name':'M5',
    'size': (4, 4),
    'start_point':(0,1),
    'end_point':(3,3),
    'room_count':6,
    'room_path':('d','r','d','r','r'),
}

M5R0 = {
    'room_name':'M5R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': True,
    'sleep': 15,

}

M5R1 = {
    'room_name':'M5R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M5R2 = {
    'room_name':'M5R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M5R3 = {
    'room_name':'M5R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M5R4 = {
    'room_name':'M5R4',
    'margin':(400, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}
M5R5= {
    'room_name':'M5R5',
    'margin':(300, 400),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': True,
    'sleep': 0,

}


M6 = {
    'mission_name':'M6',
    'size': (4, 3),
    'start_point':(0,2),
    'end_point':(3,2),
    'room_count':6,
    'room_path':('u','r','d','r','r'),
}

M6R0 = {
    'room_name':'M6R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': True,
    'sleep': 12,

}

M6R1 = {
    'room_name':'M6R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M6R2 = {
    'room_name':'M6R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M6R3 = {
    'room_name':'M6R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M6R4 = {
    'room_name':'M6R4',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}
M6R5= {
    'room_name':'M6R5',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': False,
    'sleep': 0,

}

M7 = {
    'mission_name':'M7',
    'size': (4, 2),
    'start_point':(0,1),
    'end_point':(3,1),
    'room_count':4,
    'room_path':('r','r','r'),
}

M7R0 = {
    'room_name':'M7R0',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': True,
    'sleep': 0,

}

M7R1 = {
    'room_name':'M7R1',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_QUESTION,
    'esc_needed': False,
    'sleep': 0,

}

M7R2 = {
    'room_name':'M7R2',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_MINI_MAP,
    'esc_needed': False,
    'sleep': 0,

}

M7R3 = {
    'room_name':'M7R3',
    'margin':(300, 500),
    'left_margin_png':(),
    'right_margin_png':(),
    'next_door_path':(),
    'finish_mode':FINISH_MODE_BOSS,
    'esc_needed': False,
    'sleep': 0,

}



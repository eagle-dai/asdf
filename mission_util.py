import ops_util
import logging
import aircv as ac
import numpy as np
from utils import *

def in_mission():
    pass

def in_last_room():
    pass
#
# def room_finished():
#     count = ops_util.right_top_diff()
#     logging.debug("count:%d", count)
#     if count > 600:
#         return True
#     return False

def room_finished(mpos):
    # count = ops_util.right_top_diff()
    # logging.debug("count:%d", count)
    # if count > 600:
    #     return True
    # return False
    res = ops_util.right_top_diff_img()
    obj = ac.imread(resource_path('task', 'ff.png'))
    pos = ac.find_all_template(res, obj, threshold=0.7)
    logging.debug("room_finished:%d,%s", len(pos), pos)
    for p in pos:
        dis = ops_util.diff_pos(p, mpos[0])
        logging.debug("room_finished diff:%d", dis)
        if dis >10 and dis <30:
            return True
    return False

def boss_finished():
    return len(ops_util.end_pos()) ==0


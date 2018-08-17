import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import ms_util
import screen
import kb_util
import ops_util


def go_home():
    kb_util.esc(delay=0.1)
    time.sleep(1)
    img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    obj = cv2.imread(os.path.join(os.getcwd(), 'home', 'home.png'))
    pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
    logging.debug("home:%d,%s", len(pos), pos)
    if len(pos) == 0:
        kb_util.esc(delay=0.1)
        time.sleep(1)
        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug("home:%d,%s", len(pos), pos)

    rimg = img
    rpos = pos
    if len(pos) == 1:
        logging.info("find home")
        ms_util.click_first(pos)

    img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
    logging.debug("home:%d,%s", len(pos), pos)
    if len(pos) == 1:
        logging.info("clear system menu")
        kb_util.esc(delay=0.1)
        time.sleep(1)

    return rimg, rpos


def main_task():
    kb_util.f1(delay=0.1)
    time.sleep(1)
    img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    obj = cv2.imread(os.path.join(os.getcwd(), 'task', 'zhuxian1.png'))
    pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
    logging.debug("main task:%d,%s", len(pos), pos)
    if len(pos) != 1 :
        return False

    ms_util.click_first(pos)
    ms_util.click_first(pos)
    time.sleep(1)
    while True:
        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        obj = cv2.imread(os.path.join(os.getcwd(), 'task', 'zhuxian2.png'))
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug("task direction:%d,%s", len(pos), pos)
        if len(pos) == 1:
            ms_util.click_first(pos)
            kb_util.esc(delay=0.1)
            break
        time.sleep(0.2)

    return True


def goto_fight():
    while True:
        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        obj = cv2.imread(os.path.join(os.getcwd(), 'direction', 'qianjin.png'))
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug("goto fight:%d,%s", len(pos), pos)
        if len(pos) != 1:
            continue
        direct = screen.direction(pos)
        if direct == 0:
            kb_util.left(50)
        elif direct == 1:
            kb_util.up(50)
        elif direct == 2:
            kb_util.right(50)
        elif direct == 3:
            kb_util.down(50)
        else:
            logging.warning("where to go?")
            kb_util.right(50)

        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        obj = cv2.imread(os.path.join(os.getcwd(), 'task', 'mission.png'))
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug("goto mission:%d,%s", len(pos), pos)
        if len(pos) == 1:
            kb_util.space()
            break

    while True:
        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        obj = cv2.imread(os.path.join(os.getcwd(), 'task', 'me.png'))
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug("wait mission:%d,%s", len(pos), pos)
        if len(pos) == 1:
            break
        time.sleep(0.2)


def finished():
    r = []
    pos = ops_util.find_pos_finish('task', 'wenhao.png')
    logging.debug("finised:%d,%s", len(pos), pos)
    mpos = ops_util.find_pos_finish('task', 'me.png')
    logging.debug("finised(me):%d,%s", len(mpos), mpos)
    if len(mpos) != 1:
        return r

    for p in pos:
        dx = ops_util.cx(p) - ops_util.cx(mpos[0])
        dy = ops_util.cy(p) - ops_util.cy(mpos[0])
        if abs(dx) < abs(dy):
            if dy < 0:
                r.append(1)
            else:
                r.append(3)
        else:
            if dx < 0:
                r.append(0)
            else:
                r.append(2)

    return r


def change_direction():
    img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    obj = cv2.imread(os.path.join(os.getcwd(), 'characters', 'guijiansileft2.png'))
    pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
    logging.debug("change_direction(left):%d,%s", len(pos), pos)
    # kb_util.up(5)
    if len(pos) == 1:
        logging.debug("go here")
        kb_util.right(20)
        return 1
    else:
        kb_util.left(20)
        return 0


def one_fight(d):
    kb_util.up(5, delay=0.2)
    kb_util.skill('s', 1, delay=0.02)
    kb_util.skill('d', 1, delay=0.02)
    kb_util.skill('x', 5, 0.02)

    kb_util.down(5, delay=0.2)
    kb_util.skill('s', 1, delay=0.02)
    kb_util.skill('d', 1, delay=0.02)
    kb_util.skill('x', 5, 0.02)

    kb_util.down(5, delay=0.2)
    kb_util.skill('s', 1, delay=0.02)
    kb_util.skill('d', 1, delay=0.02)
    kb_util.skill('x', 5, 0.02)

    kb_util.right(5, delay=0.2)
    kb_util.skill('s', 1, delay=0.02)
    kb_util.skill('d', 1, delay=0.02)
    kb_util.skill('x', 5, 0.02)

    kb_util.right(5, delay=0.2)
    kb_util.skill('s', 1, delay=0.02)
    kb_util.skill('d', 1, delay=0.02)
    kb_util.skill('x', 5, 0.02)






def one_fight2(s, c, d):
    start=time.time()
    while True:
        now = time.time()
        if len(finished()) >= 1:
            return
        if now-start>3:
            if d==1:
                if ops_util.am_i_stuck_right():
                    ops_util.skill_cycle()
                    if len(finished()) >= 1:
                        return
                    ops_util.right(150)
                    ops_util.left(30)
                    return 0
                else:
                    for i in range(0, 2):
                        ops_util.skill_cycle()
                        if len(finished()) >= 1:
                            return
                        ops_util.right(300)
                    return 1
            else:
                if ops_util.am_i_stuck_left():
                    ops_util.skill_cycle()
                    if len(finished()) >= 1:
                        return
                    ops_util.left(150)
                    ops_util.right(30)
                    return 1
                else:
                    for i in range(0, 2):
                        ops_util.skill_cycle()
                        if len(finished()) >= 1:
                            return
                        ops_util.left(300)
                    return 0


def fight():
    c = 0
    d = 1
    s=time.time()
    ops_util.esc_clear()
    pos = ops_util.go_middle()
    if len(pos) >=1 and ops_util.cx(pos[0]) > 400:
        d=0
    while True:
        f = finished()
        if len(f) == 0:
            c += 1
            d=one_fight2(s, c, d)
            continue
        else:
            logging.info(time.time()-s)
            s = time.time()
            next_room(f)
            ops_util.esc_clear()
            pos = ops_util.go_middle()
            if len(pos) >= 1 and ops_util.cx(pos[0]) > 400:
                d = 0


def next_room(dl):
    for d in dl:
        if d == 0:
            while True:
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    kb_util.left(200)
                else:
                    kb_util.left(400)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
                kb_util.up(100)
                if len(finished()) == 0:
                    return
                kb_util.down(200)
                if len(finished()) == 0:
                    return
        elif d == 1:
            while True:
                kb_util.up(100)
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_right():
                    kb_util.right(200)
                else:
                    kb_util.right(400)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    kb_util.left(200)
                else:
                    kb_util.left(400)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
        elif d == 2:
            while True:
                if ops_util.am_i_stuck_right():
                    kb_util.right(200)
                else:
                    kb_util.right(400)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
                kb_util.up(100)
                if len(finished()) == 0:
                    return
                kb_util.down(200)
                if len(finished()) == 0:
                    return
        elif d == 3:
            kb_util.down(100)
            if len(finished()) == 0:
                return
            if ops_util.am_i_stuck_right():
                kb_util.right(200)
            else:
                kb_util.right(400)
                if len(finished()) == 0:
                    return
                continue
            if len(finished()) == 0:
                return
            if ops_util.am_i_stuck_left():
                kb_util.left(200)
            else:
                kb_util.left(400)
                if len(finished()) == 0:
                    return
                continue
            if len(finished()) == 0:
                return


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    screen.Screen.init_dummp()
    screen.focus()
    # img, pos = go_home()
    # main_task()
    # goto_fight()
    ops_util.esc_clear()
    fight()
    # pos = whereami()

    # go_middle(pos)
    # kb_util.down(3,delay=0.2)#80
    # time.sleep(2)
    # whereami()
    # test_speed()




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
import utils
import gcf
import mission
import mission_util
import nm
import mcfg



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

def done():
    r = []
    pos = ops_util.find_pos_finish('task', 'final.png')
    logging.debug("done:%d,%s", len(pos), pos)
    mpos = ops_util.find_pos_finish('task', 'me.png')
    logging.debug("done(me):%d,%s", len(mpos), mpos)
    if len(mpos) != 1:
        return r

    for p in pos:
        dx = ops_util.cx(p) - ops_util.cx(mpos[0])
        dy = ops_util.cy(p) - ops_util.cy(mpos[0])
        if abs(dx) + abs(dy) < 20 and abs(dx) + abs(dy) > 10:
            logging.info("last room")
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

def renwuwancheng():
    r = []
    pos = ops_util.find_pos_main('task', 'renwuwancheng.png')
    logging.debug("renwuwancheng:%d,%s", len(pos), pos)
    if len(pos) == 1:
        r.append(0)
    return r

def one_fight(s, c, d):
    start=time.time()
    logging.info("one_fight:%f", start)
    while gcf.Gcfg.running:
        if len(finished()) >= 1:
            return
        ops_util.skill_cycle()
        now = time.time()
        if now-start>3:
            if d==1:
                if ops_util.am_i_stuck_right():
                    ops_util.skill_cycle()
                    # if len(finished()) >= 1:
                    #     return
                    # ops_util.right(150)
                    ops_util.left(30)
                    return 0
                else:
                    for i in range(0, 2):
                        ops_util.skill_cycle()
                        # if len(finished()) >= 1:
                        #     return
                        ops_util.right(300)
                    return 1
            else:
                if ops_util.am_i_stuck_left():
                    ops_util.skill_cycle()
                    # if len(finished()) >= 1:
                    #     return
                    # ops_util.left(150)
                    ops_util.right(30)
                    return 1
                else:
                    for i in range(0, 2):
                        ops_util.skill_cycle()
                        # if len(finished()) >= 1:
                        #     return
                        ops_util.left(300)
                    return 0


def fight():

    c = 0
    d = 1
    s=time.time()
    # ops_util.esc_clear()
    pos = ops_util.go_middle()
    if len(pos) >=1 and ops_util.cx(pos[0]) > 400:
        d=0
    b_last_room = False
    while gcf.Gcfg.running:
        # ops_util.esc_clear()
        if len(renwuwancheng()) == 1:
            kb_util.space(1, delay=0.5)
            b_last_room = False
            wait_mission()

        if b_last_room:
            ops_util.esc_clear()
        dn = done()
        if len(dn) == 1 and ((int(time.time() - s))/30)%2 == 1 :
            logging.info("last room done")
            b_last_room = True
            # s = time.time()
            last_room(dn)
            # ops_util.esc_clear()
            pos = ops_util.go_middle()
            if len(pos) >= 1 and ops_util.cx(pos[0]) > 400:
                d = 0
            d=one_fight(s, c, d)
            continue
        f = finished()
        if len(f) == 0:
            c += 1
            d=one_fight(s, c, d)
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
    logging.info("next room")
    s = time.time()
    cr = 0
    cl = 0
    for d in dl:
        cr = 0
        cl = 0
        if d == 0:
            while gcf.Gcfg.running:
                logging.info("left door")
                if(time.time() - s > 100):
                    break
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    ops_util.left(200)
                else:
                    ops_util.left(200)
                    cl = cl + 1
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
                ops_util.up(100)
                if len(finished()) == 0:
                    return
                ops_util.down(200)
                if len(finished()) == 0:
                    return
        elif d == 1:
            while gcf.Gcfg.running:
                logging.info("up door")
                if(time.time() - s > 100):
                    break
                ops_util.up(100)
                if len(finished()) == 0:
                    return
                if cr <= 10:
                    if ops_util.am_i_stuck_right():
                        ops_util.right(200)
                    else:
                        ops_util.right(200)
                        cr = cr + 1
                        if len(finished()) == 0:
                            return
                        continue
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    ops_util.left(200)
                else:
                    ops_util.left(200)
                    cl = cl + 1
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
        elif d == 2:
            while gcf.Gcfg.running:
                logging.info("right door")

                if(time.time() - s > 100):
                    break
                if ops_util.am_i_stuck_right():
                    ops_util.right(200)
                else:
                    ops_util.right(200)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return
                ops_util.up(100)
                if len(finished()) == 0:
                    return
                ops_util.down(200)
                if len(finished()) == 0:
                    return
        elif d == 3:
            while gcf.Gcfg.running:
                logging.info("down door")

                if(time.time() - s > 100):
                    break
                ops_util.down(100)
                if len(finished()) == 0:
                    return
                if cr <= 10:
                    if ops_util.am_i_stuck_right():
                        ops_util.right(200)
                    else:
                        ops_util.right(200)
                        cr = cr + 1
                        if len(finished()) == 0:
                            return
                        continue
                if len(finished()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    ops_util.left(200)
                else:
                    ops_util.left(200)
                    if len(finished()) == 0:
                        return
                    continue
                if len(finished()) == 0:
                    return


def last_room(dl):
    logging.info("last room")
    for d in dl:
        if d == 0:
            while gcf.Gcfg.running:
                if len(done()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    kb_util.left(200)
                else:
                    kb_util.left(400)
                    if len(done()) == 0:
                        return
                    continue
                if len(done()) == 0:
                    return
                kb_util.up(100)
                if len(done()) == 0:
                    return
                kb_util.down(200)
                if len(done()) == 0:
                    return
        elif d == 1:
            while gcf.Gcfg.running:
                kb_util.up(100)
                if len(done()) == 0:
                    return
                if ops_util.am_i_stuck_right():
                    kb_util.right(200)
                else:
                    kb_util.right(400)
                    if len(done()) == 0:
                        return
                    continue
                if len(done()) == 0:
                    return
                if ops_util.am_i_stuck_left():
                    kb_util.left(200)
                else:
                    kb_util.left(400)
                    if len(done()) == 0:
                        return
                    continue
                if len(done()) == 0:
                    return
        elif d == 2:
            while gcf.Gcfg.running:
                if ops_util.am_i_stuck_right():
                    kb_util.right(200)
                else:
                    kb_util.right(400)
                    if len(done()) == 0:
                        return
                    continue
                if len(done()) == 0:
                    return
                kb_util.up(100)
                if len(done()) == 0:
                    return
                kb_util.down(200)
                if len(done()) == 0:
                    return
        elif d == 3:
            kb_util.down(100)
            if len(done()) == 0:
                return
            if ops_util.am_i_stuck_right():
                kb_util.right(200)
            else:
                kb_util.right(400)
                if len(done()) == 0:
                    return
                continue
            if len(done()) == 0:
                return
            if ops_util.am_i_stuck_left():
                kb_util.left(200)
            else:
                kb_util.left(400)
                if len(done()) == 0:
                    return
                continue
            if len(done()) == 0:
                return


def start_guaji():

    screen.Screen.init_dummp()
    screen.focus()

    while gcf.Gcfg.running:
        m = mission.Mission("test", "0123")
        # m.init_rooms()
        # m.run_mission()
        ops_util.esc_clear()
        ops_util.wait_mission()





def start_kaishi():

    screen.Screen.init()
    # screen.Screen.init_dummp()
    screen.focus()
    ops_util.wait_loading()
    ops_util.esc_clear()
    ops_util.go_home()
    ops_util.esc_clear()
    ops_util.main_task()
    ops_util.goto_fight_c0()

    while gcf.Gcfg.running:
        # ops_util.esc_clear()
        ops_util.goto_fight_in_mission()
        mission_name=nm.get_m_name_in_mission()
        m=nm.Mission(mission_name)
        screen.focus()
        m.run()
        nm.pick_all()
        nm.swith_item()
        nm.destroy_item()
        ops_util.next_task()

        # m = mission.Mission("test", "0123")
        # m.init_rooms()
        # m.run_mission()
        # ops_util.esc_clear()
        # ops_util.wait_mission()


    # img, pos = go_home()
    # main_task()
    # goto_fight()
    # ops_util.esc_clear()
    # fight()
    # pos = whereami()

    # go_middle(pos)
    # kb_util.down(3,delay=0.2)#80
    # time.sleep(2)
    # whereami()
    # test_speed()

def start_zhandou():
    screen.focus()
    while gcf.Gcfg.running:
        # ops_util.esc_clear()
        ops_util.goto_fight_in_mission()
        mission_name = nm.get_m_name_in_mission()
        m = nm.Mission(mission_name)
        screen.focus()
        m.run()
        nm.pick_all()
        nm.swith_item()
        nm.destroy_item()
        ops_util.next_task()

        # m = mission.Mission("test", "0123")
        # m.init_rooms()
        # m.run_mission()
        # ops_util.esc_clear()
        # ops_util.wait_mission()

    # img, pos = go_home()
    # main_task()
    # goto_fight()
    # ops_util.esc_clear()
    # fight()
    # pos = whereami()

    # go_middle(pos)
    # kb_util.down(3,delay=0.2)#80
    # time.sleep(2)
    # whereami()
    # test_speed()

def start_jixu():
    screen.focus()
    while gcf.Gcfg.running:
        # ops_util.esc_clear()
        ops_util.goto_fight_in_mission()
        mission_name=nm.get_m_name_in_mission()
        m=nm.Mission(mission_name)
        m.run()
        nm.pick_all()
        nm.swith_item()
        nm.destroy_item()
        ops_util.next_task()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()
    # ops_util.goto_fight_c0()

    start_jixu()
    # start_zhandou()

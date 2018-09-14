import logging
import time
import kb_util
import ms_util
import gcf
from utils import *
import random
import mcfg
import nm
import numpy as np

def esc_1s():
    kb_util.esc(1, 0.3)
    # time.sleep(0.2)

def in_menu():
    pos = find_pos_main('home', 'home.png')
    logging.debug("in_menu:%d,%s", len(pos), pos)
    return pos


def in_esc():
    pos = find_pos_main('clear', 'esc.png')
    logging.debug("in_esc:%d,%s", len(pos), pos)
    return pos

def in_space():
    pos = find_pos_main('clear', 'kongge.png')
    logging.debug("in_space:%d,%s", len(pos), pos)
    return pos

def in_confirm():
    pos = find_pos_main('clear', 'confirm.png')
    logging.debug("in_confirm:%d,%s", len(pos), pos)
    return pos

def clear_confirm():
    got=False
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>15:
            break
        pos = find_pos_main('clear', 'confirm.png')
        logging.debug("clear_confirm:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no confirm")
            break
        for p in pos:
            logging.info("clear one confrim:%s", pos)
            ms_util.click_one(p)
            got=True

    s = time.time()
    while gcf.Gcfg.running:
        if time.time()-s>15:
            break
        pos = find_pos_main('clear', 'xx.png')
        logging.debug("clear_xx:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no xx")
            break
        for p in pos:
            logging.info("clear one xx:%s", pos)
            ms_util.click_one(p)
    return got

def clear_space():
    s=time.time()
    s1=time.time()
    while gcf.Gcfg.running:
        if time.time()-s1>5:
            screen.focus()
            s1=time.time()
        if time.time()-s>15:
            break
        pos = find_pos_main('clear', 'kongge.png')
        logging.debug("clear_space:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no space")
            break
        for p in pos:
            logging.info("clear one space:%s", pos)
            kb_util.space(2,0.1)

def clear_finish():
    s=time.time()
    s1=time.time()
    while gcf.Gcfg.running:
        if time.time()-s1>5:
            screen.focus()
            s1=time.time()
        if time.time()-s>15:
            break
        pos = find_pos_main('clear', 'wancheng.png')
        logging.debug("clear_finish:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no finish")
            break
        for p in pos:
            logging.info("clear one finish:%s", pos)
            kb_util.space(1,0.1)

def clear_finish_space():
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>15:
            break
        pos = find_pos_main('clear', 'wancheng.png')
        logging.debug("clear_finish:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no finish")
            break
        for p in pos:
            logging.info("clear one finish:%s", pos)
            kb_util.space(1,0.1)

def clear_menu():
    got_esc = False
    s=time.time()
    while gcf.Gcfg.running:
        if(time.time()-s>5):
            screen.focus()
            s=time.time()
        pos = in_menu()
        if len(pos) == 0 and got_esc == True:
            logging.info("no menu")
            break
        if len(pos)>0:
            got_esc = True
        else:
            clear_space()
            clear_finish()
            clear_confirm()
        # screen.focus()
        esc_1s()

def clear_menu_no_finish():
    got_esc = False
    s=time.time()
    while gcf.Gcfg.running:
        if(time.time()-s>5):
            screen.focus()
            s=time.time()
        pos = in_menu()
        if len(pos) == 0 and got_esc == True:
            logging.info("no menu")
            break
        if len(pos)>0:
            got_esc = True
        else:
            clear_space()
            clear_finish_space()
            clear_confirm()
        # screen.focus()
        esc_1s()

def clear_menu_with_focus():
    got_esc = False
    ts = time.time()
    while gcf.Gcfg.running:
        if time.time()-ts>15:
            break
        screen.focus()
        pos = in_menu()
        if len(pos) == 0 and got_esc == True:
            logging.info("no menu")
            break
        if len(pos)>0:
            got_esc = True
        else:
            clear_space()
            clear_finish()
            clear_confirm()
        # screen.focus()
        esc_1s()

def sure_no_esc():
    if len(in_esc()) > 0:
        clear_menu()


def sure_no_space():
    clear_space()

def sure_no_menu():
    s=time.time()
    while gcf.Gcfg.running:
        if(time.time()-s>5):
            screen.focus()
            s=time.time()
        pos = find_pos_main('home', 'menu.png')
        if len(pos) == 0:
            logging.info("sure_no_menu")
            break
        esc_1s()

def sure_no_task_menu():
    s=time.time()
    while gcf.Gcfg.running:
        if(time.time()-s>5):
            screen.focus()
            s=time.time()
        pos = find_pos_main('home', 'task_menu.png')
        if len(pos) == 0:
            logging.info("sure_no_task_menu")
            break
        esc_1s()

def goto_menu():
    got_esc = False
    s=time.time()
    while gcf.Gcfg.running:
        if(time.time()-s>5):
            screen.focus()
            s=time.time()
        pos = in_menu()
        if len(pos)>0:
            got_esc = True
            return
        else:
            clear_finish()
            clear_confirm()
        # screen.focus()
        esc_1s()


def esc_clear():
    esc_1s()
    clear_confirm()
    clear_finish()
    clear_menu()


def go_home():
    while gcf.Gcfg.running:
        # time.sleep(2)
        # pos = find_pos_main('clear', 'train2.png')
        # logging.debug("train:%d,%s", len(pos), pos)
        # if len(pos) == 0:
        #     logging.info("no train")
        #     break

        s=time.time()
        while gcf.Gcfg.running:
            if (time.time() - s > 5):
                screen.focus()
                s = time.time()
            esc_1s()
            clear_confirm()
            clear_finish()
            pos = in_menu()
            if len(pos) >= 1:
                s=time.time()
                while gcf.Gcfg.running:
                    if (time.time() - s > 5):
                        screen.focus()
                        s = time.time()
                    logging.info("go to home")
                    ms_util.click_first(pos)
                    time.sleep(0.5)
                    clear_confirm()
                    posc = in_menu()
                    if len(posc) == 0:
                        return

def left(step):
    #speed is 22 for 0.1
    kb_util.left(int(step/20), 0.1)


def right(step):
    kb_util.right(int(step/20), 0.1)


def up(step):
    #speed is 14 for 0.1
    kb_util.up(int(step/14), 0.1)


def down(step):
    kb_util.down(int(step/14), 0.1)

def left_v2(step):
    s=time.time()

    while True:
        pyautogui.keyDown("left", 0.05)
        if time.time() - s >= step/mcfg.SPEED_X:
            break
    pyautogui.keyUp("left", 0.01)


def left_v3(step):

    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        # pyautogui.keyDown("left", 0.1)
        # pyautogui.keyDown("up", 0.1)
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)

    s=time.time()
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    while True:
        # pyautogui.keyDown("left", 0.1)
        # pyautogui.keyDown("up", 0.1)
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)

    s=time.time()
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        # pyautogui.keyDown("left", 0.1)
        # pyautogui.keyDown("up", 0.1)
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)

def right_fight(step,ft):
    left_v2(20)
    # pyautogui.keyDown("right", 0.01)
    # pyautogui.keyUp("right", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
        if ft.finish:
          break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('r',ft)
    else:
        return

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("down", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
        if ft.finish:
          break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('r',ft)
    else:
        return

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
        if ft.finish:
          break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('r',ft)
    else:
        return

def left_fight(step,ft):
    right_v2(20)
    # pyautogui.keyDown("left", 0.01)
    # pyautogui.keyUp("left", 0.01)

    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
        if ft.finish:
          break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('l',ft)
    else:
        return


    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
        if ft.finish:
          break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('l',ft)
    else:
        return

    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
        if ft.finish:
          break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)
    if not ft.finish:
        skill_cycle_guijiansi('l',ft)
    else:
        return

def right_v2(step):
    s=time.time()
    while True:
        pyautogui.keyDown("right", 0.05)
        if time.time() - s >= step/mcfg.SPEED_X:
            break
    pyautogui.keyUp("right", 0.01)


def right_v3(step):

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("down", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)




def down_v2(step):
    s=time.time()

    while True:
        pyautogui.keyDown("down", 0.05)
        if time.time() - s >= step/mcfg.SPEED_Y:
            break
    pyautogui.keyUp("down", 0.01)

def down_v3(step):

    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step/mcfg.SPEED_Y/4:
            break
    pyautogui.keyUp("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyUp("down", 0.01)

    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_Y / 2:
            break
    pyautogui.keyUp("rigt", 0.01)
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyUp("down", 0.01)

    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    s=time.time()
    while True:
        if time.time() - s >= step / mcfg.SPEED_Y / 4:
            break
    pyautogui.keyUp("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyUp("down", 0.01)

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)
    # pyautogui.keyDown("left", 0.01)
    # pyautogui.keyUp("left", 0.01)



def up_v2(step):
    s=time.time()

    while True:
        pyautogui.keyDown("up", 0.05)
        if time.time() - s >= step/mcfg.SPEED_Y:
            break
    pyautogui.keyUp("up", 0.01)

def up_v3(step):
    s=time.time()

    pyautogui.keyDown("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    while True:
        if time.time() - s >= step/mcfg.SPEED_Y/4:
            break
    pyautogui.keyUp("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    pyautogui.keyUp("up", 0.01)

    s=time.time()
    pyautogui.keyDown("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_Y / 2:
            break
    pyautogui.keyUp("rigt", 0.01)
    pyautogui.keyDown("up", 0.01)
    pyautogui.keyUp("up", 0.01)

    s=time.time()
    pyautogui.keyDown("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_Y / 4:
            break
    pyautogui.keyUp("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    pyautogui.keyUp("up", 0.01)

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)
    # pyautogui.keyDown("left", 0.01)
    # pyautogui.keyUp("left", 0.01)


def read_pic(*args):
    return ac.imread(resource_path(*args))


# def direction(next, cur):
#     dx = cx(next) - cx(cur)
#     dy = cy(next) - cy(cur)
#     if abs(dx) < abs(dy):
#         if dy < 0:
#             return 1
#         else:
#             return 3
#     else:
#         if dx < 0:
#             return 0
#         else:
#             return 2


def where_am_i(d=None):
    c = 0
    m = 50
    diff = 200
    step = 20
    dw = False
    while gcf.Gcfg.running:
        pos = find_my_pos()
        logging.debug("where_am_i:%d,%s", len(pos), pos)
        if len(pos) > 0:
            # middle(pos)
            return my_pos_ajust(pos)
        sure_no_menu()
        sure_no_space()
        sure_no_esc()
        skill_cycle_s()

        # if dw == False:
        #     down_v2(40)
        #     dw = True
        # else:
        #     up_v2(40)
        #     dw = False

        diff = diff - step
        if diff < 0:
            diff = 200
        if d!=None and d==0:
            if c % 2 == 0:
                left_v2(diff)
            else:
                right_v2(diff)
        else:
            if c%2 == 0:
                right_v2(diff)
            else:
                left_v2(diff)
        c = c+1
        # if c > m:
        #     return pos


def find_my_pos(td=0.65):
    img = capture_main()
    pos = ac.find_all_template(img, mcfg.MY_IMG, threshold=td)
    return pos

def my_pos_ajust(pos):
    if len(pos) == 1:
        ret = []
        ret.append({})
        ret[0]['result'] = [pos[0]['result'][0], pos[0]['result'][1] + 115]
        return ret
    return None

def where_am_i_home(m=10):
    c = 0
    diff = 200
    step = 40
    dw = False
    while gcf.Gcfg.running:
        pos = find_my_pos()
        logging.debug("where_am_i_home:%d,%s", len(pos), pos)
        if len(pos) == 1:
            return my_pos_ajust(pos)
        sure_no_menu()
        if not in_home_v2():
            return None
        diff = diff - step
        if diff < 0:
            diff = 200
        if c%2 == 0:
            right_v2(diff)
        else:
            left_v2(diff)
        c = c+1
        if c > m:
            return pos



def cx(pos):
    return pos['result'][0]


def cy(pos):
    return pos['result'][1]

def skill_cycle(direction='n',ft=None):
    if ft.finish:
        return
    kb_util.skill('d', 1, delay=0.7)
    if ft.finish:
        return
    kb_util.skill('x', 4, delay=0.2)
    if ft.finish:
        return
    # if direction=='r':
    #     right_v2(100)
    # elif direction=='l':
    #     left_v2(100)
    if ft.finish:
        return
    kb_util.skill('s', 1, delay=0.3)
    if ft.finish:
        return
    kb_util.skill('x', 4, delay=0.2)

def skill_cycle_guijiansi(direction='n',ft=None):
    if ft.finish:
        return
    kb_util.skill('d', 1, delay=0.05)
    kb_util.skill('q', 1, delay=0.05)
    time.sleep(0.6)
    if ft.finish:
        return
    for i in range(0,4):
        kb_util.skill('x', 1, delay=0.25)
    if ft.finish:
        return
    if direction=='r':
        right_v2(40)
    elif direction=='l':
        left_v2(40)
    if ft.finish:
        return
    kb_util.skill('q', 1, delay=0.05)
    kb_util.skill('d', 1, delay=0.05)
    time.sleep(0.6)
    if ft.finish:
        return
    for i in range(0,3):
        kb_util.skill('x', 1, delay=0.25)

def skill_cycle_s():
    kb_util.skill('x', 4, delay=0.25)



def am_i_stuck_right():
    pos = where_am_i()
    if len(pos) == 0:
        return False
    else:
        if cx(pos[0]) > 420:
            return True

        else:
            return False

def am_i_stuck_left():
    pos = where_am_i()
    if len(pos) == 0:
        return False
    else:
        if cx(pos[0]) < 370:
            return True
        else:
            return False

def middle(pos):
    if len(pos) >= 1:
        if cy(pos[0]) > 330:
            up(cy(pos[0]) - 330)
        elif cy(pos[0]) < 330:
            down(325 - cy(pos[0]) + 15)

def middle_v2(pos,d=None):
    if d==0:
        right_v2(20)
    elif d==1:
        left_v2(20)
    if len(pos) >= 1:
        if cy(pos[0]) > mcfg.FIGHT_MIDDLE:
            up(cy(pos[0]) - mcfg.FIGHT_MIDDLE)
        elif cy(pos[0]) < mcfg.FIGHT_MIDDLE:
            # down(mcfg.FIGHT_MIDDLE - cy(pos[0])+20)
            down(mcfg.FIGHT_MIDDLE - cy(pos[0]))

def middle_v2_p(pos):
    if pos!=None:
        if cy(pos) > mcfg.FIGHT_MIDDLE:
            up(cy(pos) - mcfg.FIGHT_MIDDLE)
        elif cy(pos) < mcfg.FIGHT_MIDDLE:
            # down(mcfg.FIGHT_MIDDLE - cy(pos)+20)
            down(mcfg.FIGHT_MIDDLE - cy(pos))


def go_middle():
    logging.info("go_middle")
    # screen.focus()
    pos = where_am_i()
    middle(pos)
    return pos

def go_middle_v2():
    logging.info("go_middle_v2")
    # screen.focus()
    pos = where_am_i()
    middle_v2(pos)
    return pos


def wait_loading(char=None):
    while gcf.Gcfg.running:
        pos = find_pos_main( 'home', 'loading.png')
        logging.debug("loading:%d,%s", len(pos), pos)
        if len(pos) == 1:
            break
        screen.focus()
        if(char!=None):
            ms_util.click_first(char)
            time.sleep(0.5)
        kb_util.space(1, 0.1)
        pos = find_pos_main( 'home', 'start.png')
        logging.debug("start:%d,%s", len(pos), pos)
        if len(pos) >=1:
            pass
        else:
            break
        time.sleep(1)


def main_task():
    task='zhuxian'
    posq = find_pos_main('direction', 'qianjin.png')
    logging.debug("direction:%d,%s", len(posq), posq)
    if len(posq) == 1:
        logging.info("find direction:%d,%s", len(posq), posq)
        return task

    while gcf.Gcfg.running:
        # esc_clear()
        posz = None
        while gcf.Gcfg.running:
            kb_util.f1(delay=0.5)
            posz = find_pos_param(0,0,360,300, 'task', 'yiwancheng.png')
            logging.debug("yiwancheng task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                task = 'yiwancheng'
                logging.info("yiwancheng task find:%d,%s", len(posz), posz)
                return task

            posz = find_pos_param(0,0,360,300, 'task', 'zhuanzhi.png')
            logging.debug("zhuanzhi task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                task='zhuanzhi'
                logging.info("zhuanzhi task find:%d,%s", len(posz), posz)
                break

            posz = find_pos_param(0,0,360,300,'task', 'shoudong1.png')
            logging.debug("shoudong1 task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                task = 'shoudong1'
                logging.info("shoudong1 task find:%d,%s", len(posz), posz)
                return task


            posz = find_pos_param(0,0,360,300,'task', 'zhuxian1.png')
            logging.debug("main task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                logging.info("main task find:%d,%s", len(posz), posz)
                break
            # esc_clear()
            clear_menu()

        count=0
        while gcf.Gcfg.running and count<5:
            ms_util.click_first(posz)
            pos = find_pos_main('task', 'zhuxian2.png')
            logging.debug("task direction:%d,%s", len(pos), pos)
            if len(pos) == 1:
                ms_util.click_first(pos)
                break
            count = count+1
            clear_space()
            clear_confirm()
            time.sleep(0.5)


        sure_no_task_menu()
        posq = find_pos_main('direction', 'qianjin.png')
        logging.debug("direction:%d,%s", len(posq), posq)
        if len(posq) == 1:
            logging.info("find direction:%d,%s", len(posq), posq)
            break
        left_v3(300)

    return task


def zhuanzhi_task():
    while gcf.Gcfg.running:
        esc_clear()
        posz = None
        while gcf.Gcfg.running:
            kb_util.f1(delay=0.5)
            posz = find_pos_main( 'task', 'zhuanzhi.png')
            logging.debug("zhuanzhi task:%d,%s", len(posz), posz)
            if len(posz) == 0:
                logging.info("zhuanzhi task find:%d,%s", len(posz), posz)
                return
            break

        while gcf.Gcfg.running:
            ms_util.click_first(posz)
            pos = find_pos_main('task', 'zhuxian2.png')
            logging.debug("task direction:%d,%s", len(pos), pos)
            if len(pos) == 1:
                ms_util.click_first(pos)
                break
            pos = find_pos_main('task', 'zhuanzhidir.png')
            logging.debug("zhuanzhi direction:%d,%s", len(pos), pos)
            if len(pos) == 1:
                break
            time.sleep(1)

        esc_clear()
        posq = find_pos_main('direction', 'qianjin.png')
        logging.debug("direction:%d,%s", len(posq), posq)
        if len(posq) == 1:
            logging.info("find direction:%d,%s", len(posq), posq)
            break

def zhuanzhi_dialog():
        pos = find_pos_main('task', 'zhuanzhi.png')
        logging.debug("zhuanzhi:%d,%s", len(pos), pos)
        pos2 = None
        pos3=None
        pos4=None
        if len(pos) == 1:
            while gcf.Gcfg.running:
                ms_util.click_first(pos)
                time.sleep(2)
                pos2 = find_pos_main('task', 'zhuanzhi_step2.png')
                if len(pos2)==1:
                    break
        else:
            logging.error("no zhuanzhi")
            return

        while gcf.Gcfg.running:
            logging.debug("zhuanzhi zu feng zhe:%d,%s", len(pos), pos)
            ms_util.click_first(pos2)
            time.sleep(2)
            pos3 = find_pos_main('task', 'zhuanzhi_step3.png')
            if len(pos3) == 1:
                break

        while gcf.Gcfg.running:
            logging.debug("zhuanzhi zu feng zhe:%d,%s", len(pos), pos)
            ms_util.click_first(pos3)

            pos4 = find_pos_main('clear', 'kongge.png')
            if len(pos4) == 1:
                break

        clear_menu()
        # esc_clear()


def zhuanzhi_dialog_guijiansi():
    pos = find_pos_main('task', 'zhuanzhi.png')
    logging.debug("zhuanzhi:%d,%s", len(pos), pos)
    pos2 = None
    pos3 = None
    pos4 = None
    if len(pos) == 1:
        while gcf.Gcfg.running:
            ms_util.click_first(pos)
            time.sleep(2)
            pos2 = find_pos_main('task', 'zhuanzhi_step2_guijiansi.png')
            if len(pos2) == 1:
                break
    else:
        logging.error("no zhuanzhi")
        return

    while gcf.Gcfg.running:
        logging.debug("zhuanzhi zu feng zhe:%d,%s", len(pos), pos)
        ms_util.click_first(pos2)
        time.sleep(2)
        pos3 = find_pos_main('task', 'zhuanzhi_step3.png')
        if len(pos3) == 1:
            break

    while gcf.Gcfg.running:
        logging.debug("zhuanzhi zu feng zhe:%d,%s", len(pos), pos)
        ms_util.click_first(pos3)

        pos4 = find_pos_main('clear', 'kongge.png')
        if len(pos4) == 1:
            break

    clear_menu()
    # esc_clear()

def my_pos():
    pos = find_pos_finish('task', 'me.png')
    logging.debug("my pos:%d,%s", len(pos), pos)
    return pos

def my_pos_v2():
    img = capture_finish()
    obj = ac.imread(resource_path('task', 'me.png'))
    pos = ac.find_all_template(img, obj, threshold=0.65)
    if len(pos)==0:
        obj = ac.imread(resource_path('task', 'final.png'))
        pos = ac.find_all_template(img, obj, threshold=0.65)
    logging.debug("my pos v2:%d,%s", len(pos), pos)
    return pos


def end_pos():
    pos = find_pos_finish('task', 'final.png')
    logging.debug("final pos:%d,%s", len(pos), pos)
    return pos

def question_pos():
    pos = find_pos_finish('task', 'wenhao.png')
    logging.debug("question pos:%d,%s", len(pos), pos)

    return pos

def goto_fight():
    while gcf.Gcfg.running:
        # screen.focus()
        pos = find_pos_main('task', 'mission.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        time.sleep(2)
        if len(pos) == 1:
            kb_util.space(1, delay=0.5)
            break

        pos = find_pos_main( 'direction', 'qianjin.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        if len(pos) != 1:
            continue
        direct = screen.direction(pos)
        if direct == 0:
            go_middle()
            left(300)
        elif direct == 1:
            up(150)
        elif direct == 2:
            go_middle()
            right(300)
        elif direct == 3:
            down(150)
        else:
            logging.warning("where to go?")
            go_middle()
            right(300)

    wait_mission()


def jiejin_until(obj):
    s=time.time()
    count=0
    while gcf.Gcfg.running:
        if time.time()-s > 15:
            break
        img=capture_main()
        pos = ac.find_all_template(img, obj, threshold=0.85)
        logging.debug("jiejin_until obj:%d,%s",len(pos),pos)
        if len(pos)==1:
            goto_xy_home_dialog(pos[0]['result'][0], pos[0]['result'][1])
            time.sleep(0.5)
            img = capture_main()
            pos = ac.find_all_template(img, obj, threshold=0.85)
            if len(pos) == 0:
                kb_util.space()
                time.sleep(0.5)
                return
        else:
            count=count+1
            if count<4:
                continue
            kb_util.space()
            time.sleep(0.5)
            return


def follow_direction():
    logging.info("follow_direction")
    s=time.time()
    sd = None
    while gcf.Gcfg.running:
        if time.time()-s>5:
            screen.focus()
            s=time.time()
        me=where_am_i_home()
        pos = find_pos_main( 'direction', 'qianjin.png',td=0.5)
        if len(pos) == 0:
            pos = find_pos_main("task", "mission_g.png")
            if len(pos) > 0:
                logging.info("in mission")
                return 'mission'
            else:
                # img = capture_main()
                # pos = ac.find_all_template(img, mcfg.TASK_JIEJIN, threshold=0.9)
                # if len(pos)==1:
                #     tm=None
                    # while gcf.Gcfg.running:
                    #     ms_util.click(pos[0]['result'][0], pos[0]['result'][1]+80)
                    #     tm = capture_main()
                    #     tp = ac.find_all_template(tm, mcfg.TASK_CLOSE, threshold=0.9)
                    #     if len(tp) == 1:
                    #         break

                jiejin_until(mcfg.TASK_JIEJIN)
                tp = find_pos_main('task', 'zhuhe.png')
                if len(tp) == 1:
                    logging.info("in zhuhe")
                    ms_util.click_first(tp)
                    return  'dialog'
                tp = find_pos_main('task', 'zhuanzhi.png')
                if len(tp) == 1:
                    logging.info("in zhuanzhi")
                    return  'zhuanzhi'
                if in_home_v2():
                    logging.info("in dialog")
                    return 'dialog'
                else:
                    logging.info("in task")
                    return 'task'
        if len(me)==0:
            continue

        img=capture_main()
        pos = ac.find_all_template(img, mcfg.TASK_JIEJIN, threshold=0.85)
        if len(pos)==1:
            logging.info("task jiejin")
            jiejin_until(mcfg.TASK_JIEJIN)
            return 'dialog'

        ss=time.time()
        while gcf.Gcfg.running:
            if time.time()-ss>5:
                screen.focus()
                ss=time.time()
            d = direction()
            if d== None and sd !=None:
                d=sd
            if d!=None:
                break;
            left_v3(50)

        pos = find_pos_main('task','kaiqijineng.png')
        if len(pos) > 0:
            learn_skill_guijiansi()
            clear_menu()

        if d!= None:
            sd = d
        logging.info("direction:%d,%s", d[0], d[1])
        if d[0] == 1 or d[0] == 3:
            goto_xy_home_y_dir(d[1][0]['result'][0], d[1][0]['result'][1], me[0], d[0])
        else:
            goto_xy_home_x_dir(d[1][0]['result'][0], d[1][0]['result'][1], me[0], d[0])


def goto_zhuanzhi():
    while gcf.Gcfg.running:
        # screen.focus()
        pos = find_pos_main( 'direction', 'qianjin.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        if len(pos) != 1:
            return
        direct = screen.direction(pos)
        if direct == 0:
            go_middle_v2()
            left_v2(300)
        elif direct == 1:
            up_v2(150)
        elif direct == 2:
            go_middle_v2()
            right_v2(300)
        elif direct == 3:
            down_v2(150)
        else:
            logging.warning("where to go?")
            go_middle()
            right(300)


def goto_fight_c0():
    while gcf.Gcfg.running:
        # screen.focus()
        pos = find_pos_main('task', 'mission.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        time.sleep(2)
        if len(pos) == 1:
            kb_util.space(1, delay=0.5)
            break

        pos = find_pos_main( 'direction', 'qianjin.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        if len(pos) != 1:
            continue
        direct = screen.direction(pos)
        if direct == 0:
            go_middle_v2()
            left_v2(400)
        elif direct == 1:
            up_v2(150)
        elif direct == 2:
            go_middle()
            right_v2(400)
        elif direct == 3:
            down_v2(150)
        else:
            logging.warning("where to go?")
            go_middle_v2()
            right(400)

    wait_mission()

def fight_again():
    while gcf.Gcfg.running:
        # screen.focus()
        pos = find_pos_main( 'direction', 'qianjin.png')
        logging.debug("goto fight:%d,%s", len(pos), pos)
        if len(pos) != 1:
            return
        direct = screen.direction(pos)
        if direct == 0:
            left_v2(400)
        elif direct == 1:
            up_v2(150)
        elif direct == 2:
            right_v2(400)
        elif direct == 3:
            down_v2(150)
        else:
            logging.warning("where to go?")
            right(400)

def goto_xy(x,y,me=None):
    cp=me
    if me== None:
        cp=where_am_i()[0]
    dx=cx(cp)-x
    dy=cy(cp)-y
    if dy>0:
        up_v2(dy*1.25)
    else:
        down_v2(-dy*1.25)
    if dx > 0:
        left_v2(dx*1.5)
    else:
        right_v2(-dx*1.5)

def goto_xy_v3(x,y,me=None):
    cp=me
    if me== None:
        cp=where_am_i()[0]
    dx=cx(cp)-x
    dy=cy(cp)-y

    if dx > 0:
        left_v3(dx*1.5)
    else:
        right_v3(-dx*1.5)
    if dy>0:
        up_v3(dy*1.25)
    else:
        down_v3(-dy*1.25)


def goto_xy_home(x,y,me=None):
    cp=me
    if me== None:
        cp=where_am_i_home()[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y+40
    if dx > 0:
        left_v2(dx+40)
    else:
        right_v2(-dx+40)
    if dy>0:
        up_v2(dy)
    else:
        down_v2(-dy)

def goto_xy_home_v3(x, y, me=None):
    cp=me
    if me== None:
        cp=where_am_i_home()[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y
    if dx > 0:
        left_v3(dx+80)
    else:
        right_v3(-dx+80)
    if dy>0:
        up_v3(dy)
    else:
        down_v3(-dy)

def goto_xy_home_dialog(x, y, me=None):
    cp=me
    if me== None:
        pos=where_am_i_home()
        if pos == None:
            return
        cp=where_am_i_home()[0]
    dx=cx(cp)-x
    dy=cy(cp)-(y+180)
    count=1
    for i in range(0,count):
        if dx > 0:
            left_v2(dx/count)
        else:
            right_v2(-dx/count)
        if dy>0:
            up_v3(dy/count)
        else:
            down_v3(-dy/count)

def goto_xy_home_no(x,y,me=None,d=None):
    cp=me
    if me== None:
        cp=where_am_i_home(100)[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y
    if dx > 0:
        left_v2(dx)
    else:
        right_v2(-dx)
    if d!=None:
        if d==1:
            up_v2(dy + 50)
            up_v2(dy + 50)
        elif d==3:
            down_v2(-dy + 50)
            up_v2(dy + 50)
    else:
        if dy>0:
            up_v2(dy)
        else:
            down_v2(-dy)

def goto_xy_home_x_dir(x,y,me=None,d=None):
    logging.debug("goto_xy_home_x_dir")
    cp=me
    if me== None:
        cp=where_am_i_home(5)[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y
    if dx > 0:
        if dx>300:
            left_v3(200)
        left_v3(dx+40)
    else:
        if -dx >300:
            right_v3(200)
        right_v3(-dx+40)

    # if dy>0:
    #     up_v3(dy)
    # else:
    #     down_v3(-dy)


def goto_xy_home_y_dir(x,y,me=None,d=None):
    logging.debug("goto_xy_home_y_dir")
    cp=me
    if me== None:
        cp=where_am_i_home(5)[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y
    if dx > 0:
        left_v3(dx)
    else:
        right_v3(-dx)
    if d!=None:
        if d==1:
            up_v3(dy + 80)
        elif d==3:
            down_v3(-dy + 80)
    else:
        if dy>0:
            up_v3(dy)
        else:
            down_v3(-dy)

def goto_xy_home_no_v3(x,y,me=None,d=None):
    logging.debug("goto_xy_home_no_v3")
    cp=me
    if me== None:
        cp=where_am_i_home()[0]
        if cp==None:
            return
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y+40
    if dx > 0:
        left_v3(dx)
    else:
        right_v3(-dx)
    if d!=None:
        if d==1:
            up_v3(dy + 100)
        elif d==3:
            down_v3(-dy + 100)
    else:
        if dy>0:
            up_v3(dy)
        else:
            down_v3(-dy)

def goto_fight_in_mission():
    while gcf.Gcfg.running:
        pos = find_pos_main( 'direction', 'qianjin.png')
        logging.debug("goto fight in mission:%d,%s", len(pos), pos)
        if len(pos) != 1:
            break
        direct = screen.direction(pos)
        if direct == 0:
            go_middle_v2()
            left_v2(400)
        elif direct == 1:
            up_v2(150)
        elif direct == 2:
            go_middle()
            right_v2(400)
        elif direct == 3:
            down_v2(150)
        else:
            logging.warning("where to go?")
    wait_mission()

def wait_mission():
    while gcf.Gcfg.running:
        kb_util.space(1, 0.1)
        pos=find_pos_main("task","next_task.png")
        if len(pos)>0:
            ms_util.click_first(pos)
        esc_clear()
        pos = find_pos_main('task', 'me.png')
        logging.debug("wait mission:%d,%s", len(pos), pos)
        if len(pos) == 1:
            break
        fight_again()
        time.sleep(0.2)

def wait_in_mission():
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>5:
            s=time.time()
            screen.focus()
        kb_util.space(1, 0.1)
        img = capture_param(
            mcfg.MINI_MAP_X - 7 * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            7 * mcfg.MINI_MAP_SLOT_SIZE,
            7 * mcfg.MINI_MAP_SLOT_SIZE
        )
        if len(in_esc())>0:
            clear_menu()
        clear_space()
        pos = ac.find_all_template(img, mcfg.FINAL, threshold=0.8, rgb=False, bgremove=False)
        logging.debug("wait_in_mission:%d,%s", len(pos), pos)
        if len(pos) > 0:
            return

def learn_skill_guijiansi():

    ic=None
    while gcf.Gcfg.running:
        kb_util.skill('k', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.SKILL_PAGE, threshold=0.9)
        if len(ic)==1:
            break
        ops_util.clear_menu()
    time.sleep(0.5)

    skill_pos=[(100,150),(180,150),(220,150),(260,150),(310,150),(350,150),(390,150),(430,150),(470,150),(190,220),(290,220),(145,280),(335,280),(425,280),(50,350),(95,350),(50,420),(95,420),(145,420),(245,420),(425,420),(470,420),(525,420),(145,485)]
    for p in skill_pos:
        ms_util.move_and_click(p[0], p[1])
        time.sleep(0.3)
        img = capture_main()
        pos = ac.find_all_template(img, mcfg.SKILL_LEARN, threshold=0.98)
        logging.debug("skill：%s", pos)
        if len(pos) == 1:
            ms_util.click_first(pos)
        time.sleep(0.3)

    ms_util.click(210, 560)
    time.sleep(1)
    clear_confirm()

    while gcf.Gcfg.running:
        kb_util.skill('k', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.SKILL_PAGE, threshold=0.9)
        if len(ic) == 0:
            break

def wait_in_main():
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>5:
            s=time.time()
            screen.focus()
        pos=find_pos_main("task","find_main.png")
        if len(pos)>0:
            return 'zhuxian'
        pos = find_pos_main("task", "find_zhuanzhi.png")
        if len(pos) > 0:
            return 'zhuanzhi'
        kb_util.down(1)
        time.sleep(0.2)

        pos = find_pos_main('task','kaiqijineng.png')
        if len(pos) > 0:
            learn_skill_guijiansi()



def wait_in_zhuanzhi():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","find_zhuanzhi.png")
        if len(pos)>0:
            return
        kb_util.down(1)
        time.sleep(0.2)

def finish_yiwancheng():
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>15:
            break
        posz = find_pos_param(0,0,360,300,'task', 'yiwancheng.png')
        logging.debug("yiwancheng task:%d,%s", len(posz), posz)
        if len(posz) == 1:
            ms_util.click_first(posz)
            ms_util.click_first(posz)
            clear_space()
            clear_confirm()
            clear_menu_no_finish()
        else:
            break


def wait_till_next_mission():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","next_task.png")
        if len(pos)>0:
            return
        esc_clear()
        time.sleep(0.2)

def wait_till_next_mission_and_home():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","next_task.png")
        if len(pos)>0:
            kb_util.skill('F12')
            return
        esc_clear()
        time.sleep(0.2)

def clear_to_mission():
    s = time.time()
    while gcf.Gcfg.running:
        if time.time()-s>5:
            s=time.time()
            screen.focus()
        pos=find_pos_main("task","renwuwancheng.png")
        logging.info("clear_to_mission:%s",pos)
        if len(pos)==1:
            return
        clear_menu()

def mission_to_home():
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s>5:
            s=time.time()
            screen.focus()
        pos=find_pos_main("task","renwuwancheng.png")
        logging.info("mission_to_home:%s",pos)
        if len(pos)==0:
            while gcf.Gcfg.running:
                if in_home_v2():
                    return
        kb_util.skill('F12',delay=0.2)



def next_task():
    while gcf.Gcfg.running:
        kb_util.space(1, 0.5)
        pos=find_pos_main("task","next_task.png")
        if len(pos)>0:
            ms_util.click_first(pos)
        esc_clear()
        pos = find_pos_main('task', 'me.png')
        logging.debug("wait next task:%d,%s", len(pos), pos)
        if len(pos) == 1:
            break
        fight_again()
        time.sleep(0.2)

def right_top_diff():
    time.sleep(0.2)
    img1 = capture_finish()
    time.sleep(0.2)
    img2 = capture_finish()
    res = cv2.absdiff(img1, img2)
    count = 0
    for i in range(0, 150):
        for j in range(0,150):
            for k in range(0,2):
                if res[i][j][k] != 0:
                    count += 1

    return count


def right_top_diff_img():
    time.sleep(0.2)
    img1 = capture_finish()
    time.sleep(0.2)
    img2 = capture_finish()
    res = cv2.absdiff(img1, img2)
    return res


def same_pos(cur, next):
    dx = cx(next) - cx(cur)
    dy = cy(next) - cy(cur)
    if abs(dx) + abs(dy) < 10:
        return True
    return False

def diff_pos(cur, next):
    dx = cx(next) - cx(cur)
    dy = cy(next) - cy(cur)

    return abs(dx) + abs(dy)


def img_diff():
    obj = ac.imread(resource_path('task', 'b18x18.png'))
    for i in range(0, 18):
        for j in range(0,18):
            for k in range(0,2):
                if  obj[i][j][k] != 255:
                    print(obj[i][j][k])
                # obj[i][j][k] = 0

    img1 = capture_finish()
    # img1 = capture_main()
    time.sleep(0.2)
    img2 = capture_finish()
    # img2 = capture_main()
    res = cv2.absdiff(img1, img2)
    ac.show(res)
    # logging.debug("%s", res)
    for i in range(0, 150):
        for j in range(0,150):
            for k in range(0,2):
                if res[i][j][k] != 0:
                    res[i][j][k] = 255
                    print(res[i][j][k])
                else:
                    pass
                    # res[i][j][k] = img1[i][j][k]

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    contours = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # 获取最小包围矩形
        rect = cv2.minAreaRect(contours[0])

        # 中心坐标
        x, y = rect[0]
        print(x, y)

    cv2.imshow("a", obj)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("a", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("a", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("a", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pos = ac.find_all_template(res, obj, threshold=0.9, rgb = False)
    screen.show(res, pos)
    print(pos)

def in_home_v2():
    time.sleep(0.2)
    pos = find_pos_param(700,0,100,50, 'home','in_home_v2.png',td=0.7)
    logging.info("in_home_v2:%s", pos)
    if len(pos)>0:
        return True
    return False

def in_home():
    goto_menu()
    ms_util.click_up(mcfg.HOME_X,mcfg.HOME_Y)
    pos = find_pos_main('home', 'in_home.png',td=0.9)
    logging.debug("in_home:%s",pos)
    if len(pos)>0:
        return False
    return True

def direction():
    logging.debug("direction")
    img = capture_main()
    # ac.show(img)
    posl = ac.find_all_template(img, mcfg.ITEM_LEFT, threshold=0.7, rgb=True, bgremove=False)
    if len(posl)==1:
        logging.info("left:%s", posl)
        return (0,posl)
    posr= ac.find_all_template(img, mcfg.ITEM_RIGHT, threshold=0.7, rgb=True, bgremove=False)
    if len(posr)==1:
        logging.info("right:%s", posr)
        return (2,posr)
    # ac.show(upimg)
    posu = ac.find_all_template(img, mcfg.ITEM_UP, threshold=0.7, rgb=True, bgremove=False)
    if len(posu)==1:
        logging.info("up:%s", posu)
        return (1,posu)
    posu = ac.find_all_template(img, mcfg.ITEM_UP11, threshold=0.7, rgb=True, bgremove=False)
    if len(posu)==1:
        logging.info("up:%s", posu)
        return (1,posu)
    posd = ac.find_all_template(img, mcfg.ITEM_DOWN, threshold=0.6, rgb=True, bgremove=False)
    if len(posd)==1:
        logging.info("down:%s", posd)
        return (3,posd)

    logging.warn("no direction")
    return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()
    screen.focus()

    kb_util.skill('s', 1, delay=0.65)
    kb_util.skill('x', 4, delay=0.25)
    time.sleep(2)
    kb_util.skill('q', 1, delay=0.65)
    kb_util.skill('x', 3, delay=0.25)
    exit(0)
    char = cv2.imread(resource_path('characters','my_pos1.0.png'))
    #148 185 209
    bm = np.ndarray((char.shape[1]),dtype=np.uint8)
    for i in range(0,bm.shape[0]):
        bm[i]=0
    for i in range(0,char.shape[1]):
        for j in range(0,char.shape[0]):
            print(char[j][i][0],char[j][i][1],char[j][i][2])
            if char[j][i][0]==148 and char[j][i][1]==185 and char[j][i][2]==209:
                bm[i]=1
        print('\n')

    start=0
    end=char.shape[1]-1

    lv_got = False
    space_got = False
    for i in range(1,bm.shape[0]-1):
        if not lv_got:
            if bm[i-1]==0 and bm[i]==1:
                lv_got=True
        else:
            if not space_got:
                if bm[i - 1] == 0 and bm[i] == 0:
                    space_got=True
            else:
                if bm[i - 1] == 0 and bm[i] == 1:
                    if start==0:
                        start=i
                elif bm[i - 1] == 0 and bm[i] == 0:
                    if start!=0:
                        end=i-2
                        break

    res=np.ndarray((char.shape[0],end-start+1,char.shape[2]),char.dtype)
    for i in range(0,res.shape[1]):
        for j in range(0,res.shape[0]):
            res[j][i][0] = char[j][i+start][0]
            res[j][i][1] = char[j][i+start][1]
            res[j][i][2] = char[j][i+start][2]
    ac.show(res)
    # ac.show(char)
    print(start,end)

    img = capture_main()
    pos = ac.find_all_template(img, res, 0.5)
    logging.debug("%s",pos)









    exit(0)

    screen.Screen.init_dummp()
    screen.focus()
    direction()
    # right_fight(400)
    # logging.debug("in home:%d",in_home())
    # zhuanzhi_task()
    # goto_zhuanzhi()
    # wait_mission()
    # mission_name = nm.get_m_name_in_mission()
    # m = nm.Mission(mission_name)
    # screen.focus()
    # m.run()
    # nm.pick_all()
    # nm.swith_item()
    # ops_util.next_task()

    # posz=None
    # while gcf.Gcfg.running:
    #     img=capture_main()
    #     obj = cv2.imread(resource_path('task', 'zhuanzhi_npc1.png'))
    #     pos=ac.find_all_template(img,obj,threshold=0.7)
    #     goto_xy(pos[0]['result'][0],pos[0]['result'][1])
    #     kb_util.space(1,0.1)
    #     time.sleep(2)
    #     img=capture_main()
    #     obj = cv2.imread(resource_path('task', 'zhuanzhi_step1.png'))
    #     posz=ac.find_all_template(img,obj,threshold=0.7)
    #     time.sleep(2)
    #     if len(posz)==1:
    #         break
    #
    #
    #
    # poss=None
    # while gcf.Gcfg.running:
    #     ms_util.click_first(posz)
    #     time.sleep(2)
    #     img=capture_main()
    #     obj = cv2.imread(resource_path('task', 'zhuanzhi_step2.png'))
    #     poss=ac.find_all_template(img,obj,threshold=0.7)
    #     logging.debug("zhiye,%s",poss)
    #     if len(poss)==1:
    #         break
    #
    #
    # for i in range(0,5):
    #     ms_util.click_first(poss)
    # time.sleep(2)
    # img=capture_main()
    # obj = cv2.imread(resource_path('task', 'zhuanzhi_step3.png'))
    # pos=ac.find_all_template(img,obj,threshold=0.7)
    # logging.debug("zhiye,%s",pos)
    # time.sleep(2)
    # for i in range(0,5):
    #     ms_util.click_first(pos)
    # time.sleep(2)
    # kb_util.esc()
    # time.sleep(2)
    # img=capture_main()
    # obj = cv2.imread(resource_path('clear', 'confirm.png'))
    # pos=ac.find_all_template(img,obj,threshold=0.7)
    # logging.debug("zhiye,%s",pos)
    # time.sleep(2)
    # for i in range(0,5):
    #     ms_util.click_first(pos)




    # kb_util.skill('shiftright')
    # kb_util.skill('shiftright')
    # kb_util.skill('shiftright')
    # pos = find_pos_main('clear', 'train2.png')
    # logging.debug("train:%d,%s", len(pos), pos)
    # if len(pos) == 0:
    #     logging.info("no train")

    # img_diff()
    # where_am_i()
    # s=time.time()
    # # 140 1s 110 1s
    # while True:
    #     pyautogui.keyDown("up", 0.05)
    #     if time.time()-s>=1:
    #         break
    # pyautogui.keyUp("up", 0.01)
    # logging.debug("cost:%f",time.time()-s)
    # where_am_i()




    # screen.focus()
    # pos = find_pos_main('clear', 'confirm2.png')
    # logging.info(pos)
    # esc_clear()
    # pos = where_am_i()
    # right(200)
    # pos = where_am_i()

    # go_middle()
    # where_am_i()
    # r = am_i_stuck_right()
    # logging.info(r)
    # find_pos_main("img1", "test1.png", td=0.8)
    # print(resource_path("img1", "test1.png"))
    # str = input("Enter your input: ")
    # print("Received input is : ", str)
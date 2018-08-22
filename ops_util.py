import logging
import time
import kb_util
import ms_util
import gcf
from utils import *
import random
import mcfg
import nm

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

def clear_confirm():
    got=False
    while gcf.Gcfg.running:
        pos = find_pos_main('clear', 'confirm.png')
        logging.debug("clear_confirm:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no confirm")
            break
        for p in pos:
            logging.info("clear one confrim:%s", pos)
            ms_util.click_one(p)
            got=True
    return got

def clear_space():
    while gcf.Gcfg.running:
        pos = find_pos_main('clear', 'kongge.png')
        logging.debug("clear_space:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no space")
            break
        for p in pos:
            logging.info("clear one space:%s", pos)
            kb_util.space(2,0.1)

def clear_finish():
    while gcf.Gcfg.running:
        pos = find_pos_main('clear', 'wancheng.png')
        logging.debug("clear_finish:%d,%s", len(pos), pos)
        if len(pos) == 0:
            logging.info("no finish")
            break
        for p in pos:
            logging.info("clear one finish:%s", pos)
            ms_util.click_one(p)

def clear_menu():
    got_esc = False
    while gcf.Gcfg.running:
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
    while gcf.Gcfg.running:
        pos = find_pos_main('home', 'menu.png')
        if len(pos) == 0:
            logging.info("sure_no_menu")
            break
        esc_1s()

def goto_menu():
    got_esc = False
    while gcf.Gcfg.running:
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

        while gcf.Gcfg.running:
            esc_1s()
            clear_confirm()
            clear_finish()
            pos = in_menu()
            if len(pos) >= 1:
                while gcf.Gcfg.running:
                    logging.info("go to home")
                    ms_util.click_first(pos)
                    time.sleep(0.5)
                    clear_confirm()
                    # return
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
    s=time.time()

    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
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

def left_fight(step,done):
    if not done:
        skill_cycle('l')
    s=time.time()
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)
    if not done:
        skill_cycle('l')
    s=time.time()
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)

    if not done:
        skill_cycle('l')
    s=time.time()
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("left", 0.01)
    pyautogui.keyUp("left", 0.01)

def right_v2(step):
    s=time.time()
    while True:
        pyautogui.keyDown("right", 0.05)
        if time.time() - s >= step/mcfg.SPEED_X:
            break
    pyautogui.keyUp("right", 0.01)


def right_v3(step):
    s=time.time()

    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    s=time.time()
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("down", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    s=time.time()
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)


def right_fight(step,done):
    if not done:
        skill_cycle('r')
    s=time.time()
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
    while True:
        if time.time() - s >= step/mcfg.SPEED_X/4:
            break
    pyautogui.keyUp("up", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    if not done:
        skill_cycle('r')
    s=time.time()
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("down", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_X / 2:
            break
    pyautogui.keyUp("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyUp("right", 0.01)

    if not done:
        skill_cycle('r')
    s=time.time()
    pyautogui.keyDown("right", 0.01)
    pyautogui.keyDown("up", 0.01)
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
    s=time.time()

    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("left", 0.01)
    while True:
        if time.time() - s >= step/mcfg.SPEED_Y/4:
            break
    pyautogui.keyUp("left", 0.01)
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyUp("down", 0.01)

    s=time.time()
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("right", 0.01)
    while True:
        if time.time() - s >= step / mcfg.SPEED_Y / 2:
            break
    pyautogui.keyUp("rigt", 0.01)
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyUp("down", 0.01)

    s=time.time()
    pyautogui.keyDown("down", 0.01)
    pyautogui.keyDown("left", 0.01)
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


def direction(next, cur):
    dx = cx(next) - cx(cur)
    dy = cy(next) - cy(cur)
    if abs(dx) < abs(dy):
        if dy < 0:
            return 1
        else:
            return 3
    else:
        if dx < 0:
            return 0
        else:
            return 2


def where_am_i():
    c = 0
    m = 50
    diff = 200
    step = 20
    dw = False
    while gcf.Gcfg.running:
        # kb_util.skill('enter', delay=0.1)
        # for i in range(0, 2):
        #     kb_util.skill('g', delay=0.05)
        # kb_util.skill('enter', delay=0.1)
        # time.sleep(0.2)
        # pos = find_pos_main('home', 'gg_pos.png')
        pos = find_pos_main('characters', 'my_pos.png')
        # pos = find_pos_main('characters', 'm_fashi_pos_l2.png')
        # if len(pos) == 0:
        #     pos = find_pos_main('characters', 'm_fashi_pos_r2.png')
        logging.debug("where_am_i:%d,%s", len(pos), pos)
        if len(pos) > 0:
            # middle(pos)
            return pos
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
        if c%2 == 0:
            right_v2(diff)
        else:
            left_v2(diff)
        c = c+1

        # if c > m:
        #     return pos


def where_am_i_home(m=10):
    c = 0
    diff = 200
    step = 40
    dw = False
    while gcf.Gcfg.running:
        pos = find_pos_main('characters', 'my_pos.png',td=0.95)
        logging.debug("where_am_i_home:%d,%s", len(pos), pos)
        if len(pos) == 1:
            return pos
        sure_no_menu()
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

def skill_cycle(direction='n'):
    kb_util.skill('d', 1, delay=0.1)
    kb_util.skill('x', 5, delay=0.1)
    if direction=='r':
        right_v2(80)
    elif direction=='l':
        left_v2(0)
    kb_util.skill('s', 1, delay=0.1)
    kb_util.skill('x', 5, delay=0.1)

def skill_cycle_s():
    kb_util.skill('s', 1, delay=0.1)
    kb_util.skill('x', 5, delay=0.1)



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

def middle_v2(pos):
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


def wait_loading():
    while gcf.Gcfg.running:
        pos = find_pos_main( 'home', 'loading.png')
        logging.debug("loading:%d,%s", len(pos), pos)
        if len(pos) == 1:
            break
        screen.focus()
        kb_util.space(1, 0.1)
        pos = find_pos_main( 'home', 'start.png')
        logging.debug("start:%d,%s", len(pos), pos)
        if len(pos) >=1:
            # ms_util.click_first(pos)
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
            posz = find_pos_main( 'task', 'yiwancheng.png')
            logging.debug("yiwancheng task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                task = 'yiwancheng'
                logging.info("yiwancheng task find:%d,%s", len(posz), posz)
                return task

            posz = find_pos_main( 'task', 'zhuanzhi.png')
            logging.debug("zhuanzhi task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                task='zhuanzhi'
                logging.info("zhuanzhi task find:%d,%s", len(posz), posz)
                break

            posz = find_pos_main( 'task', 'zhuxian1.png')
            logging.debug("main task:%d,%s", len(posz), posz)
            if len(posz) == 1:
                logging.info("main task find:%d,%s", len(posz), posz)
                break
            # esc_clear()
            clear_menu()

        while gcf.Gcfg.running:
            ms_util.click_first(posz)
            pos = find_pos_main('task', 'zhuxian2.png')
            logging.debug("task direction:%d,%s", len(pos), pos)
            if len(pos) == 1:
                ms_util.click_first(pos)
                break
            clear_space()
            clear_confirm()
            time.sleep(1)

        # esc_clear()
        clear_menu()
        posq = find_pos_main('direction', 'qianjin.png')
        logging.debug("direction:%d,%s", len(posq), posq)
        if len(posq) == 1:
            logging.info("find direction:%d,%s", len(posq), posq)
            break

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


        esc_clear()


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


def follow_direction():
    while gcf.Gcfg.running:
        # screen.focus()
        me=where_am_i_home()
        pos = find_pos_main( 'direction', 'qianjin.png')
        if len(pos) == 0:
            pos = find_pos_main("task", "mission_g.png")
            if len(pos) > 0:
                logging.info("in mission")
                return 'mission'
            else:
                img = capture_main()
                pos = ac.find_all_template(img, mcfg.TASK_JIEJIN, threshold=0.9)
                if len(pos)==1:
                    tm=None
                    while gcf.Gcfg.running:
                        ms_util.click(pos[0]['result'][0], pos[0]['result'][1]+80)
                        tm = capture_main()
                        tp = ac.find_all_template(tm, mcfg.TASK_CLOSE, threshold=0.9)
                        if len(tp) == 1:
                            break

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

        d=screen.direction(pos)
        if d==1 or d==3:
            goto_xy_home_no(pos[0]['result'][0],pos[0]['result'][1],me[0])
        else:
            goto_xy_home(pos[0]['result'][0],pos[0]['result'][1],me[0])


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


def goto_xy_home(x,y,me=None):
    cp=me
    if me== None:
        cp=where_am_i_home()[0]
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

def goto_xy_home_no(x,y,me=None):
    cp=me
    if me== None:
        cp=where_am_i_home()[0]
    middle_v2_p(cp)
    dx=cx(cp)-x
    # dy=cy(cp)-y+40
    dy=mcfg.FIGHT_MIDDLE-y+40
    if dx > 0:
        left_v2(dx)
    else:
        right_v2(-dx)
    if dy>0:
        up_v2(dy)
    else:
        down_v2(-dy)

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
    while gcf.Gcfg.running:
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

def wait_in_main():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","find_main.png")
        if len(pos)>0:
            return 'zhuxian'
        pos = find_pos_main("task", "find_zhuanzhi.png")
        if len(pos) > 0:
            return 'zhuanzhi'
        kb_util.down(1)
        time.sleep(0.2)

def wait_in_zhuanzhi():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","find_zhuanzhi.png")
        if len(pos)>0:
            return
        kb_util.down(1)
        time.sleep(0.2)

def finish_yiwancheng():
    posz = find_pos_main('task', 'yiwancheng.png')
    logging.debug("yiwancheng task:%d,%s", len(posz), posz)
    if len(posz) == 1:
        ms_util.click_first(posz)
        clear_space()
        # kb_util.space(10,0.1)
        # time.sleep(0.5)
        clear_confirm()


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
    while gcf.Gcfg.running:
        pos=find_pos_main("task","renwuwancheng.png")
        logging.info("clear_to_mission:%s",pos)
        if len(pos)==1:
            return
        clear_menu()

def mission_to_home():
    while gcf.Gcfg.running:
        pos=find_pos_main("task","renwuwancheng.png")
        logging.info("mission_to_home:%s",pos)
        if len(pos)==0:
            return
        kb_util.skill('F12')



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
    pos = find_pos_finish('home', 'in_home_v2.png',td=0.9)
    logging.info("in_home_v2:%s",pos)
    if len(pos)>0:
        return False
    return True

def in_home():
    goto_menu()
    ms_util.click_up(mcfg.HOME_X,mcfg.HOME_Y)
    pos = find_pos_main('home', 'in_home.png',td=0.9)
    logging.debug("in_home:%s",pos)
    if len(pos)>0:
        return False
    return True



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()
    screen.focus()
    right_fight(400)
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
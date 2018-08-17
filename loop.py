import mcfg
import importlib
import logging
import os
import pyautogui
import cv2
import aircv as ac
from utils import *
import ops_util
import gcf
import time
import kb_util
import ms_util
import map
from finishthread import *

class Mission(object):
    def fight_circle(self, d):
        logging.info("fight_circle")
        start=time.time()
        while gcf.Gcfg.running:
            if self.ft.finish:
                return -1
            pos = ops_util.where_am_i()
            # ops_util.skill_cycle()
            if time.time() - start > 10:
                break
            else:
                if d == 1:
                    if self.reach_right(pos[0]):
                        ops_util.left_fight(400)
                        return 0
                    else:
                        ops_util.right_fight(400)
                        return 1
                else:
                    if self.reach_left(pos[0]):
                        ops_util.right_fight(400)
                        return 1
                    else:
                        ops_util.left_fight(400)
                        return 0

    def fight(self):
        logging.info("fight")
        d = 1
        s = time.time()
        pos = ops_util.go_middle_v2()
        if len(pos) > 0 and ops_util.cx(pos[0]) > 400:
            d = 0
            ops_util.left_v3(30)
        else:
            ops_util.right_v3(30)
        while gcf.Gcfg.running:
            d = self.fight_circle(d)
            # if self.ft.mexy==None or self.ft.mexy != (10, 10):
            #     self.pick_item()
            ops_util.go_middle_v2()
            if d== -1:
                break

    def reach_left(self,p):
        logging.debug("reach_left:%s",p)
        if p['result'][0]<300:
            return True
        else:
            return False

    def reach_left_door(self,p):
        logging.debug("reach_left:%s",p)
        if p['result'][0]<150:
            return True
        else:
            return False

    def reach_right(self,p):
        logging.debug("reach_right:%s",p)
        if p['result'][0]>500:
            return True
        else:
            return False

    def reach_right_door(self,p):
        logging.debug("reach_right:%s",p)
        if p['result'][0]>670:
            return True
        else:
            return False

    def pick_item(self):
        img=capture_param(0,250,800,300)
        pos = ac.find_all_template(img, mcfg.ITEM, threshold=0.95, rgb=False, bgremove=False)
        for p in pos:
            ops_util.goto_xy(p['result'][0] - 20, p['result'][1] + 250 - 100)
            kb_util.skill('x',4)


    def goto_x(self,p):
        cp=ops_util.where_am_i()[0]
        dx=ops_util.cx(cp)-ops_util.cx(p)
        if dx>0:
            ops_util.left_v3(dx)
        else:
            ops_util.right_v3(-dx)

    def goto_y(self,p):
        cp=ops_util.where_am_i()[0]
        # dy=ops_util.cy(cp)-ops_util.cy(p)-210
        dy=ops_util.cy(cp)-ops_util.cy(p)-60
        if dy>0:
            ops_util.up_v3(dy)
        else:
            ops_util.down_v3(-dy)

    def reach_next_room(self,index):
        if len(ops_util.in_esc())>0:
            return True
        x,y=map.xy_me()
        if self.path[index][1]!= x or self.path[index][2]!=y:
            return True
        return False

    def where_is_door(self):
        x,y=map.xy_me()
        for i in range(0,len(self.path)):
            if self.path[i][1] == x and self.path[i][2]==y:
                return self.path[i][0],i

    def next_door(self):
        door,index=self.where_is_door()
        logging.info("next door:%s,%d",door,index)
        ops_util.go_middle_v2()
        right_reached=False
        s=time.time()
        while gcf.Gcfg.running:
            if time.time()-s>15:
                return -1
            if self.reach_next_room(index):
                return 0
            if door=='l':
                logging.debug("left door")
                pos = ops_util.where_am_i()
                if self.reach_left_door(pos[0]):
                    p = self.ft.check_left_gate()
                    if p != None:
                        self.goto_y(p)
                        ops_util.left_v3(200)
                        continue
                else:
                    ops_util.left_v3(200)
                continue
            if door=='r':
                logging.debug("righ door")
                pos = ops_util.where_am_i()
                if self.reach_right_door(pos[0]):
                    p = self.ft.check_right_gate()
                    if p != None:
                        self.goto_y(p)
                        ops_util.right_v3(200)
                        continue
                else:
                    ops_util.right_v3(200)
                continue
            if door=='u':
                logging.debug("up door")
                p=self.ft.check_up_gate()
                if p!=None:
                    self.goto_x(p)
                    ops_util.up_v3(200)
                    ops_util.up_v3(200)
                    continue
                pos = ops_util.where_am_i()
                if right_reached!=True:
                    if self.reach_right(pos[0]):
                        right_reached=True
                    ops_util.right_v3(200)
                    continue
                pos = ops_util.where_am_i()
                if self.reach_left(pos[0]):
                    right_reached = False
                ops_util.left_v3(200)
            if door == 'd':
                logging.debug("down door")
                p = self.ft.check_down_gate()
                if p != None:
                    self.goto_x(p)
                    ops_util.down_v3(200)
                    ops_util.down_v3(200)
                    continue
                pos = ops_util.where_am_i()
                if right_reached != True:
                    if self.reach_right(pos[0]):
                        right_reached = True
                    ops_util.right_v3(200)
                    continue
                pos = ops_util.where_am_i()
                if self.reach_left(pos[0]):
                    right_reached = False
                ops_util.left_v3(200)


    def __init__(self, m_name):
        logging.info("mission name:%s", m_name)
        self.path=None
        self.ft=None
        if m_name=="zhuanzhi":
            self.path=[]
            for i in range(7,10):
                self.path.append(['r',i,10,0])

    def run(self):
        logging.info("mission run")
        while gcf.Gcfg.running:
            if ops_util.in_esc():
                ops_util.clear_menu()
            ops_util.clear_space()
            self.ft=FinishThread('ft',self.path)
            self.ft.setDaemon(True)
            self.ft.start()
            self.fight()
            if self.path==None:
                self.path=self.ft.path
            if self.ft.mexy==(10,10):
                #boos done
                logging.info("boss done")
                return
            else:
                self.next_door()

def pick_all():
    kb_util.skill('shiftright')
    kb_util.skill('shiftright')
    kb_util.skill('x',10)

def space_until(obj,end,final):
    while gcf.Gcfg.running:
        img=capture_main()
        pos = ac.find_all_template(img, obj, threshold=0.85)
        endpos = ac.find_all_template(img, end, threshold=0.85)
        logging.debug("space_until obj:%d,%s",len(pos),pos)
        logging.debug("space_until end:%d,%s",len(endpos),endpos)

        if len(endpos)==1:
            kb_util.space()
            time.sleep(0.5)
            img = capture_main()
            finalpos = ac.find_all_template(img, final, threshold=0.85)
            logging.debug("space_until finalpos:%d,%s", len(finalpos), finalpos)
            if len(finalpos) == 1:
                return finalpos
        elif len(pos)==1:
            ops_util.goto_xy_home_no(pos[0]['result'][0],pos[0]['result'][1])
            img = capture_main()
            endpos = ac.find_all_template(img, end, threshold=0.85)
            logging.debug("space_until endpos:%d,%s", len(endpos), endpos)
            if len(endpos) == 1:
                kb_util.space()
                time.sleep(0.5)
                img = capture_main()
                finalpos = ac.find_all_template(img, final, threshold=0.85)
                logging.debug("space_until finalpos:%d,%s", len(finalpos), finalpos)
                if len(finalpos)==1:
                    return finalpos

def click_until(pos,end):
    while gcf.Gcfg.running:
        ms_util.click_first(pos)
        time.sleep(0.5)
        img=capture_main()
        endpos = ac.find_all_template(img, end, threshold=0.85)
        logging.debug("click_until end:%d,%s",len(endpos),endpos)
        if len(endpos)==1:
            return endpos



def click_until_null(obj,td=0.7):
    while gcf.Gcfg.running:
        img=capture_main()
        pos = ac.find_all_template(img, obj, threshold=td)
        logging.debug("click_until_null end:%d,%s",len(pos),pos)
        if len(pos)==1:
            ms_util.click_first(pos)
            time.sleep(0.2)
        else:
            break


def click_until_down(pos,end):
    while gcf.Gcfg.running:
        ms_util.click_first_down(pos)
        time.sleep(0.5)
        img=capture_main()
        endpos = ac.find_all_template(img, end, threshold=0.85)
        logging.debug("click_until_down end:%d,%s",len(endpos),endpos)
        if len(endpos)==1:
            return endpos


def destroy_item():
    while gcf.Gcfg.running:
        pos = space_until(mcfg.ITEM_FENJIE0,mcfg.ITEM_SPACE,mcfg.ITEM_FENJIE)
        time.sleep(0.5)
        pos=click_until(pos,mcfg.ITEM_QUANBUFENJIE)
        qpos=pos
        # ms_util.move(pos[0]['result'][0],pos[0]['result'][1])
        pos = click_until_down(pos,mcfg.ITEM_FENJIE1)
        click_until_null(mcfg.ITEM_XIYOU,0.95)
        click_until_null(mcfg.ITEM_WODE,0.98)
        pos=click_until(qpos,mcfg.CLEAR_CONFIRM)
        pos=click_until_null(mcfg.CLEAR_CONFIRM)
        time.sleep(3)
        ops_util.esc_clear()
        break

def destroy_item_v2():
    while gcf.Gcfg.running:
        pos = space_until(mcfg.ITEM_FENJIE0,mcfg.ITEM_SPACE,mcfg.ITEM_FENJIE)
        time.sleep(0.5)
        kb_util.down(1,0.1)
        time.sleep(0.5)
        kb_util.space(1,0.1)
        time.sleep(0.5)
        kb_util.skill('a',delay=0.1)
        time.sleep(0.5)
        clear_confirm()
        time.sleep(3)
        ops_util.esc_clear()
        break


def fix_item():
    while gcf.Gcfg.running:
        pos = space_until(mcfg.ITEM_FENJIE0, mcfg.ITEM_SPACE, mcfg.ITEM_XIULI)
        time.sleep(0.5)
        kb_util.space(1, 0.1)
        # pos = click_until(pos, mcfg.ITEM_XIULI1)
        kb_util.skill('s',delay=0.1)
        time.sleep(0.5)
        clear_confirm()
        ops_util.esc_clear()
        break



def swith_item():

    ic=None
    while gcf.Gcfg.running:
        kb_util.skill('i', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.ITEM_PAGE, threshold=0.9)
        if len(ic)==1:
            break

    for i in range(0,8):
        for j in range(0,1):
            ms_util.click_up(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
            time.sleep(0.2)
            img=capture_main()
            pos=ac.find_all_template(img,mcfg.ITEM_USED,threshold=0.9)
            logging.debug("used,%d,%d,%s",i,j,pos)
            if len(pos)==0:
                ms_util.right_click(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
                time.sleep(0.2)
                if clear_confirm():
                    time.sleep(2)
                    ms_util.right_click(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
                logging.info("swith,%d,%d",i,j)
                time.sleep(0.2)
            else:
                pos = ac.find_all_template(img, mcfg.ITEM_SWITCHED, threshold=0.8)
                logging.debug("switched,%d,%d,%s", i, j, pos)
                if len(pos) > 0:
                    ms_util.right_click(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
                    time.sleep(0.2)
                    if clear_confirm():
                        time.sleep(2)
                        ms_util.right_click(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
                    logging.info("swith,%d,%d", i, j)
                    time.sleep(0.2)

    while gcf.Gcfg.running:
        kb_util.skill('i', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.ITEM_PAGE, threshold=0.9)
        if len(ic) == 0:
            break


def set_hot_key():
    kb_util.skill('enter')

    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init_dummp()
    # screen.focus()
    # screen.gen_speed()
    # m = Mission("M")
    # ft=FinishThread('ft',[])
    # ft.check_right_gate()
    # where_am_i()
    # m.pick_item()
    # swith_item()
    # destroy_item_v2()
    # fix_item()
    # exit(0)

    # screen.Screen.init()
    screen.Screen.init_dummp()
    screen.focus()
    # ops_util.wait_loading()
    ops_util.clear_menu()
    if not ops_util.in_home():
        ops_util.go_home()
    ops_util.clear_menu()
    screen.gen_speed()
    logging.info("speed:%d,%d", mcfg.SPEED_X,mcfg.SPEED_Y)

    while gcf.Gcfg.running:
        task = ops_util.main_task()
        if task=='yiwancheng':
            ops_util.finish_yiwancheng()
            continue
        fork=ops_util.follow_direction()
        if fork=='mission':
            # if task=='zhuanzhi':
            #     ops_util.wait_in_zhuanzhi()
            #     ops_util.wait_in_mission()
            #     m = Mission("zhuanzhi")
            #     m.run()
            #     ops_util.clear_to_mission()
            #     pick_all()
            #     ops_util.mission_to_home()
            #     ops_util.clear_menu()
            #     ops_util.sure_no_menu()
            # else:
                mission=ops_util.wait_in_main()
                ops_util.wait_in_mission()
                m=Mission(mission)
                m.run()
                ops_util.clear_to_mission()
                pick_all()
                ops_util.mission_to_home()
                ops_util.clear_menu()
                # ops_util.where_am_i_home(1000)
                swith_item()
                fix_item()
                destroy_item_v2()
                ops_util.sure_no_menu()
        elif fork=='zhuanzhi':
            logging.info("zhuanzhi")
            ops_util.zhuanzhi_dialog()
        elif fork=='dialog':
            ops_util.clear_space()
            ops_util.clear_confirm()



    # ops_util.mission_to_home()
    # ops_util.where_am_i_home(1000)
    # swith_item()
    # destroy_item()

    # logging.debug("mission name:%s", get_m_na me_in_mission())
    # swith_item()
    # destroy_item()
    # ops_util.go_middle_v2()
    # set_hot_key()
    # ops_util.where_am_i()
    # ops_util.left_v2(100)
    # ops_util.where_am_i()


    # m = Mission('M0')
    # m.run()
    # logging.info("mini map:%d", m.mini_map[6][6])
    # p = {}
    # p['result'] = (9.5, 10.8)
    # logging.debug("point:%s", right_point(get_point_in_mini_map(p)))
    # logging.debug("point:%s", left_point(get_point_in_mini_map(p)))
    # logging.debug("point:%s", up_point(get_point_in_mini_map(p)))
    # logging.debug("point:%s", down_point(get_point_in_mini_map(p)))
    # logging.debug("room index:%d", m.room_index((2,2)))
    # pad = ac.imread('pad.png')
    # diff1 = ac.imread('diff1.png')
    # diff2 = ac.imread('diff2.png')
    # diff = cv2.absdiff(diff1, diff2)
    # ac.show(diff)
    # fill_png(14,72,pad,diff)
    # ac.show(diff)
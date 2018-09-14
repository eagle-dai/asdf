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
from focusthread import *

class Mission(object):
    def fight_circle(self, d):
        logging.info("fight_circle")
        start=time.time()
        while gcf.Gcfg.running:
            if self.ft.finish:
                return -1
            pos = ops_util.where_am_i(d)
            ops_util.middle_v2(pos,d)
            if time.time() - start > 10:
                break
            else:
                if d == 1:
                    if self.reach_right(pos[0]):
                        if pos[0]['result'][0]>650:
                            ops_util.left_fight(350, self.ft)
                        else:
                            pass
                            # ops_util.right_fight(100,self.ft)
                        return 0
                    else:
                        if pos[0]['result'][0]>400:
                            ops_util.right_fight(650-pos[0]['result'][0], self.ft)
                        else:
                            ops_util.right_fight(350,self.ft)
                        return 1
                else:
                    if self.reach_left(pos[0]):
                        if pos[0]['result'][0]<150:
                            ops_util.right_fight(350, self.ft)
                        else:
                            pass
                            # ops_util.left_fight(100,self.ft)
                        return 1
                    else:
                        if pos[0]['result'][0] < 400:
                            ops_util.left_fight(pos[0]['result'][0]-150, self.ft)
                        else:
                            ops_util.left_fight(350, self.ft)
                        return 0

    def fight(self):
        logging.info("fight")
        d = 1
        s = time.time()
        pos = ops_util.go_middle_v2()
        if len(pos) > 0 and ops_util.cx(pos[0]) > 400:
            d = 0
            ops_util.left_v2(30)
        else:
            ops_util.right_v2(30)
        s=time.time()
        while gcf.Gcfg.running:
            screen.focus()
            if ops_util.in_esc() or ops_util.in_space() or ops_util.in_confirm():
                ops_util.clear_menu()
            dd = self.fight_circle(d)
            if dd!=d:
                d = dd
                s=time.time()
            elif time.time()-s>90:
                logging.info("time reached")
                if d==1:
                    d=0
                elif d==0:
                    d=1
            # if self.ft.mexy==None or self.ft.mexy != (10, 10):
            #     self.pick_item_v2()
            # ops_util.go_middle_v2()
            if d== -1:
                break
            # ops_util.go_middle_v2()


    def reach_left(self,p):
        logging.debug("reach_left:%s",p)
        if p['result'][0]<300:
            logging.info("left reached")
            return True
        else:
            return False

    def reach_right(self,p):
        logging.debug("reach_right:%s",p)
        if p['result'][0]>500:
            logging.info("right reached")
            return True
        else:
            return False

    def reach_left_door(self,p):
        logging.debug("reach_left:%s",p)
        if p['result'][0]<150:
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
            kb_util.skill('x',2)

    def pick_item_v2(self,door):
        logging.info("pick_item_v2")
        while gcf.Gcfg.running:
            pos = ops_util.where_am_i()
            if door == 'l'or door=='u' or door=='d':
                if self.reach_right(pos[0]):
                    break
                else:
                    ops_util.right_v3(200)
            else:
                if self.reach_left(pos[0]):
                    break
                else:
                    ops_util.left_v3(200)

        while gcf.Gcfg.running:
            img=capture_param(0,250,800,300)
            pos = ac.find_all_template(img, mcfg.ITEM, threshold=0.95, rgb=False, bgremove=False)
            for p in pos:
                ops_util.goto_xy(p['result'][0], p['result'][1] + 250)
                kb_util.skill('x',2)

            pos = ops_util.where_am_i()
            if door == 'l'or door=='u' or door=='d':
                if self.reach_left(pos[0]):
                    break
                else:
                    ops_util.left_v3(200)
            else:
                if self.reach_right(pos[0]):
                    break
                else:
                    ops_util.right_v3(200)

    def pick_item_v3(self,door):
        logging.info("pick_item_v3")
        s = time.time()
        s2 = s
        while gcf.Gcfg.running:
            if time.time()-s>15:
                break
            if time.time() - s2 > 3:
                s2=time.time()
                screen.focus()
            pos=go_middle_v2()
            if door == 'l'or door=='u' or door=='d':
                if self.reach_right(pos[0]):
                    break
                else:
                    if pos[0]['result'][0]<=500:
                        ops_util.right_v3(200)
            else:
                if self.reach_left(pos[0]):
                    break
                else:
                    if pos[0]['result'][0]>=250:
                        ops_util.left_v3(200)

        s = time.time()
        s2=s
        while gcf.Gcfg.running:
            if time.time()-s>15:
                break
            if time.time() - s2 > 5:
                s2 = time.time()
                screen.focus()
            img=capture_param(0,250,800,300)
            pos = ac.find_all_template(img, mcfg.ITEM, threshold=0.90, rgb=False, bgremove=False)
            for p in pos:
                # ops_util.go_middle_v2()
                ops_util.goto_xy_v3(p['result'][0]-50, p['result'][1]+285)
                kb_util.skill('x',2)
                continue


            pos = ops_util.where_am_i()
            if door == 'l'or door=='u' or door=='d':
                if self.reach_left(pos[0]):
                    break
                else:
                    if pos[0]['result'][0]>=250:
                        ops_util.left_v3(200)
            else:
                if self.reach_right(pos[0]):
                    break
                else:
                    if pos[0]['result'][0]<=500:
                        ops_util.right_v3(200)


    def goto_x(self,p):
        cp=ops_util.where_am_i()[0]
        dx=ops_util.cx(cp)-ops_util.cx(p)
        if dx>0:
            ops_util.left_v2(dx)
        else:
            ops_util.right_v2(-dx)

    def goto_y(self,p):
        cp=ops_util.where_am_i()[0]
        dy=ops_util.cy(cp)-(ops_util.cy(p)+200)
        if dy>0:
            ops_util.up_v2(dy)
        else:
            ops_util.down_v2(-dy)

    def reach_next_room(self,index):
        logging.debug("reach_next_room")
        if len(ops_util.in_esc())>0:
            return True
        x,y=map.xy_me()
        if self.path[index][1]!= x or self.path[index][2]!=y:
            logging.debug("reach_next_room done")
            return True
        return False

    def reach_next_room2(self,xy):
        logging.debug("reach_next_room2")
        if len(ops_util.in_esc())>0:
            return True
        x,y=map.xy_me()
        if xy[0]!= x or xy[1]!=y:
            logging.info("reach_next_room2 done")
            return True
        return False

    def where_is_door(self):
        x,y=map.xy_me()
        for i in range(0,len(self.path)):
            if self.path[i][1] == x and self.path[i][2]==y:
                return self.path[i][0],i
        return None


    def where_is_door2(self,lastxy,curxy):
        if lastxy[0]==curxy[0]:
            if lastxy[1]==curxy[1]+1:
                return 'd'
            else:
                return 'u'
        else:
            if lastxy[0] == curxy[0] + 1:
                return 'r'
            else:
                return 'l'


    def next_door(self):
        nd = self.where_is_door()
        not_found=False
        curxy = None
        door = None
        index=-1
        if nd==None:
            lastxy = self.lastft.mexy
            curxy = map.xy_me()
            door = self.where_is_door2(lastxy,curxy)
            not_found = True
        else:
            door,index=nd
        logging.info("next door:%s,%d",door,index)
        ops_util.go_middle_v2()
        # self.pick_item_v3(door)
        right_reached=False
        s=time.time()
        while gcf.Gcfg.running:
            if time.time()-s>30:
                return -1
            if not_found:
                if self.reach_next_room2(curxy):
                    return 0
            else:
                if self.reach_next_room(index):
                    return 0

            if door=='l':
                logging.debug("left door")
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if self.reach_left_door(pos[0]):
                    p = self.ft.check_left_gate()
                    if p != None:
                        self.goto_y(p)
                        ops_util.right_v2(20)
                        ops_util.left_v3(200)
                        continue
                    else:
                        ops_util.right_v2(20)
                        ops_util.left_v3(200)
                else:
                    ops_util.right_v2(20)
                    ops_util.left_v3(200)
                continue
            if door=='r':
                logging.debug("righ door")
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if self.reach_right_door(pos[0]):
                    p = self.ft.check_right_gate()
                    if p != None:
                        self.goto_y(p)
                        ops_util.left_v2(20)
                        ops_util.right_v3(200)
                        continue
                    else:
                        ops_util.left_v2(20)
                        ops_util.right_v3(200)
                else:
                    ops_util.left_v2(20)
                    ops_util.right_v3(200)
                continue
            if door=='u':
                logging.debug("up door")
                p=self.ft.check_up_gate()
                if p!=None:
                    self.goto_x(p)
                    ops_util.up_v3(150)
                    ops_util.up_v3(150)
                    continue
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if right_reached!=True:
                    if self.reach_right(pos[0]):
                        right_reached=True
                    ops_util.left_v2(20)
                    ops_util.right_v3(200)
                    continue
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if self.reach_left(pos[0]):
                    right_reached = False
                ops_util.right_v2(20)
                ops_util.left_v3(200)
            if door == 'd':
                logging.debug("down door")
                p = self.ft.check_down_gate()
                if p != None:
                    self.goto_x(p)
                    ops_util.down_v3(150)
                    ops_util.down_v3(150)
                    continue
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if right_reached != True:
                    if self.reach_right(pos[0]):
                        right_reached = True
                    ops_util.left_v2(20)
                    ops_util.right_v3(200)
                    continue
                pos = ops_util.where_am_i()
                middle_v2(pos)
                if self.reach_left(pos[0]):
                    right_reached = False
                ops_util.right_v2(20)
                ops_util.left_v3(200)


    def __init__(self, m_name):
        logging.info("mission name:%s", m_name)
        self.path=None
        self.e = None
        self.ft=None
        self.lastft = None
        if m_name=="zhuanzhi":
            self.path=[]
            for i in range(7,10):
                self.path.append(['r',i,10,0])

    def run(self):
        logging.info("mission run")
        while gcf.Gcfg.running:
            if ops_util.in_esc() or ops_util.in_space() or ops_util.in_confirm():
                ops_util.clear_menu()

            ops_util.clear_space()
            self.lastft=self.ft
            self.ft=FinishThread('ft',self.path,self.e)
            self.ft.setDaemon(True)
            self.ft.start()
            self.fight()
            if self.path==None:
                self.path=self.ft.path
            if self.e==None:
                self.e=self.ft.e
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
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s > 15:
            break
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
            ops_util.goto_xy_home_dialog(pos[0]['result'][0], pos[0]['result'][1])
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
    return None

def click_until(pos,end):
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s > 15:
            break
        ms_util.click_first(pos)
        time.sleep(0.5)
        img=capture_main()
        endpos = ac.find_all_template(img, end, threshold=0.85)
        logging.debug("click_until end:%d,%s",len(endpos),endpos)
        if len(endpos)==1:
            return endpos



def click_until_null(obj,td=0.7):
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s > 15:
            break
        img=capture_main()
        pos = ac.find_all_template(img, obj, threshold=td)
        logging.debug("click_until_null end:%d,%s",len(pos),pos)
        if len(pos)==1:
            ms_util.click_first(pos)
            time.sleep(0.2)
        else:
            break


def click_until_down(pos,end):
    s=time.time()
    while gcf.Gcfg.running:
        if time.time()-s > 15:
            break
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
        ops_util.clear_menu()
        break

def destroy_item_v2():
    while gcf.Gcfg.running:
        pos = space_until(mcfg.ITEM_FENJIE0,mcfg.ITEM_SPACE,mcfg.ITEM_FENJIE)
        time.sleep(0.5)
        kb_util.down(1,0.1)
        time.sleep(0.5)
        kb_util.space(1,0.1)
        time.sleep(0.5)
        img = capture_main()
        endpos = ac.find_all_template(img, mcfg.ITEM_QUANBUFENJIE, threshold=0.85)
        if len(endpos) ==0:
            break
        # screen.focus()
        # ms_util.click_first(endpos)
        click_until_down(endpos,mcfg.ITEM_FENJIE1)
        click_until_null(mcfg.ITEM_XIYOU2, 0.95)
        click_until_null(mcfg.ITEM_XIYOU, 0.95)
        click_until_null(mcfg.ITEM_WODE, 0.98)
        # ms_util.click_first(endpos)
        # time.sleep(0.5)
        # screen.focus()
        # time.sleep(0.5)
        # screen.focus()
        kb_util.skill('a',delay=0.1)
        time.sleep(0.5)
        clear_confirm()
        time.sleep(3)
        ops_util.clear_menu()
        break


def fix_item():
    while gcf.Gcfg.running:
        pos = space_until(mcfg.ITEM_FENJIE0, mcfg.ITEM_SPACE, mcfg.ITEM_XIULI)
        if pos == None:
            clear_menu()
            continue
        time.sleep(0.5)
        kb_util.space(1, 0.1)
        # pos = click_until(pos, mcfg.ITEM_XIULI1)
        kb_util.skill('s',delay=0.1)
        time.sleep(0.5)
        clear_confirm()
        ops_util.clear_menu()
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


def learn_skill():

    ic=None
    while gcf.Gcfg.running:
        kb_util.skill('k', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.SKILL_PAGE, threshold=0.9)
        if len(ic)==1:
            break
        ops_util.clear_menu()
    time.sleep(0.5)

    # ms_util.move_and_click(100,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(180,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(220,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(260,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(310,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(350,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(390,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(430,150)
    # time.sleep(0.5)
    # ms_util.move_and_click(470,150)
    # time.sleep(0.5)

    # ms_util.move_and_click(145,220)
    # time.sleep(0.3)
    # img = capture_main()
    # pos = ac.find_all_template(img, mcfg.SKILL_LEARN, threshold=0.98)
    # logging.debug("skill：%s",pos)
    # if len(pos) == 1:
    #     ms_util.click_first(pos)
    #     # ms_util.move_and_click(pos[0]['result'][0],pos[0]['result'][1])
    # time.sleep(0.3)
    #
    #
    # ms_util.move_and_click(240,220)
    # time.sleep(0.3)
    # img = capture_main()
    # pos = ac.find_all_template(img, mcfg.SKILL_LEARN, threshold=0.98)
    # logging.debug("skill：%s",pos)
    # if len(pos) == 1:
    #     ms_util.click_first(pos)
    #     ms_util.move_and_click(pos[0]['result'][0],pos[0]['result'][1])
    # time.sleep(0.3)
    # return

    skill_pos=[(50,285),(425,280),(145,220),(240,220),(100,150)]
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
    ops_util.clear_confirm()

    while gcf.Gcfg.running:
        kb_util.skill('k', 1, 0.2)
        img = capture_main()
        ic = ac.find_all_template(img, mcfg.SKILL_PAGE, threshold=0.9)
        if len(ic) == 0:
            break

def set_hot_key():
    kb_util.skill('enter')

    pass

def get_char_name():
    pos = ops_util.find_pos_main('item', 'sel_char2.png',td=0.95)
    logging.info("pos:%s",pos)
    if len(pos)==0:
        return None
    x,y=pos[0]['rectangle'][0]
    y=y-24
    char=ops_util.capture_param(x,y,119,11)
    # ac.show(char)
    # return
    #148 185 209
    bm = np.ndarray((char.shape[1]),dtype=np.uint8)
    for i in range(0,bm.shape[0]):
        bm[i]=0
    for i in range(0,char.shape[1]):
        for j in range(0,char.shape[0]):
            # print(char[j][i][0],char[j][i][1],char[j][i][2])
            if char[j][i][0]==148 and char[j][i][1]==185 and char[j][i][2]==209:
                bm[i]=1
        # print('\n')

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
    # ac.show(res)
    # ac.show(char)
    print(start,end)
    return res

def start_guaji():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(thread)s %(filename)s][line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    screen.Screen.init()
    mcfg.MY_IMG=get_char_name()
    screen.focus()
    ops_util.wait_loading()
    # screen.focus()
    # screen.Screen.init_dummp()
    ops_util.clear_menu()
    if not ops_util.in_home():
        ops_util.go_home()
        while gcf.Gcfg.running:
            if ops_util.in_home_v2():
                break
            time.sleep(0.2)
            ops_util.clear_menu()
    ops_util.clear_menu()
    screen.gen_speed()
    logging.info("speed:%d,%d", mcfg.SPEED_X,mcfg.SPEED_Y)

    ss=time.time()
    while gcf.Gcfg.running:
        if time.time()-ss>30*60:
            logging.info("gen_speed")
            screen.gen_speed()
            ss = time.time()
        task = ops_util.main_task()
        if task=='yiwancheng':
            logging.info("yiwancheng")
            ops_util.finish_yiwancheng()
            continue
        if task == 'shoudong1':
            logging.info("shoudong1")
            goto_menu()
            screen.focus()
            ts = time.time()
            while gcf.Gcfg.running:
                if time.time()-ts>5:
                    screen.focus()
                logging.debug("to character")
                ms_util.click(390, 460)
                ms_util.click(390, 460)
                time.sleep(2)
                pos = ops_util.find_pos_main('screen', 'top.png')
                if len(pos)==1:
                    break
            char = ops_util.find_pos_main('item', 'sel_char.png',td=0.97)
            logging.info("char:%s",pos)
            screen.focus()
            ops_util.wait_loading(char)
            ops_util.clear_menu()
            ops_util.clear_menu()
            ops_util.up_v2(150)
            kb_util.space(1, 0.1)
            ops_util.clear_menu()
            logging.info("shoudong1 finish")
            continue
        fork=ops_util.follow_direction()
        if fork=='mission':
            logging.info("mission:")
            mission=ops_util.wait_in_main()
            ops_util.wait_in_mission()
            m=Mission(mission)
            m.run()
            screen.focus()
            ops_util.clear_to_mission()
            screen.focus()
            pick_all()
            ops_util.mission_to_home()
            ops_util.clear_menu()
            if mission=="zhuanzhi":
                time.sleep(2)
                clear_menu()
                # learn_skill()

            swith_item()
            fix_item()
            if mission=="zhuanzhi":
                swith_item()
            destroy_item_v2()
            ops_util.sure_no_menu()
        elif fork=='zhuanzhi':
            logging.info("zhuanzhi")
            # ops_util.zhuanzhi_dialog()
            ops_util.zhuanzhi_dialog_guijiansi()
        elif fork=='dialog':
            logging.info("dialog")
            ops_util.jiejin_until(mcfg.TASK_JIEJIN)
            ops_util.clear_space()
            ops_util.clear_confirm()
            ops_util.clear_menu()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(thread)s %(filename)s][line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    start_guaji()
    exit(0)
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init_dummp()
    # screen.focus()
    # learn_skill()
    # exit(0)
    # destroy_item_v2()
    # exit(0)
    # screen.gen_speed()
    # m = Mission("M")
    # m.pick_item_v3('r')
    # exit(0)
    # ft=FinishThread('ft',[])
    # ft.check_right_gate()
    # where_am_i()
    # m.pick_item()
    # swith_item()
    # destroy_item_v2()
    # fix_item()
    # exit(0)

    screen.Screen.init()
    # screen.Screen.init_dummp()
    screen.focus()
    # focus = FocusThread('focus')
    # focus.setDaemon(True)
    # focus.start()
    ops_util.wait_loading()
    ops_util.clear_menu()
    if not ops_util.in_home():
        ops_util.go_home()
        while gcf.Gcfg.running:
            if ops_util.in_home_v2():
                break
            time.sleep(0.2)
            ops_util.clear_menu()
    ops_util.clear_menu()
    screen.gen_speed()
    logging.info("speed:%d,%d", mcfg.SPEED_X,mcfg.SPEED_Y)

    ss=time.time()
    while gcf.Gcfg.running:
        if time.time()-ss>30*60:
            screen.gen_speed()
            ss = time.time()
        task = ops_util.main_task()
        if task=='yiwancheng':
            ops_util.finish_yiwancheng()
            continue
        if task == 'shoudong1':
            goto_menu()
            screen.focus()
            ts = time.time()
            while gcf.Gcfg.running:
                if time.time()-ts>5:
                    screen.focus()
                logging.debug("to character")
                ms_util.click(390, 460)
                ms_util.click(390, 460)
                time.sleep(2)
                pos = ops_util.find_pos_main('screen', 'top.png')
                if len(pos)==1:
                    break
            char = ops_util.find_pos_main('item', 'sel_char.png',td=0.97)
            logging.info("char:%s",pos)
            screen.focus()
            ops_util.wait_loading(char)
            ops_util.clear_menu()
            ops_util.clear_menu()
            ops_util.up_v2(150)
            kb_util.space(1, 0.1)
            ops_util.clear_menu()
            logging.info("shoudong1 finish")
            continue
        fork=ops_util.follow_direction()
        if fork=='mission':
            mission=ops_util.wait_in_main()
            ops_util.wait_in_mission()
            m=Mission(mission)
            m.run()
            screen.focus()
            ops_util.clear_to_mission()
            screen.focus()
            pick_all()
            ops_util.mission_to_home()
            ops_util.clear_menu()
            if mission=="zhuanzhi":
                time.sleep(2)
                clear_menu()
                learn_skill()

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
            ops_util.clear_menu()



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
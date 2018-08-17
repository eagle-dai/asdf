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

def instance(module_name, class_name, *args, **kwargs):
    module_meta = importlib.import_module(module_name)
    module_meta = __import__(module_name, globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    obj = class_meta(*args, **kwargs)
    return obj

def fill_png(c,s,pad,img):
    for i in range(0, c):
        for j in range(0, c):
            for k in range(0, s):
                for l in range(0, s):
                    if img[i*s+k][j*s+l][0] != 0 or img[i*s+k][j*s+l][1] != 0 or img[i*s+k][j*s+l][2] !=0:
                        img[i*s+k][j*s+l][0] = pad[k][l][0]
                        img[i*s+k][j*s+l][1] = pad[k][l][1]
                        img[i*s+k][j*s+l][2] = pad[k][l][2]
    return img

def fill_png_v2(w,h,s,pad,img):
    count=0
    for i in range(0, h):
        for j in range(0, w):
            for k in range(0, s):
                for l in range(0, s):
                    # if img[i*s+k][j*s+l][0] != 0 or img[i*s+k][j*s+l][1] != 0 or img[i*s+k][j*s+l][2] !=0:
                    if img[i * s + k][j * s + l][0] + img[i * s + k][j * s + l][1] + img[i * s + k][j * s + l][2] > 30:
                        img[i*s+k][j*s+l][0] = pad[k][l][0]
                        img[i*s+k][j*s+l][1] = pad[k][l][1]
                        img[i*s+k][j*s+l][2] = pad[k][l][2]
                        count+=1
    return img

def get_m_name_in_select():
    fs = os.listdir(resource_path('mission'))
    img = capture_param(650, 480, 150, 24)
    found=None
    width=0
    for f in fs:
        if f.endswith('.png'):
            obj = ac.imread(resource_path('mission',f))
            pos = ac.find_all_template(img, obj, threshold=0.9)
            if len(pos) == 1:
                if obj.shape[1]>width:
                    found=f
                    width=obj.shape[2]
    return found.rstrip('.png')


def get_m_name_in_mission():
    fs = os.listdir(resource_path('mission'))
    img = capture_param(600, 0, 150, 24)
    found=None
    width=0
    for f in fs:
        if f.endswith('.png'):
            obj = ac.imread(resource_path('mission',f))
            logging.debug("mission:%s",f)
            pos = ac.find_all_template(img, obj, threshold=0.95)
            logging.debug("pos,%s", pos)
            if len(pos) == 1:
                logging.debug("abs,%f",abs(150-43-pos[0]['result'][0]-obj.shape[1]))
                # if abs(150-43-pos[0]['result'][0]-obj.shape[1])<5:
                #     found=f
                #     break
                if obj.shape[1]>width:
                    found=f
                    width=obj.shape[2]
    return found.rstrip('.png')


def get_point_in_mini_map(p):
    x = int(p['result'][0] / mcfg.MINI_MAP_SLOT_SIZE)
    y = int(p['result'][1] / mcfg.MINI_MAP_SLOT_SIZE)

    return x, y

def right_point(pt):
    return pt[0]+1,pt[1]

def left_point(pt):
    return pt[0]-1,pt[1]

def up_point(pt):
    return pt[0],pt[1]-1

def down_point(pt):
    return pt[0],pt[1]+1

class Room(object):
    def __init__(self, r_name):
        logging.info("room name:%s", r_name)
        self.r = getattr(mcfg,r_name)
        self.r_i = -1
        self.m_r_png = None
        self.m_l_png = None
        self.m = None

    def test(self):
        logging.debug("test")

    def fight_circle(self, d):
        logging.info("fight_circle")
        start=time.time()
        while gcf.Gcfg.running:
            if self.finished():
                return -1
            ops_util.skill_cycle()
            if time.time() - start > 10:
                break
            else:
                pos = ops_util.where_am_i()
                if d == 1:
                    if self.reach_right(pos[0]):
                        self.check_up_gate()
                        ops_util.left_v2(10)
                        return 0
                    else:
                        ops_util.right_v2(150)
                        return 1
                else:
                    if self.reach_left(pos[0]):
                        ops_util.right_v2(10)
                        return 1
                    else:
                        ops_util.left_v2(150)
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
        while gcf.Gcfg.running:
            ops_util.go_middle_v2()
            d = self.fight_circle(d)
            if self.r['finish_mode']!=mcfg.FINISH_MODE_BOSS:
                self.pick_item()
            if d== -1:
                break

    def run(self):
        logging.info("%s run", self.r['room_name'])
        if self.r['esc_needed']:
            ops_util.esc_clear()
        self.fight()

    def reach_left(self,p):
        logging.debug("reach_left:%s",p)
        if p['result'][0]<self.r['margin'][0]:
            return True
        else:
            return False

    def reach_right(self,p):
        logging.debug("reach_right:%s",p)
        if p['result'][0]>self.r['margin'][1]:
            return True
        else:
            return False

    def finished(self):
        if self.r['finish_mode']==mcfg.FINISH_MODE_QUESTION or self.r['finish_mode']==mcfg.FINISH_MODE_UPGATE:
            img = capture_param(
                mcfg.MINI_MAP_X-self.m.m['size'][0]*mcfg.MINI_MAP_SLOT_SIZE,
                mcfg.MINI_MAP_Y,
                self.m.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
                self.m.m['size'][1] * mcfg.MINI_MAP_SLOT_SIZE
            )
            pos = ac.find_all_template(img, mcfg.QUESTION, threshold=0.7, rgb=False, bgremove=False)
            logging.debug("question finished:%d,%s", len(pos), pos)
            if len(pos) > 0:
                return True
            if self.r['finish_mode'] == mcfg.FINISH_MODE_UPGATE:
                if self.check_up_gate()!=None:
                    return True
        elif self.r['finish_mode']==mcfg.FINISH_MODE_MINI_MAP:
            ts = time.time()
            img1 = capture_param(
                mcfg.MINI_MAP_X-self.m.m['size'][0]*mcfg.MINI_MAP_SLOT_SIZE,
                mcfg.MINI_MAP_Y,
                self.m.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
                self.m.m['size'][1] * mcfg.MINI_MAP_SLOT_SIZE
            )
            for i in range(0, 3):
                img2 = capture_param(
                    mcfg.MINI_MAP_X - self.m.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
                    mcfg.MINI_MAP_Y,
                    self.m.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
                    self.m.m['size'][1] * mcfg.MINI_MAP_SLOT_SIZE
                )
                diff = cv2.absdiff(img1, img2)
                # ac.show(diff)
                fill_png_v2(self.m.m['size'][0],self.m.m['size'][1], mcfg.MINI_MAP_SLOT_SIZE, mcfg.PAD1, diff)
                pos = ac.find_all_template(diff, mcfg.PAD1, threshold=0.7, rgb=False, bgremove=False)
                logging.debug("minimap finished:%d,%s", len(pos), pos)
                if len(pos) > 0:
                    # ac.show(img1)
                    # ac.show(img2)
                    # ac.show(diff)
                    return True
        elif self.r['finish_mode']==mcfg.FINISH_MODE_DOOR:
            pass
        elif self.r['finish_mode']==mcfg.FINISH_MODE_BOSS:
            img = capture_param(
                mcfg.MINI_MAP_X-self.m.m['size'][0]*mcfg.MINI_MAP_SLOT_SIZE,
                mcfg.MINI_MAP_Y,
                self.m.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
                self.m.m['size'][1] * mcfg.MINI_MAP_SLOT_SIZE
            )
            pos = ac.find_all_template(img, mcfg.FINAL, threshold=0.7, rgb=False, bgremove=False)
            logging.debug("question finished:%d,%s", len(pos), pos)
            if len(pos) == 0:
                return True

        return False


    def pick_item(self):
        img=capture_param(0,250,800,300)
        pos = ac.find_all_template(img, mcfg.ITEM, threshold=0.95, rgb=False, bgremove=False)
        for p in pos:
            ops_util.goto_xy(p['result'][0] - 20, p['result'][1] + 250 - 100)
            kb_util.skill('x',4)


    def check_up_gate(self):
        obj = cv2.imread(ops_util.resource_path('task', 'door_f_u.png'))
        s = time.time()
        for i in range(0, 5):
            img=capture_param(0,140,800,100)
            pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
            logging.debug("check_up_gate:%d,%s", len(pos), pos)
            if len(pos)>0:
                return pos[0]

        return None

    def check_down_gate(self):
        obj = cv2.imread(ops_util.resource_path('task', 'door_f_d.png'))
        s = time.time()
        while time.time()-s<0.5:
        # for i in range(0, 5):
            img=capture_param(0,420,800,100)
            pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
            logging.debug("check_down_gate:%d,%s", len(pos), pos)
            if len(pos)>0:
                return pos[0]

        return None

    def goto_x(self,p):
        cp=ops_util.where_am_i()[0]
        dx=ops_util.cx(cp)-ops_util.cx(p)
        if dx>0:
            ops_util.left_v2(dx)
        else:
            ops_util.right_v2(-dx)

    def reach_next_room(self):
        new_pos = self.m.position()
        if len(new_pos) > 0:
            n_i = self.m.room_index(get_point_in_mini_map(new_pos[0]))
            if self.r_i != n_i:
                return True
        else:
            return True
        return False



    def next_door(self):
        logging.info("%s next door", self.r['room_name'])
        ops_util.go_middle_v2()
        right_reached=False
        s=time.time()
        while gcf.Gcfg.running:
            if time.time()-s>15:
                return -1
            if self.reach_next_room():
                    return 0
            if len(self.r['next_door_path'])==0:
                if self.m.m['room_path'][self.r_i]=='l':
                    logging.debug("left door")
                    ops_util.left_v2(200)
                    continue
                if self.m.m['room_path'][self.r_i]=='r':
                    logging.debug("righ door")
                    ops_util.right_v2(200)
                    continue
                if self.m.m['room_path'][self.r_i]=='u':
                    logging.debug("up door")
                    p=self.check_up_gate()
                    if p!=None:
                        self.goto_x(p)
                        ops_util.up_v2(150)
                        continue
                    pos = ops_util.where_am_i()
                    if right_reached!=True:
                        if self.reach_right(pos[0]):
                            right_reached=True
                        ops_util.right_v2(200)
                        continue
                    pos = ops_util.where_am_i()
                    if self.reach_left(pos[0]):
                        right_reached = False
                    ops_util.left_v2(200)
                if self.m.m['room_path'][self.r_i] == 'd':
                    logging.debug("down door")
                    p = self.check_down_gate()
                    if p != None:
                        self.goto_x(p)
                        ops_util.down_v2(150)
                        continue
                    pos = ops_util.where_am_i()
                    if right_reached != True:
                        if self.reach_right(pos[0]):
                            right_reached = True
                        ops_util.right_v2(200)
                        continue
                    pos = ops_util.where_am_i()
                    if self.reach_left(pos[0]):
                        right_reached = False
                    ops_util.left_v2(200)
            # else:
            #     for path in self.r['next_door_path']:
            #         if path[0] == 'm':
            #             ops_util.go_middle()
            #         elif path[0]=='l':
            #             pass
            #         elif path[0]=='r':
            #             if path[1]==-1:
            #                 while gcf.Gcfg.running:
            #                     if self.reach_right():
            #                         ops_util.right_v2(200)
            #                         break
            #                     ops_util.right_v2(200)
            #             else:
            #                 ops_util.right_v2(path[1])
            #         elif path[0]=='u':
            #             ops_util.right_v2(path[1])
            #         elif path[0]=='d':
            #             pass



class Mission(object):
    def __init__(self, m_name):
        logging.info("mission name:%s", m_name)
        self.m = getattr(mcfg,m_name)
        self.r = []
        # self.r_i = -1
        # self.mini_map = [
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0]
        # ]
        self.real_path = []
        for i in range(0, self.m['room_count']):
            r = Room(m_name + 'R' + str(i))
            r.m=self
            self.r.append(r)

    def run(self):
        logging.info("%s run", self.m['mission_name'])

        while gcf.Gcfg.running:
            ops_util.esc_clear()
            while gcf.Gcfg.running:
                pos=self.position()
                if len(pos)>0:
                    break
            x,y=get_point_in_mini_map(pos[0])
            # if first_get!=True:
            #     first_get=True
            #     if x!=self.m['start_point'][0] or y!=self.m['start_point'][1]:
            #         logging.info("2nd mission")
            #         self.m['start_point']=self.m['start_point1']
            #         self.m['size']=self.m['size1']
            #         self.m['end_point']=self.m['end_point1']
            #         self.m['room_count']=self.m['room_count1']
            #         self.m['room_path']=self.m['room_path1']

            # assert x==self.m['start_point'][0] and y==self.m['start_point'][1]
            ri = self.room_index(get_point_in_mini_map(pos[0]))
            self.r[ri].r_i=ri
            self.r[ri].run()
            if self.r[ri].r['finish_mode']==mcfg.FINISH_MODE_BOSS:
                logging.info("finish one mission")
                ops_util.esc_clear()
                ops_util.wait_till_next_mission()
                return
            else:
                done=self.r[ri].next_door()
                if done==-1:
                    continue

            if self.r[ri].r['sleep']>0:
                s=time.time()
                while gcf.Gcfg.running:
                    ops_util.skill_cycle()
                    if time.time()-s>self.r[ri].r['sleep']:
                        break

    def position(self):
        img = capture_param(
            mcfg.MINI_MAP_X - self.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            self.m['size'][0] * mcfg.MINI_MAP_SLOT_SIZE,
            self.m['size'][1] * mcfg.MINI_MAP_SLOT_SIZE
        )
        pos = ac.find_all_template(img, mcfg.ME, threshold=0.6, rgb=False, bgremove=False)
        if len(pos) == 0:
            pos = ac.find_all_template(img, mcfg.FINAL, threshold=0.6, rgb=False, bgremove=False)
        logging.debug("postion:%d,%s", len(pos), pos)
        return pos

    def finished(self):
        pass

    def room_index(self,pt):
        s_pt = self.m['start_point']
        path = self.m['room_path']
        logging.debug("room_path:%s",path)


        for i in range(0, len(path)+1):
            if pt[0] == s_pt[0] and pt[1] == s_pt[1]:
                logging.info("room index:%d",i)
                return i
            if path[i] == 'l':
                s_pt = left_point(s_pt)
            elif path[i] == 'r':
                s_pt = right_point(s_pt)
            elif path[i] == 'u':
                s_pt = up_point(s_pt)
            elif path[i] == 'd':
                s_pt = down_point(s_pt)

        return -1






class Game(object):
    PAD = None
    def __init__(self):
        pass

def pick_all():
    kb_util.skill('shiftright')
    kb_util.skill('shiftright')
    kb_util.skill('x',10)
    kb_util.skill('F12',5)
    time.sleep(2)



def test_pick_item():
    img=capture_param(0,250,800,300)
    pos = ac.find_all_template(img, mcfg.ITEM, threshold=0.95, rgb=False, bgremove=False)
    logging.debug("ic:%d,%s",len(pos),pos)
    for p in pos:
        ops_util.goto_xy(p['result'][0]-20,p['result'][1]+250-100)
        kb_util.skill('x', 4)

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
            ops_util.goto_xy(pos[0]['result'][0],pos[0]['result'][1])
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

        # img = capture_main()
        # pos = ac.find_all_template(img, mcfg.ITEM_XIYOU, threshold=0.95)
        # logging.debug("xiyou,%d,%s",len(pos),pos)
        # if len(pos)>0:
        #     ms_util.click_first(pos)
        # time.sleep(0.5)
        break


    # img = capture_main()
    # pos = ac.find_all_template(img, mcfg.ITEM_XIYOU, threshold=0.95)
    # logging.debug("xiyou,%d,%s",len(pos),pos)
    # if len(pos)>0:
    #     ms_util.click_first(pos)
    # time.sleep(0.5)
    #
    # pos = ac.find_all_template(img, mcfg.ITEM_WODE, threshold=0.98)
    # logging.debug("wode,%d,%s",len(pos),pos)
    # if len(pos)>0:
    #     ms_util.click_first(pos)
    #
    # ms_util.click(200,330)
    # ms_util.click(200,330)
    # time.sleep(0.5)
    # ops_util.esc_clear()



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
                logging.info("swith,%d,%d",i,j)
                time.sleep(0.2)
            else:
                pos = ac.find_all_template(img, mcfg.ITEM_SWITCHED, threshold=0.8)
                logging.debug("switched,%d,%d,%s", i, j, pos)
                if len(pos) > 0:
                    ms_util.right_click(ic[0]['result'][0]-59+20+i*mcfg.ITEM_SIZE,ic[0]['result'][1]+20+j*mcfg.ITEM_SIZE)
                    logging.info("swith,%d,%d", i, j)
                    time.sleep(0.2)

            # kb_util.skill('i', 1, 0.2)
            # screen.focus()

def set_hot_key():
    kb_util.skill('enter')

    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()
    screen.focus()
    # logging.debug("mission name:%s", get_m_na me_in_mission())
    # test_pick_item()
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
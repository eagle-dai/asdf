from threading import *
import map
import aircv as ac
import cv2
from ops_util import *
import ops_util
import logging
import os

class FinishThread(Thread):
    def __init__(self, name, path, ff, *args):
        super(FinishThread, self).__init__(name=name)
        self.data = args
        self.path=path
        self.gate=None
        self.finish=False
        self.mexy=None
        self.e = ff


    def check_up_gate(self):
        fs = os.listdir(resource_path('door'))
        doors=[]
        for f in fs:
            if f.startswith('door_f_u'):
                doors.append(ac.imread(resource_path('door', f)))
        s = time.time()
        while time.time()-s<0.5:
            img=capture_param(0,140,800,200)
            for obj in doors:
                pos = ac.find_all_template(img, obj, threshold=0.95, rgb=False, bgremove=False)
                if len(pos)>0:
                    logging.debug("check_up_gate:%d,%s", len(pos), pos)
                    return pos[0]
            # time.sleep(0.1)
        return None

    def check_down_gate(self):
        fs = os.listdir(resource_path('door'))
        doors=[]
        for f in fs:
            if f.startswith('door_f_d'):
                doors.append(ac.imread(resource_path('door', f)))
        s = time.time()
        while time.time()-s<0.5:
            img=capture_param(0,420,800,100)
            for obj in doors:
                pos = ac.find_all_template(img, obj, threshold=0.95, rgb=False, bgremove=False)
                if len(pos)>0:
                    logging.debug("check_down_gate:%d,%s", len(pos), pos)
                    return pos[0]
            # time.sleep(0.1)

        return None

    def check_left_gate(self):
        fs = os.listdir(resource_path('door'))
        doors=[]
        for f in fs:
            if f.startswith('door_f_l'):
                doors.append(ac.imread(resource_path('door', f)))
        s = time.time()
        while time.time() - s < 0.5:
            img = capture_param(0, 150, 150, 450)
            for obj in doors:
                pos = ac.find_all_template(img, obj, threshold=0.97, rgb=False, bgremove=False)
                if len(pos) > 0:
                    logging.debug("check_left_gate:%d,%s", len(pos), pos)
                    return pos[0]
            # time.sleep(0.1)

        return None

    def check_right_gate(self):
        fs = os.listdir(resource_path('door'))
        doors=[]
        for f in fs:
            if f.startswith('door_f_r'):
                doors.append(ac.imread(resource_path('door', f)))
        s = time.time()
        while time.time() - s < 0.5:
            img = capture_param(650, 150, 150, 450)
            for obj in doors:
                pos = ac.find_all_template(img, obj, threshold=0.95, rgb=False, bgremove=False)
                if len(pos) > 0:
                    logging.debug("check_right_gate:%d,%s", len(pos), pos)
                    return pos[0]
            # time.sleep(0.1)

        return None

    def where_is_door(self):
        for p in self.path:
            if p[1]==self.mexy[0] and p[2]==self.mexy[1]:
                return p[0]
        return 'unknown'

    def finished(self):
        me=map.position_me_n()
        if me!=None:
            self.mexy=map.xy(me,self.e)
            logging.debug("mexy:%s", self.mexy)

        if self.mexy == (10, 10) and time.time()-self.sts>15:
            pos = map.position_final_n()
            if pos == None:
                if len(ops_util.in_esc())>0:
                    clear_menu()
                    return False
                else:
                    return True
            else:
                return False

        pos = find_pos_main("task","renwuwancheng.png")
        if len(pos) >0:
            self.mexy=(10,10)
            return True

        img = capture_param(
            mcfg.MINI_MAP_X - 7 * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            7 * mcfg.MINI_MAP_SLOT_SIZE,
            7 * mcfg.MINI_MAP_SLOT_SIZE
        )
        pos = ac.find_all_template(img, mcfg.QUESTION, threshold=0.8, rgb=False, bgremove=False)
        # logging.debug("postion question:%d,%s", len(pos), pos)
        if len(pos)>0:
            return True

        direction=self.where_is_door()
        if direction=='u':
            self.gate=self.check_up_gate()
            if self.gate== None:
                self.gate=self.check_down_gate()
            if self.gate== None:
                self.gate=self.check_left_gate()
            if self.gate== None:
                self.gate=self.check_right_gate()
        elif direction=='d':
            self.gate=self.check_down_gate()
            if self.gate== None:
                self.gate=self.check_up_gate()
            if self.gate== None:
                self.gate=self.check_left_gate()
            if self.gate== None:
                self.gate=self.check_right_gate()
        elif direction=='l':
            self.gate=self.check_left_gate()
            if self.gate== None:
                self.gate=self.check_up_gate()
            if self.gate== None:
                self.gate=self.check_down_gate()
            if self.gate== None:
                self.gate=self.check_right_gate()
        elif direction=='r':
            self.gate = self.check_up_gate()
            if self.gate== None:
                self.gate = self.check_down_gate()
            if self.gate== None:
                self.gate = self.check_left_gate()
            if self.gate== None:
                self.gate = self.check_right_gate()
        else:
            self.gate=self.check_up_gate()
            if self.gate== None:
                self.gate=self.check_down_gate()
            if self.gate== None:
                self.gate=self.check_left_gate()
            if self.gate== None:
                self.gate=self.check_right_gate()

        if self.gate!= None:
            return True

        return False

    def run(self):
        logging.info("runinng")
        self.sts=time.time()
        if self.path==None:
            while gcf.Gcfg.running:
                try:
                    self.path=map.check_path()
                    break
                except:
                    continue

        self.mexy=map.xy_me()
        if self.e == None:
            self.e = map.position_final()
        logging.debug("mexy:%s", self.mexy)
        while gcf.Gcfg.running:
            if self.finished():
                logging.info("finish room:%s", self.mexy)
                self.finish=True
                break
            img = capture_main()
            pos = ac.find_all_template(img, mcfg.TASK_JIANQI2, threshold=0.8, rgb=False, bgremove=False)
            if len(pos)==1:
                pos = ac.find_all_template(img, mcfg.TASK_JIANQI, threshold=0.8, rgb=False, bgremove=False)
                if len(pos) == 0:
                    kb_util.skill('f')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()

    screen.focus()
    img = capture_main()
    pos = ac.find_all_template(img, mcfg.TASK_JIANQI2, threshold=0.8, rgb=False, bgremove=False)
    logging.debug("pos:%d",len(pos))
    if len(pos) == 1:
        pos = ac.find_all_template(img, mcfg.TASK_JIANQI, threshold=0.8, rgb=False, bgremove=False)
        logging.debug("pos:%d", len(pos))
        if len(pos) == 0:
            kb_util.skill('f')
    exit(0)
    ops_util.in_home_v2()
    td=FinishThread('ft',None)
    # td.check_right_gate()




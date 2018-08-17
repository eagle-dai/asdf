from threading import *
import map
import aircv as ac
import cv2
from ops_util import *
import ops_util
import logging
import os

class FinishThread(Thread):
    def __init__(self, name, path, *args):
        super(FinishThread, self).__init__(name=name)
        self.data = args
        self.path=path
        self.gate=None
        self.finish=False
        self.mexy=None


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
                pos = ac.find_all_template(img, obj, threshold=0.95, rgb=False, bgremove=False)
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

    def finished(self):
        me=map.position_me_n()
        if me!=None:
            self.mexy=map.xy_me()

        if self.mexy == (10, 10) and time.time()-self.sts>15:
            pos = map.position_final_n()
            if pos == None:
                if ops_util.in_esc():
                    clear_menu()
                    return False
                else:
                    return True
            else:
                return False


        img = capture_param(
            mcfg.MINI_MAP_X - 7 * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            7 * mcfg.MINI_MAP_SLOT_SIZE,
            7 * mcfg.MINI_MAP_SLOT_SIZE
        )
        pos = ac.find_all_template(img, mcfg.QUESTION, threshold=0.8, rgb=False, bgremove=False)
        logging.debug("postion question:%d,%s", len(pos), pos)
        if len(pos)>0:
            return True

        direction=self.where_is_door()
        if direction=='u':
            self.gate=self.check_up_gate()

        if direction=='d':
            self.gate=self.check_down_gate()

        if direction=='l':
            self.gate=self.check_left_gate()

        if direction=='r':
            self.gate=self.check_right_gate()

        if self.gate!= None:
            return True

        return False

    def run(self):
        self.sts=time.time()
        if self.path==None:
            self.path=map.check_path()
        self.mexy=map.xy_me()
        while gcf.Gcfg.running:
            if self.finished():
                logging.info("finish room:%s", self.mexy)
                self.finish=True
                break


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')
    # screen.Screen.init()
    screen.Screen.init_dummp()
    screen.focus()
    td=FinishThread('ft',None)
    td.check_left_gate()




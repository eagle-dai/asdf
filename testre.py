import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import ms_util
import screen
import ops_util
from ops_util import *
import nm
import mcfg
import gcf


def check_screen():
    img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    obj = cv2.imread(ops_util.resource_path('task', 'ic.png'))
    pos = ac.find_all_template(img, obj, threshold=0.95, rgb=False, bgremove=False)
    logging.debug("%d,%s", len(pos), pos)
    screen.show(img, pos)


def check_gate():
    obj = cv2.imread(ops_util.resource_path('task', 'door_f_v2.png'))
    s = time.time()
    for i in range(0,5):
        img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        pos = ac.find_all_template(img, obj, threshold=0.9, rgb=False, bgremove=False)
        logging.debug("check_gate:%d,%s", len(pos), pos)
        # screen.show(img, pos)
    logging.info("cost:%f", time.time()-s)

def check_finish():
    # xy = (650, 480, 150, 24)
    # xy = (600, 0, 150, 24)
    # screen.Screen.init()
    screen.Screen.init_dummp()
    xy = (667, 29, 126, 126)


    pad = cv2.imread(ops_util.resource_path('task', 'fill1.png'))

    # img = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img1 = ops_util.capture_param(
        mcfg.MINI_MAP_X - 4 * mcfg.MINI_MAP_SLOT_SIZE,
        mcfg.MINI_MAP_Y,
        4 * mcfg.MINI_MAP_SLOT_SIZE,
        4 * mcfg.MINI_MAP_SLOT_SIZE
    )
    ac.show(img1)

    time.sleep(0.2)
    img2 = ops_util.capture_param(
        mcfg.MINI_MAP_X - 4 * mcfg.MINI_MAP_SLOT_SIZE,
        mcfg.MINI_MAP_Y,
        4 * mcfg.MINI_MAP_SLOT_SIZE,
        4 * mcfg.MINI_MAP_SLOT_SIZE
    )
    ac.show(img2)

    diff = cv2.absdiff(img1, img2)
    ac.show(diff)
    logging.debug("shape:%s",diff.shape)
    logging.debug("shape:%s",pad.shape)
    nm.fill_png_v2(4,4, 18, pad, diff)

    pos = ac.find_all_template(diff, pad, threshold=0.5, rgb=False, bgremove=False)
    logging.debug("%d,%s", len(pos), pos)

    screen.show(diff, pos)

    obj = cv2.imread(ops_util.resource_path('mission', 'M1.png'))
    pos = ac.find_all_template(diff, obj, threshold=0.7, rgb=False, bgremove=False)
    logging.debug("%d,%s", len(pos), pos)
    screen.show(diff, pos)

def position_start_end_diff():
    s=position_me()
    e=position_final()
    x=(s['result'][0]-e['result'][0])/18
    y=(s['result'][1]-e['result'][1])/18
    logging.debug('position_start_end_diff:%d,%d',x,y)
    return int(x),int(y)

def position_me():
    while gcf.Gcfg.running:
        img = capture_param(
            mcfg.MINI_MAP_X - 7 * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            7 * mcfg.MINI_MAP_SLOT_SIZE,
            7 * mcfg.MINI_MAP_SLOT_SIZE
        )
        pos = ac.find_all_template(img, mcfg.ME4X10, threshold=0.8, rgb=False, bgremove=False)
        logging.debug("postion me:%d,%s", len(pos), pos)
        if len(pos)>0:
            return pos[0]

def position_final():
    while gcf.Gcfg.running:
        img = capture_param(
            mcfg.MINI_MAP_X - 7 * mcfg.MINI_MAP_SLOT_SIZE,
            mcfg.MINI_MAP_Y,
            7 * mcfg.MINI_MAP_SLOT_SIZE,
            7 * mcfg.MINI_MAP_SLOT_SIZE
        )
        pos = ac.find_all_template(img, mcfg.FINAL, threshold=0.8, rgb=False, bgremove=False)
        logging.debug("postion final:%d,%s", len(pos), pos)
        if len(pos)>0:
            return pos[0]

def check_map_a():
    # xy = (650, 480, 150, 24)
    # xy = (600, 0, 150, 24)
    # screen.Screen.init()
    screen.Screen.init_dummp()
    ra = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    ra[10][10]='ff'
    rar = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

    img1 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img1 = cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR)

    time.sleep(0.2)
    img2 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

    # ac.show(img2)

    diff = cv2.absdiff(img1, img2)
    # ac.show(diff)

    mff = cv2.imread(ops_util.resource_path('task', 'mff.png'))
    mlr = cv2.imread(ops_util.resource_path('task', 'mlr.png'))
    mud = cv2.imread(ops_util.resource_path('task', 'mud.png'))
    mul = cv2.imread(ops_util.resource_path('task', 'mul.png'))
    mur = cv2.imread(ops_util.resource_path('task', 'mur.png'))
    mdl = cv2.imread(ops_util.resource_path('task', 'mdl.png'))
    mdr = cv2.imread(ops_util.resource_path('task', 'mdr.png'))


    pmff = ac.find_all_template(diff, mff, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmff %d,%s", len(pmff), pmff)
    pmlr = ac.find_all_template(diff, mlr, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmlr %d,%s", len(pmlr), pmlr)
    pmud = ac.find_all_template(diff, mud, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmud %d,%s", len(pmud), pmud)
    pmul = ac.find_all_template(diff, mul, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmul %d,%s", len(pmul), pmul)
    pmur = ac.find_all_template(diff, mur, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmur %d,%s", len(pmur), pmur)
    pmdl = ac.find_all_template(diff, mdl, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmdl %d,%s", len(pmdl), pmdl)
    pmdr = ac.find_all_template(diff, mdr, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("pmdr %d,%s", len(pmdr), pmdr)
    # screen.show(diff, pmlr)

    for p in pmlr:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("lr:x,y:%d,%d",x,y)
        ra[10+x][10+y]='lr'

    for p in pmud:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("ud:x,y:%d,%d",x,y)
        ra[10+x][10+y]='ud'

    for p in pmul:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("ul:x,y:%d,%d",x,y)
        ra[10+x][10+y]='ul'

    for p in pmur:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("ur:x,y:%d,%d",x,y)
        ra[10+x][10+y]='ur'

    for p in pmdl:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("dl:x,y:%d,%d",x,y)
        ra[10+x][10+y]='dl'

    for p in pmdr:
        x=int((p['result'][0]-pmff[0]['result'][0])/18)
        y=int((p['result'][1]-pmff[0]['result'][1])/18)
        logging.info("dr:x,y:%d,%d",x,y)
        ra[10+x][10+y]='dr'

    path=[]
    ix=10
    iy=10
    while True:
        if ra[ix][iy-1]!=0 and rar[ix][iy-1]==0:#u
            if ra[ix][iy-1].find('d') !=-1:
                if ra[ix][iy]=='ff':
                    path.insert(0,'d')
                    rar[ix][iy]=1
                    iy=iy-1
                    continue
                elif ra[ix][iy].find('u')!=-1:
                    path.insert(0,'d')
                    rar[ix][iy]=1
                    iy=iy-1
                    continue
        if ra[ix][iy+1]!=0 and rar[ix][iy+1]==0:
            if ra[ix][iy+1].find('u') !=-1:
                if ra[ix][iy]=='ff':
                    path.insert(0,'u')
                    rar[ix][iy] = 1
                    iy=iy+1
                    continue
                elif ra[ix][iy].find('d')!=-1:
                    path.insert(0,'u')
                    rar[ix][iy] = 1
                    iy=iy+1
                    continue
        if ra[ix-1][iy]!=0 and rar[ix-1][iy]==0:
            if ra[ix-1][iy].find('r') != -1:
                if ra[ix][iy] == 'ff':
                    path.insert(0, 'r')
                    rar[ix][iy] = 1
                    ix = ix-1
                    continue
                elif ra[ix][iy].find('l')!=-1:
                    path.insert(0, 'r')
                    rar[ix][iy] = 1
                    ix = ix-1
                    continue
        if ra[ix+1][iy]!=0 and rar[ix+1][iy]==0:
            if ra[ix + 1][iy].find('l') != -1:
                if ra[ix][iy] == 'ff':
                    path.insert(0, 'l')
                    rar[ix][iy] = 1
                    ix = ix + 1
                    continue
                elif ra[ix][iy].find('r')!=-1:
                    path.insert(0, 'l')
                    rar[ix][iy] = 1
                    ix = ix + 1
                    continue

        if ra[ix][iy]=='lr':
            if rar[ix-1][iy]==1:
                path.insert(0,'l')
            if rar[ix+1][iy]==1:
                path.insert(0,'r')
        if ra[ix][iy] == 'ud':
            if rar[ix][iy-1] == 1:
                path.insert(0, 'u')
            if rar[ix][iy+1] == 1:
                path.insert(0, 'd')
        if ra[ix][iy] == 'ul':
            if rar[ix][iy-1] == 1:
                path.insert(0, 'r')
            if rar[ix-1][iy] == 1:
                path.insert(0, 'd')
        if ra[ix][iy] == 'ur':
            if rar[ix][iy-1] == 1:
                path.insert(0, 'l')
            if rar[ix + 1][iy] == 1:
                path.insert(0, 'd')
        if ra[ix][iy] == 'dl':
            if rar[ix][iy+1] == 1:
                path.insert(0, 'r')
            if rar[ix + 1][iy] == 1:
                path.insert(0, 'u')
        if ra[ix][iy] == 'dr':
            if rar[ix +1][iy] == 1:
                path.insert(0, 'u')
            if rar[ix][iy+1] == 1:
                path.insert(0, 'l')

        break

    logging.info("path:%s",path)


def check_path():
    res=None
    while gcf.Gcfg.running:
        pos=ops_util.find_pos_main('task','map.png',td=0.9)
        if len(pos)==2:
            break
        kb_util.skill('n',delay=0.1)
    while gcf.Gcfg.running:
        ra = [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ]
        ra[10][10]='ff'

        img1 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img1 = cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR)

        time.sleep(0.2)
        img2 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
        img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

        diff = cv2.absdiff(img1, img2)
        # ac.show(diff)

        mff = cv2.imread(ops_util.resource_path('task', 'mff.png'))
        mlr = cv2.imread(ops_util.resource_path('task', 'mlr.png'))
        mud = cv2.imread(ops_util.resource_path('task', 'mud.png'))
        mul = cv2.imread(ops_util.resource_path('task', 'mul.png'))
        mur = cv2.imread(ops_util.resource_path('task', 'mur.png'))
        mdl = cv2.imread(ops_util.resource_path('task', 'mdl.png'))
        mdr = cv2.imread(ops_util.resource_path('task', 'mdr.png'))

        mlur = cv2.imread(ops_util.resource_path('task', 'mlur.png'))
        murd = cv2.imread(ops_util.resource_path('task', 'murd.png'))
        mrdl = cv2.imread(ops_util.resource_path('task', 'mrdl.png'))
        mdlu = cv2.imread(ops_util.resource_path('task', 'mdlu.png'))


        pmff = ac.find_all_template(diff, mff, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmff %d,%s", len(pmff), pmff)
        pmlr = ac.find_all_template(diff, mlr, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmlr %d,%s", len(pmlr), pmlr)
        pmud = ac.find_all_template(diff, mud, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmud %d,%s", len(pmud), pmud)
        pmul = ac.find_all_template(diff, mul, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmul %d,%s", len(pmul), pmul)
        pmur = ac.find_all_template(diff, mur, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmur %d,%s", len(pmur), pmur)
        pmdl = ac.find_all_template(diff, mdl, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmdl %d,%s", len(pmdl), pmdl)
        pmdr = ac.find_all_template(diff, mdr, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmdr %d,%s", len(pmdr), pmdr)

        pmlur = ac.find_all_template(diff, mlur, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmlur %d,%s", len(pmlur), pmlur)
        pmurd = ac.find_all_template(diff, murd, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmurd %d,%s", len(pmurd), pmurd)
        pmrdl = ac.find_all_template(diff, mrdl, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmrdl %d,%s", len(pmrdl), pmrdl)
        pmdlu = ac.find_all_template(diff, mdlu, threshold=0.90, rgb=False, bgremove=False)
        logging.debug("pmdlu %d,%s", len(pmdlu), pmdlu)


        # screen.show(diff, pmlr)

        for p in pmlr:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("lr:x,y:%d,%d",x,y)
            ra[10+x][10+y]='lr'

        for p in pmud:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("ud:x,y:%d,%d",x,y)
            ra[10+x][10+y]='ud'

        for p in pmul:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("ul:x,y:%d,%d",x,y)
            ra[10+x][10+y]='ul'

        # screen.show(diff, pmur)
        for p in pmur:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("ur:x,y:%d,%d",x,y)
            ra[10+x][10+y]='ur'

        for p in pmdl:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("dl:x,y:%d,%d",x,y)
            ra[10+x][10+y]='dl'

        for p in pmdr:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("dr:x,y:%d,%d",x,y)
            ra[10+x][10+y]='dr'

        ###
        for p in pmlur:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("lur:x,y:%d,%d",x,y)
            ra[10+x][10+y]='lur'

        for p in pmurd:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("urd:x,y:%d,%d",x,y)
            ra[10+x][10+y]='urd'

        for p in pmrdl:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("rdl:x,y:%d,%d",x,y)
            ra[10+x][10+y]='rdl'

        for p in pmdlu:
            x=int((p['result'][0]-pmff[0]['result'][0])/18)
            y=int((p['result'][1]-pmff[0]['result'][1])/18)
            logging.info("dlu:x,y:%d,%d",x,y)
            ra[10+x][10+y]='dlu'

        dx,dy=position_start_end_diff()
        ra[dx+10][dy+10]='ss'

        ps=[]
        path=[]
        ix=10
        iy=10
        gen_path(ra,dx+10,dy+10,path,ps)
        logging.debug("check path:%s", ps)
        for p in ps:
            if len(p)>=4:
                res=p
            if res != None:
                if len(p)<len(res):
                    res=p
        if res != None:
            break

    while gcf.Gcfg.running:
        pos=ops_util.find_pos_main('task','map.png',td=0.9)
        if len(pos)==1:
            break
        kb_util.skill('n',delay=0.1)

    return res

def circled(path,x,y):
    for i in path:
        if i[1]==x and i[2]==y:
            return True
    return False


def gen_path(ra,ix,iy,path,ps):
    lpath=path[:]
    if ra[ix][iy]=='ss' or ra[ix][iy].find('u')!=-1:
        if ra[ix][iy-1]!=0:
            if ra[ix][iy - 1]=='ff':
                lpath.append(('u', ix, iy))
                ps.append(lpath)
                logging.debug("gen_path:%d,%s", len(lpath),lpath)
                return
            elif ra[ix][iy-1].find('d') !=-1:
                if not circled(path, ix, iy-1):
                    lpath.append(('u', ix, iy))
                    gen_path(ra,ix,iy-1,lpath,ps)

    lpath=path[:]
    if ra[ix][iy] == 'ss' or ra[ix][iy].find('d') != -1:
        if ra[ix][iy+1]!=0:
            if ra[ix][iy+1]=='ff':
                lpath.append(('d', ix, iy))
                ps.append(lpath)
                logging.debug("gen_path:%d,%s", len(lpath),lpath)
                return
            elif ra[ix][iy+1].find('u') !=-1:
                if not circled(path, ix, iy + 1):
                    lpath.append(('d', ix, iy))
                    gen_path(ra,ix,iy+1,lpath,ps)

    lpath=path[:]
    if ra[ix][iy] == 'ss' or ra[ix][iy].find('l') != -1:
        if ra[ix-1][iy]!=0:
            if ra[ix-1][iy] == 'ff':
                lpath.append(('l', ix, iy))
                ps.append(lpath)
                logging.debug("gen_path:%d,%s", len(lpath),lpath)
                return
            elif ra[ix-1][iy].find('r') != -1:
                if not circled(path, ix-1, iy):
                    lpath.append(('l', ix, iy))
                    gen_path(ra, ix-1, iy, lpath,ps)

    lpath=path[:]
    if ra[ix][iy] == 'ss' or ra[ix][iy].find('r') != -1:
        if ra[ix+1][iy] != 0:
            if ra[ix+1][iy] == 'ff':
                lpath.append(('r', ix, iy))
                ps.append(lpath)
                logging.debug("gen_path:%d,%s", len(lpath),lpath)
                return
            elif ra[ix+1][iy].find('l') != -1:
                if not circled(path, ix+1, iy):
                    lpath.append(('r', ix, iy))
                    gen_path(ra, ix+1, iy, lpath,ps)


def check_map():
    # xy = (650, 480, 150, 24)
    # xy = (600, 0, 150, 24)
    # screen.Screen.init()
    screen.Screen.init_dummp()

    pad = cv2.imread(ops_util.resource_path('task', 'mdr.png'))

    img1 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img1 = cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR)

    time.sleep(0.2)
    img2 = pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

    ac.show(img2)

    diff = cv2.absdiff(img1, img2)
    ac.show(diff)


    pos = ac.find_all_template(diff, pad, threshold=0.90, rgb=False, bgremove=False)
    logging.debug("%d,%s", len(pos), pos)

    screen.show(diff, pos)

def test_speed():
    ops_util.up_v2(200)
    time.sleep(0.5)
    pos1 = ops_util.find_pos_main('characters', 'my_pos.png')
    s = time.time()
    while True:
        pyautogui.keyDown("down", 0.05)
        if time.time() - s >= 1:
            break
    pyautogui.keyUp("down", 0.01)
    time.sleep(0.5)
    pos2 = ops_util.find_pos_main('characters', 'my_pos.png')

    logging.info("speedY:%f", pos2[0]['result'][1]-pos1[0]['result'][1])

def test_speedX():
    pos1 = ops_util.find_pos_main('characters', 'my_pos.png')
    s = time.time()
    while True:
        pyautogui.keyDown("left", 0.05)
        if time.time() - s >= 1:
            break
    pyautogui.keyUp("left", 0.01)
    time.sleep(0.5)
    pos2 = ops_util.find_pos_main('characters', 'my_pos.png')

    logging.info("speedX:%f", pos2[0]['result'][0]-pos1[0]['result'][0])


def test_walk():

    pos1 = ops_util.find_pos_main('characters', 'my_pos.png')
    ops_util.right_v3(110)
    # ops_util.left_v3(110)

    time.sleep(0.5)
    pos2 = ops_util.find_pos_main('characters', 'my_pos.png')
    logging.info("speed XS:%f", pos2[0]['result'][0]-pos1[0]['result'][0])
    logging.info("speed YS:%f", pos2[0]['result'][1]-pos1[0]['result'][1])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # input("press any key to start:")
    # screen.Screen.init()
    # exit(0)
    screen.Screen.init_dummp()
    screen.focus()
    ops_util.up_v3(150)

    # test_walk()
    exit(0)
    screen.gen_speed()
    exit(0)
    a=(8,9)
    b=(8,9)
    logging.debug("%d",a==b)
    # time.sleep(1)
    test_speed()
    # 225,150,150,120

    # test_speedX()
    # position_me()
    # position_final()
    # dx,dy=position_start_end_diff()

    # check_path()

    # input("press any key to start:")
    # ops_util.where_am_i()


    # check_gate()
    # exit(0)
    # check_screen()
    # exit(0)
    # check_finish()
    # exit(0)
    # check_map_a()
    # exit(0)





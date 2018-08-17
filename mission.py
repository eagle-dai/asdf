import mission_util
import logging
import ops_util
import gcf
import time

class Room(object):
    def __init__(self, index):
        self.index = index
        self.me_pos = None
        self.last = False

    def clear(self):
        pass

    def fight_circle(self, d):
        logging.info("fight_circle")
        start = time.time()
        while gcf.Gcfg.running:
            if len(self.me_pos) == 0:
                if mission_util.boss_finished():
                    return -1
            else:
                if mission_util.room_finished(self.me_pos):
                    return -1
            ops_util.skill_cycle()
            now = time.time()
            if now - start > 3:
                if d == 1:
                    if ops_util.am_i_stuck_right():
                        ops_util.skill_cycle()
                        ops_util.left(30)
                        return 0
                    else:
                        for i in range(0, 2):
                            ops_util.skill_cycle()
                            ops_util.right(300)
                        return 1
                else:
                    if ops_util.am_i_stuck_left():
                        ops_util.skill_cycle()
                        ops_util.right(30)
                        return 1
                    else:
                        for i in range(0, 2):
                            ops_util.skill_cycle()
                            ops_util.left(300)
                        return 0

    def reach_next_room(self):
        pos = ops_util.my_pos()
        ret = False
        if len(pos) != 0:
            ret = ops_util.same_pos(pos[0], self.me_pos[0])
        else:
            if self.last:
                ret = False
            else:
                ops_util.esc_clear()
                ret = True
        logging.debug("reach_next_room:%d,%d,%d", ret, len(pos), len(self.me_pos))
        return ret

    def fight(self):
        logging.info("fight")
        d = 1
        s = time.time()
        self.me_pos = ops_util.my_pos()
        if len(self.me_pos) > 0:
            endp = ops_util.end_pos()
            diff = ops_util.diff_pos(self.me_pos[0], endp[0])
            logging.debug("romm diff:%d", diff)
            if diff < 20:
                logging.info("last room")
                self.last = True
        else:
            logging.info("boss room")

        pos = ops_util.go_middle()
        if len(pos) >= 1 and ops_util.cx(pos[0]) > 400:
            d = 0
        while gcf.Gcfg.running:
            d = self.fight_circle(d)
            pos = ops_util.go_middle()
            if d== -1:
                break


    def next_room(self, dl):
        logging.info("next room")
        for d in dl:
            if d == 0:
                while gcf.Gcfg.running:
                    logging.info("left door")
                    if self.reach_next_room() != True:
                        return
                    if ops_util.am_i_stuck_left():
                        ops_util.left(400)
                    else:
                        ops_util.left(400)
                        continue
                    if self.reach_next_room() != True:
                        return
                    ops_util.up(200)
                    if self.reach_next_room() != True:
                        return
                    ops_util.down(400)
            elif d == 1:
                while gcf.Gcfg.running:
                    logging.info("up door")
                    if self.reach_next_room() != True:
                        return
                    ops_util.up(200)
                    while gcf.Gcfg.running:
                        if ops_util.am_i_stuck_right():
                            for i in range(0,12):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.up(30)
                                ops_util.right(50)
                            break
                        else:
                            for i in range(0,5):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.up(30)
                                ops_util.right(100)
                            continue

                    while gcf.Gcfg.running:
                        if ops_util.am_i_stuck_left():
                            for i in range(0, 12):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.up(30)
                                ops_util.left(50)
                            break
                        else:
                            for i in range(0, 5):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.up(30)
                                ops_util.left(100)
                            continue
            elif d == 2:
                while gcf.Gcfg.running:
                    logging.info("right door")
                    if self.reach_next_room() != True:
                        return
                    if ops_util.am_i_stuck_right():
                        ops_util.right(400)
                    else:
                        ops_util.right(400)
                        continue
                    if self.reach_next_room() != True:
                        return
                    ops_util.up(200)
                    if self.reach_next_room() != True:
                        return
                    ops_util.down(400)
            elif d == 3:
                while gcf.Gcfg.running:
                    logging.info("down door")
                    if self.reach_next_room() != True:
                        return
                    ops_util.down(200)
                    while gcf.Gcfg.running:
                        if ops_util.am_i_stuck_right():
                            for i in range(0,12):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.down(30)
                                ops_util.right(50)
                            break
                        else:
                            for i in range(0,5):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.down(30)
                                ops_util.right(100)
                            continue

                    while gcf.Gcfg.running:
                        if ops_util.am_i_stuck_left():
                            for i in range(0, 12):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.down(30)
                                ops_util.left(50)
                            break
                        else:
                            for i in range(0, 5):
                                if self.reach_next_room() != True:
                                    return
                                ops_util.down(30)
                                ops_util.left(100)
                            continue

class Mission(object):
    def __init__(self, name, directions):
        self.name = name
        self.directions = directions
        self.rooms = []
        self.start_pos = None
        self.end_pos = None
        self.path = []

    def where_is_next_room(self, mpos):
        r = []
        pos = ops_util.question_pos()

        if len(pos) == 0:
            pos = ops_util.end_pos()

        if len(pos) == 0:
            return r
        elif len(pos) == 2:
            r.append(1)

        for p in pos:
            r.append(ops_util.direction(p, mpos[0]))
        return r

    def init_rooms(self):
        self.start_pos = ops_util.my_pos()[0]
        logging.info('start pos: %s', self.start_pos)
        self.end_pos = ops_util.end_pos()[0]
        logging.info('end pos: %s', self.end_pos)

        for i in range(0, 20):
            r = Room(i)
            self.rooms.append(r)

    def run_mission(self):
        while gcf.Gcfg.running:
            ops_util.esc_clear()
            r = self.rooms[len(self.path)]
            r.fight()
            logging.info("finish one room")
            if len(r.me_pos) == 0:
                logging.info("boss is killed")
                logging.info("room path:%s", self.path)
                ops_util.esc_clear()
                return
            d = self.where_is_next_room(r.me_pos)
            r.next_room(d)
            self.path.append(d[0])



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - [%(levelname)s]: [%(message)s]')  # logging.basicConfig函数对日志的输出格式及方式做相关配置

    logging.debug("%d %s", 1, 'abc')
    logging.info('this is a loggging info message')
    logging.debug('this is a loggging debug message')
    logging.warning('this is loggging a warning message')
    logging.error('this is an loggging error message')
    logging.critical('this is a loggging critical message 好的呢')

    s = 'abc'
    print(s[0])

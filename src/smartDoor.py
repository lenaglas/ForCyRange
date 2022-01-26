import logging 
import random
import time, sched

logging.basicConfig(filename='logs/smartDoor.log', format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)



s = sched.scheduler(time.time, time.sleep)


def log_door_lock(lock_mode): 
    if lock_mode == 0:
        message= "DOOR LOCKED"
    else:
        message= "DOOR UNLOCKED"
    logging.info(message)
    

def lock_door(sc): 
    print("Doing stuff...")
    # do your stuff
    lock_mode = random.randint(0,1)
    sleep = random.randint(0,20)
    log_door_lock(lock_mode)
    s.enter(sleep, 1, lock_door, (sc,))

s.enter(1, 1, lock_door, (s,))
s.run()


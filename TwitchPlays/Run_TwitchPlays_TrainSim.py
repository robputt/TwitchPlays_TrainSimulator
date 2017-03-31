import threading
import time
from TwitchPlays.irc_handler import irc_controller
from TwitchPlays.train_sim.train_sim_controller import async_tasks
from TwitchPlays.train_sim.train_sim_controller import controller

async = threading.Thread(target=async_tasks)
async.start()
irc_controller(controller)

#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from state import State
from web_server.server import web_server
import os
import logging

if __name__ == "__main__":
    logger = logging.getLogger("si100b_proj:main")
    logger.setLevel("INFO")
    pid = os.fork()
    if (pid == 0):
        ppid = os.getppid()
        try:
            web_server.run(host="0.0.0.0", port=9000)
        except KeyboardInterrupt:
            logger.warning("Web server exits.")
            os.kill(ppid)
    else:
        try:
            state = State()
            state.spin()
        except KeyboardInterrupt:
            logger.warning("Crawler exits.")
            os.kill(pid)

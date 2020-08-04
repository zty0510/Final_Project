#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

# NOTE to student:
# YOU ARE NOT SUPPOSED TO EDIT THE FILE.
#
# This file is intended to provide a unified entrypoint for your web server
# and the cralwer. You can treat this file as a black box. Being unable to
# know how the magic in this file works won't cause trouble to you finishing
# the project. If you feel the need to edit it, do it at your own risk.
# Understand every line of the file before proceed to editing. When in doubt,
# ask on Piazza.

from state import State
from web_server.server import web_server
import os
import logging

if __name__ == "__main__":
    logger = logging.getLogger("si100b_proj:main")
    logger.setLevel("INFO")
    # Create a new process.
    # `fork()` is a UNIX syscall that creates a new process.
    # `os.fork` is a Python wrapper of it. See `man fork` for more information.
    pid = os.fork()
    if (pid == 0):
        # The child process.
        # In this process, we run the web server.
        ppid = os.getppid()
        try:
            web_server.run(host="0.0.0.0", port=9000)
        except KeyboardInterrupt:
            logger.warning("Web server exits.")
            os.kill(ppid)
    else:
        # The parent process.
        # In this process, we run the cralwer and LED controller.
        try:
            state = State()
            state.spin()
        except KeyboardInterrupt:
            # The process is being killed, let the child process exit.
            logger.warning("Crawler exits.")
            os.kill(pid)

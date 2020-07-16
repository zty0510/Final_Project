#=============================================================================#
#                               Web Project                                   #
#       SI 100B: Introduction to Information Science and Technology           #
#                       Fall 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 07/07/2020                           #
#=============================================================================#

from state import State
from web_server.server import web_server
import multiprocessing

if __name__ == "__main__":
    state = State()
    server_process = multiprocessing.Process(target=web_server.run)
    cralwer_process = multiprocessing.Process(target=state.spin)
    server_process.start()
    cralwer_process.start()
    try:
        server_process.join()
        cralwer_process.join()
    except KeyboardInterrupt:
        server_process.kill()
        cralwer_process.kill()

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
    # create the `State` object of the web crawler.
    state = State()
    # start two process
    # @server_process: the Flask HTTP server process for configuration and data visualization (step 3, 4);
    # @crawler_process: the web crawler process for data retriving (step 1, 2);
    server_process = multiprocessing.Process(target=web_server.run)
    cralwer_process = multiprocessing.Process(target=state.spin)
    # let those two process run
    server_process.start()
    cralwer_process.start()
    # wait for the two running process and kill them when Ctr-C is pressed
    try:
        server_process.join()
        cralwer_process.join()
    except KeyboardInterrupt:
        server_process.kill()
        cralwer_process.kill()

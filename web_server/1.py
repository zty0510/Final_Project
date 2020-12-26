import csv
import threading
import statesec
import server
import fr24_crawler
import  multiprocessing
def run_web():
    print("go_web")
    server.web_server.run(host="127.0.0.1", port=5000)


def run_state():
    print("go_state")
    run = statesec.State()
    run.spin()

if __name__ == "__main__":
    web_server= threading.Thread(target=run_web)
    state= threading.Thread(target=run_state)



    state.start()
    web_server.start()

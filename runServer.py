import os
import socket

MAIN_FILE = "./home.py"
PORT = 8501

def runServer(file, port):
    fileDir = os.path.dirname(file)
    open(f"{fileDir}/.serverRunning", "w")
    os.system(f"streamlit run {file} --server.port={port}")

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        output = s.connect_ex(('localhost', port)) == 0
    return output

mainDir = os.path.dirname(MAIN_FILE)

if __name__ == '__main__':

    try:
        if '.serverRunning' not in os.listdir(mainDir):
            runServer(MAIN_FILE, PORT)
        elif not is_port_in_use(PORT):
            os.remove("./.serverRunning")
            runServer(MAIN_FILE, PORT)
        else:
            while is_port_in_use(PORT):
                PORT += 10
                runServer(MAIN_FILE, PORT)

    except KeyboardInterrupt:
        print("\033[1F\033[14GDone!")
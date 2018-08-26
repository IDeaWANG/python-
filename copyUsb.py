#coding-utf-8
from time import sleep 
import os,shutil
usb_path ="/volumes/wangjun"
content = os.listdir(usb_path)
while True:
    new_content = os.listdir(usb_path)
    if new_content != content :
        break;
    sleep(0)
x = [item for item in new_content if item not in content]
shutil.copytree(os.path.join(usb_path,x[0]),'/Users/home/usb_copy')



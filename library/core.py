import os
import platform 
import os.path
import threading
import subprocess 
from subprocess import Popen, PIPE

def osName():
  os=platform.system()
  return os

def trashSize():
    path=''
    command=""
    if(osName()=="Linux") :
      homedir = os.environ['HOME']
      path=homedir+"/.local/share/Trash"+" | awk '{print $1}'"
      command="du -hs "+path
    else :
      path='/home/sanjay/'

    process = subprocess.Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    output, code = process.communicate()
    output=output.decode("utf-8")
    s = str(output)
  
    return s

def folderSize():
    path=''
    homedir = os.environ['HOME']
    if(osName()=="Linux") :
      path='/home/sanjay/projects/'
    else :
      path='/home/sanjay/'
    size=os.statvfs(path)
    return homedir
import os, shutil
import platform 
import os.path
import threading
import subprocess 
from subprocess import Popen, PIPE
# pylint: disable=E1101

trashSizee=""

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

def clearTrash():
    path=''
    command=""
    if(osName()=="Linux") :
      homedir = os.environ['HOME']
      path=homedir+"/.local/share/Trash"
    
    else :
      path='/home/sanjay/'

    folder=path
    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
              global trashSizee
              trashSizee.label.configure(text=trashSize())
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))

    

def folderSize():
    path=''
    homedir = os.environ['HOME']
    if(osName()=="Linux") :
      path='/home/sanjay/projects/'
    else :
      path='/home/sanjay/'
    size=os.statvfs(path)
    return homedir
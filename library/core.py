import os
import platform 

def osName():
  os=platform.system()
  return os

def folderSize():
    path=''
    if(osName()=="Linux") :
      path='/home/sanjay/projects/'
    else :
      path='/home/sanjay/'
    size=os.statvfs(path)
    return size
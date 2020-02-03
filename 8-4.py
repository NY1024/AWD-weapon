#pyinotify的使用示例
# -*- coding: utf-8 -*-
import os
import argparse
from pyinotify import WatchManager,Notifier,ProcessEvent
from pyinotify import IN_DELETE,IN_CREATE,IN_MOVED_TO,IN_ATTRIB
class EventHandler(ProcessEvent):
    #定义事件处理的类
    def process_IN_CREATE（self,event):
        print "[!]Create:"+event.pathname
        DeleteFileorDir(event.pathname)
    def process_IN_DELETE(self,event):
        print "[!]Delete :"+event.pathname
    def process_IN_ATTRIB(self,event):
        print "[!]Attribute been modified:"+event.pathname
    def process_IN_MOVED_TO(self,event):
        print "[!]File or dir been moved to here:"+event.pathname
        DeleteFileorDir(event.pathname)
def DeleteFileorDir(target):
    if os.path.isdir(target):
        filelist = os.listdir(target)
        for files in filelist:
            DeleteFileorDir(target+"/"+files)
        try:
            os.rmdir(target)
            print " >>Delete successfully:"+ target
        except:
            print "[-]Delete directory failed:"+target
    if os.path.isfile(target):
        try:
            os.remove(target)
            print ">>Delete file successfully" + target
        except:
            print "[-]Delete file failed:"+ target
def Monitor(path):
    wm = WatchManager()
    mask = IN_DELETE |  IN_ATTRIB | IN_CREATE | IN_MOVED_TO
    notifier = Notifier(wm,EventHandler())
    wm.add_watch(path,mask,rec=True)
    print '[+]Now Starting Monitor:%s' % (path)
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="%(prog)s - w [path]",
        
    )
    parser.add_argument('-w','--watch',action="store",dest="path",defalt="/var/www/html/",help="directory to watch,default is /var/www/html")
    args = parser.parse_args()
    Monitor(args.path)
    
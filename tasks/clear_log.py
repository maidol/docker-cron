#!/usr/bin/python
import os
import datetime

now=datetime.datetime.now()
delta=datetime.timedelta(days=-3)
n_days=now+delta
currentdate3 = str(n_days.strftime('%Y-%m-%d'))
delta=datetime.timedelta(days=-4)
n_days=now+delta
currentdate4 = str(n_days.strftime('%Y-%m-%d'))
delta=datetime.timedelta(days=-5)
n_days=now+delta
currentdate5 = str(n_days.strftime('%Y-%m-%d'))

path=os.getenv('CLEAR_LOG_DIR')
if path == '' or path == '/' or path == None:
    print 'CLEAR_LOG_DIR can not be empty or /'
    exit()

print 'CLEAR_LOG_DIR ' + path
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            if currentdate3 in fullpath or currentdate4 in fullpath or currentdate5 in fullpath :
                print 'delete ' + fullpath
                os.remove(fullpath)
            if "pm2-err" in fullpath or "pm2-out" in fullpath :
                print 'clear empty ' + fullpath
                f = open(r'%s' % fullpath,'w')
                f.truncate()
                f.close()

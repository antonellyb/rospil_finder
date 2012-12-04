#!/usr/bin/python

#import threading
from threading import Thread
import urllib2
import os
import subprocess
import time
doc_path="/home/vbarinov/projects/gozakupki/documents/"
if not os.path.exists(doc_path):
  os.makedirs(doc_path)

def get_Document ( idx ):
  headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
  req = urllib2.Request( "http://zakupki.gov.ru/pgz/printForm?type=NOTIFICATION&id=" + str(idx) , None, headers )
  try:
    resp = urllib2.urlopen(req)
    localFile = open( doc_path + "/doc_" + str(idx) + ".xml" , 'w')
    localFile.write(resp.read())
    localFile.close()
    return (doc_path + "/doc_" + str(idx) + ".xml" )
  except urllib2.URLError, e:
      return 0
      pass

def variator ( start, end ):
  for idx in xrange( start, end+1 ):
    doc = get_Document( idx )
    if (doc != 0):
      print doc

class myThread (Thread):
    def __init__(self, begin, end):
        self.begin=begin
        self.end=end
        Thread.__init__(self )
    def run(self):
        print "Start: "  + str(self.begin) + " End: " + str(self.end)
       # Get lock to synchronize threads
       #threadLock.acquire()
        variator( self.begin, self.end )
#        thread.exit()
       # Free lock to release next thread
       #threadLock.release()


num_threads=5;
total_ids=1000;
th_array = []
for thread_id in xrange( 1,  num_threads+1 ):
   start= (total_ids/num_threads)*(thread_id-1)+1
   end =  (total_ids/num_threads)*thread_id 
   th_array.append(myThread ( start, end ))
#   myThread( start, end ).start()
 
for thrd in th_array:
  thrd.start()
alive="true"
#while (alive):
#  alive='false'
#  for thrd in th_array:
#    if (thrd.isAlive):
#      alive="true"
print "done"

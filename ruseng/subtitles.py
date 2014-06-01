#!/usr/bin/python

import sys
import logging
from random import randint
import re
import time
from datetime import datetime
import os, random

def subtitles():
    show_lines = 20
    files_dir = "/home/zserg/projects/subtitles/files"

    logging.basicConfig(level=logging.DEBUG)

    #if len(sys.argv)!= 3 :
    #   print "usage: subtitles.py <file_ru> <file_eng>"
    #   exit()

    file_name = random.choice(os.listdir(files_dir))
    mObj = re.match(r'(.*)_(ru|en)\.srt',file_name,re.M|re.I)
    if not mObj:
       exit()

    file_name_ru = os.path.join(files_dir,mObj.group(1)+"_ru.srt")
    file_name_en = os.path.join(files_dir,mObj.group(1)+"_en.srt")

    logging.debug("file_ru=%s"%file_name_ru)
    logging.debug("file_en=%s"%file_name_en)

    file_ru = open(file_name_ru)
    file_en = open(file_name_en)

    r_size = 0;
    for line in file_ru:
      r_size+=1

    logging.debug("r_size=%s"%r_size)

    offset = randint(1,r_size)

    logging.debug("offset=%s"%offset)

    i = 0
    time_code_not_found = True
    file_ru.seek(0)
    out_ru = []
    
    for line in file_ru:
      if (i>=offset) & (i<offset+show_lines):
        m1 = re.match( r'^[0-9]*$', line, re.M|re.I)
        if not m1:
           out_ru.append(to_html_ru('%s'%(line.rstrip())))
        if time_code_not_found:
            sObj = re.search( r'(\d+\:\d+\:\d+),', line, re.M|re.I)
            if sObj:
                logging.debug("time=%s"%sObj.group(1))
                time_code_not_found = False
                time_code_s = sObj.group(1)

      i+=1
    logging.debug("CP1")

    time_code = datetime.strptime(time_code_s,"%H:%M:%S")
    logging.debug("CP0")

    time_code_not_found = True
    for line in file_en:
        if time_code_not_found:
            sObj = re.search( r'(\d+\:\d+\:\d+),', line, re.M|re.I)
            if sObj:
                time_code_s = sObj.group(1)
                time_code_en = datetime.strptime(time_code_s,"%H:%M:%S")
                #if time_code == time_code_en:
                if (time_code - time_code_en).total_seconds()<2:
                   logging.debug(time_code)
                   logging.debug(time_code_en)
                   time_code_not_found = False
                   #time.sleep(1)
                   #wait = raw_input("Press ENTER for english...")
                   #out.append(to_html("==================================="))
                   out_en = to_html("<hr>")
                   out_en = out_en + to_html(line.rstrip())
                   for i in range(show_lines):
                       line = next(file_en).rstrip()
                       m1 = re.match( r'^[0-9]*$', line, re.M|re.I)
                       if not m1:
                          out_en = out_en + to_html(line)


     

    return file_name, out_ru, out_en

def to_html_ru(line):
   s = re.search(r'-->',line,re.I|re.M)
   if s:
      line = '<p class="timecode">'+line+'</p>'
   else:
      line = '<p class="text1">'+line+'</p>'

   return line


def to_html(line):
   s = re.search(r'-->',line,re.I|re.M)
   if s:
      line = '<div class=\\"timecode\\">'+line+'</div>'
   else:
      line = '<div class=\\"text1\\">'+line+'</div>'
   
   line = re.sub(r"'","_",line)  

   return line





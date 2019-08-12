#!/usr/bin/python3

import re
import sys 
import os
import codecs
import codecs
import argparse

# _*_ coding:utf-8 _*_
def select(num):
   conuter = 0
   if num == 0:
      with open('aaa.txt') as handle:
         lines = handle.readlines()
         new_file = open('bbb.txt','w')
         for line in lines:
            if (conuter <= 6 or conuter >= 27):        #or  == a || b 
               print(conuter)
               top_line = re.sub(r'xxxxxx','ddd',line)
               new_file.write(top_line)
            conuter += 1
         new_file.close()
   elif num == 1:
      pass
   else:
      pass

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('-mn','--modules_name', default = 0, help = 'this is shenme ')
   parser.add_argument('-num','--num', default = 0, help = 'this is shenme ')
   args = parser.parse_args()
   modules = args.module_name;
   num = args.num;
   select(0)

#/usr/bin/pyhon3

import re
import sys 
import os
import codecs

# _*_ coding:utf-8 _*_
def select(num):
   conuter = 0
   if num == 0:
      with open('aaa.txt') as handle:
         lines = handle.readlines()
         new_file = open('bbb.txt','w')
         for line in lines:
            if (conuter <= 6 or conuter >= 27):         #在python中，异或非分别用and or not 表示
               print(conuter)
               top_line = re.sub(r'xxxxxx','ddd',line)
               new_file.write(top_line)
            conuter = conuter + 1
         new_file.close()
   elif num == 1:
      pass
   else:
      pass

if __name__ == '__main__':
   select(0)

#!/usr/bin/python3

import os
import sys
import re
import codecs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-mn','--modules_name', default = 0, help = 'this is shenme ')
parser.add_argument('-num','--num', default = 0, help = 'this is shenme ')
args = parser.parse_args()
modules = args.modules_name;
num = args.num;

class Uvm_gen():
   def __init__(self,module_name,b):
      self.module_name = module_name
      self.b = b

   def mkdir_file(self,module_name):
      mkdir = 'mkdir ' + module_name + '_verfi'
      os.system(mkdir)

   def rename_file(self,module_name):
      os.system('cp -r ../uvm_gen/* ./')
      path = os.getcwd()
      print(path)
      path = path + '/' + module_name + '_verfi'
      os.chdir(path)
      print(os.getcwd())

if __name__ == '__main__':
   os.system('rm -r ' + modules + '_verfi')
   print('clean old file %(modules_name)s_verfi' % {'modules_name' : modules})
   uvm_gen = Uvm_gen(modules,1)
   uvm_gen.mkdir_file(modules)
   uvm_gen.rename_file(modules)
      







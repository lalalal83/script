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
      os.system('cp -r ../uvm_gen/templates/* ./' + module_name + '_verfi')
      path = os.getcwd()
      print(path)
      path = path + '/' + module_name + '_verfi'
      os.chdir(path)
      print(os.getcwd())
      filelist = os.listdir(path)
      for file in filelist:
         '''rename this file'''
         old_name = path + os.sep + file
         new_file = re.sub(r'uvm',module_name,file)
         new_name = path + os.sep + new_file
         os.rename(old_name,new_name)

   def new_content(self,module_name):
      path = os.getcwd()
      filelist =  os.listdir(path)
      for file1 in filelist:
         with open(file1) as handle:
            handle_lines = handle.readlines()
         with open(file1,'w') as new_handle:
            for line in handle_lines:
               if '{:NAME:}' in line:
                  line = re.sub(r'{:NAME:}',module_name,line)
               if '{:UPPERNAME:}' in line:
                  line = re.sub(r'{:UPPERNAME:}',module_name.upper(),line)
               if '' in line:
                  #new_line = re
                  pass
               new_handle.write(line)

      
if __name__ == '__main__':
   os.system('rm -r ' + modules + '_verfi')
   print('clean old file %(modules_name)s_verfi' % {'modules_name' : modules})
   uvm_gen = Uvm_gen(modules,1)
   uvm_gen.mkdir_file(modules)
   uvm_gen.rename_file(modules)
   uvm_gen.new_content(modules)
      







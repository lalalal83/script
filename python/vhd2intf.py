#!/usr/bin/python3

import re
import sys 
import os
import codecs

def deal_with_vhdl():
	handle = open('aaa.txt')
	new_file = open('bbb.sv','w')
	handlelines = handle.readlines()
	for line in handlelies:
		interface = re.findall(r'^.*?:',line)
		interface = interface[0].strip()[:-1]
		bit_num = re.findall(r':.*?$',line)
		bit_num = bit_num[0].strip()
		num = re.findall(r'\d',bit_num)
		if('bit' in line):
			len_num = len(num)
			if len_num == 0:
				reline = '	logic		' + interface + ';\n'
			elif len_num == 1:
				num = num[0].strip()
				num = int(num) - 1
				num = str(num)
				reline = '	logic[ ' + num + ':0]' + interface + ';\n'
			else:
				num = num[0].strip() + num[1].strip()
				num = int(num) - 1
				num = str(num)
				if num == '9':
					reline = '	logic[ ' + num + ':0]' + interface + ';\n'
				else:
					reline = '	logic[' + num + ':0]' + interface + ';\n'
		else:
			reline = '	logic[ ?:0]' + interface + ';\n'
		new_file.write(reline)
	new_file.close()


if __name__ == '__main__':
	deal_with_vhdl()


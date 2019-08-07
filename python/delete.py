def delblankline(infile, outfile):
   infopen = open(infile)
   outfopen = open(outfile, 'w') 
   lines = infopen.readlines()
   for line in lines:
      if line.split():
         outfopen.writelines(line)
      else:
         outfopen.writelines("")
   infopen.close()
   outfopen.close()

if __name__ == '__main__': 
   delblankline("aaa.txt", "bbb.txt")

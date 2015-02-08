import rpyc
import sys

if len(sys.argv) == 2:
  temp = sys.argv[1]
 
else:
  temp = "localhost"

c = rpyc.connect(temp, port=18863)

def downl(bindata, fname):
  fc = open(fname, "wb")
  fc.write(bindata)
  fc.close
  print "Download Complete!"

def printlist(filename):
  print filename

bgsrv = rpyc.BgServingThread(c)

name = raw_input("Enter Your Name:")

while True:
  cmd = raw_input("Enter your command:")
  
  if cmd == 'list':
    c.root.set_list_printlist(printlist)
    c.root.show()
  elif cmd == 'download':
    num = input('Enter the list index for the file that you want to download starting from 0:')
    c.root.set_calldownl(downl) 
    c.root.calldownl(num)
  elif cmd == 'upload':
    path = raw_input('Enter the file you want to upload:')
    fo = open(path, "rb")
    str = fo.read()
    fo.close()
    c.root.upl(str, path)

bgsrv.stop()
c.close()

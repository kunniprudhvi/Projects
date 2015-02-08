import rpyc

class Service(rpyc.Service):
  def on_connect(self):
    pass

  def on_disconnect(self):
    print "Someone left!"

  def exposed_setCallback(self,showMe):
    c.setCallback(showMe)

  def exposed_upl(self, file, path):
    c.upl(file, path)

  def exposed_show(self):
    c.show()

  def exposed_set_list_printlist(self, printlist):
    c.set_list_printlist(printlist)

  def exposed_set_calldownl(self, downloadlist):
    c.set_calldownl(downloadlist)

  def exposed_calldownl(self, num):
    c.calldownl(num) 

class FileShareServer:
  def __init__(self):
    self.files = []
    self.filename = []
    self.list_printlist = []
    self.list_downl = []

  def set_list_printlist(self, printlist):
    self.list_printlist = self.list_printlist + [printlist]

  def show(self):
    try:
      self.list_printlist[-1](self.filename)   
    except:
      pass 	

  def upl(self, file, path):
    self.files = self.files + [file]
    self.filename = self.filename + [path]

  def set_calldownl(self, downloadlist):
    self.list_downl = self.list_downl + [downloadlist]
  
  def calldownl(self, num):
    bindata = self.files[num]
    fname = self.filename[num] 
    self.list_downl[-1](bindata, fname)
	
if __name__ == "__main__":
  from rpyc.utils.server import ThreadedServer
  c = FileShareServer()
  t = ThreadedServer(Service, port = 18863)
  t.start()


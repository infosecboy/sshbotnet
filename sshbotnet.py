from pexpect import pxssh
class Client:
	def __init__(self,tgthost,tgtuser,tgtpass):
		self.tgthost = tgthost
		self.tgtuser = tgtuser
		self.tgtpass = tgtpass
		self.session = self.connect()
	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.tgthost,self.tgtuser,self.tgtpass)
			return s
		except Exception,e:
			print(e)
			print("[+] error connecting")
	def command(self,cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before
host = raw_input("Enter host ip address")
username = raw_input("Enter username")
password  = raw_input("Enter password")
commd = raw_input("Enter command")
client = Client(host,username,password)
print(client.command(commd))


		

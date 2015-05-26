from ftplib import FTP

host = "192.168.0.13" # raw_input("host: ")
user = "marcin" # raw_input("user: ")
passwd = "sector1985" # raw_input("password: ")

print "connecting to ftp...\n"


try:
	ftp = FTP(host)
	ftp.login(user, passwd)
except Exception,e:
	print e
else:
	filelist = []
	ftp.retrlines('LIST',filelist.append)
	print ftp.dir()	
	print

	for f in filelist:
		if "test.txt" in f:
			print "found!!"

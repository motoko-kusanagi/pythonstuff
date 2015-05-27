from ftplib import FTP
import os
import time
import pyodbc

### CONSTANT VARiABLES
host = "192.168.0.13" # raw_input("host: ")
user = "marcin" # raw_input("user: ")
passwd = "passwd" # raw_input("password: ")
my_file = "test.txt"

### SQL CONNECTiON
db_host = "192.168.0.14"
db_user = "marcin"
db_passwd = "passwd"
db_name = "python"
db_table = "import"

### FTP PATH/FiLENAME
path = os.path.dirname(os.path.realpath(__file__))
path = path + "/csv"
my_dfile = path + "/" + my_file

def print_info():
	print "host : " + host
	print "user : "	+ user
	print 
	time.sleep(1)

def print_file():
	file = open(my_dfile, 'r')
	file_contents = file.read()
	print (file_contents)
	file.close()
	

def dir_check():
	import getpass
	import os
	user_dir = getpass.getuser()

	path = os.path.dirname(os.path.realpath(__file__))
	path = path + "/csv"
	print path
	
	try:
		os.makedirs(path)
	except OSError:
		if os.path.exists(path):
			pass

def grab_file():
	localfile = open(my_dfile, 'wb')
	ftp.retrbinary('RETR ' + my_file, localfile.write, 1024)
	localfile.close()

def search_file():
	for f in filelist:
        	if my_file in f:
                	print "%s is there! " % my_file
			time.sleep(1)
			answer = raw_input("proceed with download? (y/n) : ")
			
			while answer not in ['y', 'Y', 'n', 'N']:
				print "invalid answer..."
				answer = raw_input("proceed with download? (y/n) : ")
			
			if answer == "n" or answer == "N":
				break

			dir_check()
                        grab_file()
			print_file()
                        ftp.quit()

def sql_insert():
	sql = pyodbc.connect('Driver={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s') % (db_host, db_name, db_user, db_passwd)
	cursor = sql.cursor()
	cursor.execute("select user_id, user_name from users")
	rows = cursot.fetchall()

	for row in rows:
		print row.user_id, row.user_name

try:
	print_info()
	ftp = FTP(host)
	ftp.login(user, passwd)
except Exception,e:
	print e
else:
        print "connected to ftp server"
        time.sleep(1)

	filelist = []
	ftp.retrlines('LIST',filelist.append)
	print ftp.dir()	
	print

	search_file()

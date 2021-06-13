from ftplib import FTP, error_perm
import os

ftp_host ='127.0.0.1'
ftp_login = 'ahenry'
ftp_password = '1234'
OUTPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Output_Files'

ftp = FTP(ftp_host, ftp_login, ftp_password)
print(ftp.getwelcome())

print(ftp.nlst())

def placeFiles(ftp, path):
    for filename in os.listdir(path):
        localpath = os.path.join(path, filename)
        if os.path.isfile(localpath):
            print("Directory to upload")
            ftp.storbinary('STOR ' + filename, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            print('MKDIR', filename)
            try:
                ftp.mkd(filename)
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    raise
            
            print("CWD", filename)
            ftp.cwd(filename)
            placeFiles(ftp, localpath)
            print("CWD", "..")
            ftp.cwd("..")

placeFiles(ftp, OUTPUT_FOLDER)

ftp.quit()

""" 
source = path
print(source)
source_file = open(source, 'rb')
ftp.storbinary('STOR '+source, source_file)
source_file.close()

ftp.rename(source,'test2.py')


destination = 'test2.py'
dest_file = open(destination, 'wb')
ftp.retrbinary('RETR ' + destination, dest_file.write, 1024)
dest_file.close()
 """
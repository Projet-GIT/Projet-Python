from ftplib import FTP, error_perm
import os
import sys
import shutil
import urllib.request as request
from contextlib import closing
import io
import ftplib
import time


ftp_host ='127.0.0.1'
ftp_login = 'ahenry'
ftp_password = '1234'
INPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Input_Files' 
OUTPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Output_Files'



def EnvoieFTP(ftp, path):
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
            EnvoieFTP(ftp, localpath)
            print("CWD", "..")
            ftp.cwd("..")


def downloadFiles(path, destination, ftp):
    try:
        ftp.cwd(path)
        os.chdir(destination)
        mkdir_p(destination[0:len(destination)-1] + path)
        print("Created: " + destination[0:len(destination)-1] + path)
    except OSError:
        pass
    except ftplib.error_perm:
        print("Error: could not change to " + path)
        sys.exit("Ending Application")

    filelist=ftp.nlst()
    interval = 0.5
    for file in filelist:
        time.sleep(interval)
        try:
            print(path)
            print(file)
            ftp.cwd(path + file)
            downloadFiles(path + file + "\\", destination, ftp)
        except ftplib.error_perm:
            os.chdir(destination[0:len(destination)-1] + path)

            try:
                print(destination + path)
                filen = open(os.path.join(destination[0:len(destination)-1] + path, file), "wb")
                ftp.retrbinary("RETR " + file, filen)
                print("Downloaded: " + file)
            except:
                print("Error: File could not be downloaded " + file)
    return

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if os.path.isdir(path):
            pass
        else:
            raise

if __name__ == "__main__":
    ftp = FTP(ftp_host, ftp_login, ftp_password)
    print(ftp.getwelcome())
    print(ftp.nlst())
    while 42:      
        answer = input("Menu: 1.Envoie FTP, 2.Reception Fichier, 3.Quit\n")
        if answer == "1":
            EnvoieFTP(ftp, OUTPUT_FOLDER)
        elif answer == "2":
            downloadFiles("\\", INPUT_FOLDER, ftp)
        elif answer == "3":
            print("Ending")
            ftp.quit()
            sys.exit(42)
        else:
            print("Error answer must be between 1, 2 or 3")
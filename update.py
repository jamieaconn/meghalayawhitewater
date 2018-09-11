import sys
import os
import ftplib
    
from local_info import ftp_url, ftp_pass, ftp_user

def uploadThis(path):
    FTP = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
    files = os.listdir(path)
    os.chdir(path)

    for f in files:
        #print os.path.join(path, f)
        #print os.path.isfile(os.path.join(path, f))
        if os.path.isfile(os.path.join(path, f)):
            print "\tuploading..."
            fh = open(f, 'rb')
            FTP.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(os.path.join(path, f)):
            print "\tcreating dir"
            FTP.mkd(f)
            FTP.cwd(f)
            uploadThis(os.path.join(path, f))
    FTP.cwd('..')
    os.chdir('..')

#uploadThis("/Users/jconn/meghalayarivers/_site")

#f = "archive.zip"

#fh = open("Archive.zip")
#FTP = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
#FTP.storbinary('STOR %s' % f, fh)
#fh.close()

import ftplib
import os


myFTP = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
myPath = "/Users/jconn/meghalayarivers/upload/"
def uploadThis(path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        newpath = os.path.join(path, f)
        if os.path.isfile(f):
            print "file:", f
            fh = open(f, 'rb')
            myFTP.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(f):
            print "directory:", f
            myFTP.mkd(f)
            myFTP.cwd(f)
            uploadThis(newpath)
    myFTP.cwd('..')
    os.chdir('..')
uploadThis(myPath) # now call the recursive function  

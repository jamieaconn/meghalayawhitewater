import sys
import os
import ftplib
    
from local_info import ftp_url, ftp_pass, ftp_user

def uploadThis(path):
    FTP = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
    files = os.listdir(path)
    os.chdir(path)

    for f in files:
        print os.path.join(path, f)
        print os.path.isfile(os.path.join(path, f))
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

f = "archive.zip"

fh = open("archive.zip")
FTP = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
FTP.storbinary('STOR %s' % f, fh)
fh.close()
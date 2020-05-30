import sys
import os
import ftplib
    
from local_info import ftp_url, ftp_pass, ftp_user


def remove_ftp_dir(ftp, path):
    for (name, properties) in ftp.mlsd(path=path):
        if name in ['.', '..']:
            continue
        elif properties['type'] == 'file':
            ftp.delete(os.path.join(path, name))
        elif properties['type'] == 'dir':
            remove_ftp_dir(ftp, os.path.join(path, name))
    ftp.rmd(path)


def recursive_upload(ftp, path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        newpath = os.path.join(path, f)
        if os.path.isfile(f):
            print "file:", f
            fh = open(f, 'rb')
            ftp.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(f):
            print "directory:", f
            ftp.mkd(f)
            ftp.cwd(f)
            recursive_upload(ftp, newpath)
    ftp.cwd('..')
    os.chdir('..')


ftp = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
local_path = "/Users/jconn/meghalayarivers/upload/"
#remove_ftp_dir(ftp, 'public_html')
recursive_upload(ftp, local_path)


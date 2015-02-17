__author__ = 'Manu'
import os
from datetime import datetime
import ftplib
import urllib

def ftp_file(**kargs):

    # Map arguments
    server = kargs['server']
    username = kargs['username']
    password = kargs['password']
    filepath = kargs['filepath']
    downloadFolder = kargs['downloadFolder']
    force_download = kargs['force_download']

    if '/' in filepath:
        ftp_path = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
    else:
        ftp_path = None
        filename = filepath

    # Connect to FTP server
    try:
        ftp = ftplib.FTP(server)
    except (ftplib.socket.error, ftplib.socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % server
        return False
    print '*** Connected to host %s' % server

    try:
        ftp.login(username, password)
    except ftplib.error_perm, e:
        print 'ERROR: cannot login'
        ftp.quit()
        return False
    print '*** Logged in successfully'

    # Go to target directory
    try:
        ftp.cwd(ftp_path)
        print '*** Changed to folder: "%s"' % ftp_path
    except ftplib.error_perm, e:
        print 'ERROR: cannot CD to "%s"' % ftp_path
        ftp.quit()
        return False

    # Create download folder (if needed)
    if not os.path.exists(downloadFolder):
        os.makedirs(downloadFolder)

    # Check if download is needed
    local_file = os.path.join(downloadFolder, filename)
    if os.path.exists(local_file):
        remote_modified_date = ftp.sendcmd('MDTM ' + filename)
        remote_modified_date = datetime.strptime(remote_modified_date[4:], "%Y%m%d%H%M%S").strftime("%d %b %Y")
        local_modified_date = os.path.getmtime(local_file)
        local_modified_date = datetime.fromtimestamp(local_modified_date).strftime("%d %b %Y")

        if remote_modified_date != local_modified_date:
            download_necessary = True
            print "Local file date: %s | Remote file date: %s" % (local_modified_date, remote_modified_date)
        else:
            download_necessary = False
            print "Download is not necessary. Local file is up to date! (%s)" % local_modified_date
            result = True
    else:
        download_necessary = True

    if download_necessary or force_download:

        try:
            ftp.voidcmd('TYPE I')
            if downloadFolder is not None:
                currentDir = os.getcwd()
                os.chdir(downloadFolder)
            size = ftp.size(filename)
            print "Downloading %s... (%s) into %s" % (filename, size, downloadFolder)
            result = ftp.retrbinary("RETR %s" % filename, open(filename, 'wb').write)
            os.chdir(currentDir)
            print "Download complete!"

        except ftplib.error_perm, e:
            print 'ERROR: cannot read file "%s"' % filename
            result = e.message

    # Close connection
    ftp.quit()
    print "Disconnected from server"

    return result


def http_file(filepath, downloadFolder, filename="", force_download=False):

    # Create download folder (if needed)
    if not os.path.exists(downloadFolder):
        try:
            os.makedirs(downloadFolder)
            print "Created folder '%s'" % downloadFolder
        except:
            print "Error creating folder %s" % downloadFolder

    # Download file
    if not filename:
        filename = os.path.basename(filepath)
    print "Downloading %s to '%s'..." % (filename, downloadFolder)
    try:
        urllib.urlretrieve (
            filepath,
            os.path.join(downloadFolder, filename)
            )
        print "Download completed!"
    except Exception, e:
        print "ERROR downloading airports CSV file. %s" % e

    return True
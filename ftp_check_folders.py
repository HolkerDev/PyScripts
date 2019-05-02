from ftplib import FTP

'''Script connects to UITM ftp server and shows all the folders inside WSPÓLNY directory'''

USER_LOGIN = 'w*****'
USER_PASS = '*********'

ftp = FTP('ftp.wsiz.rzeszow.pl')

ftp.login(user=USER_LOGIN, passwd=USER_PASS)

ftp.cwd('../')
ftp.cwd('WSPOLNY')
print(ftp.nlst())

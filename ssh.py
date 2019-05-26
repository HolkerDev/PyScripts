import paramiko

USERNAME = ''
PASSWORD = ''

# connect to the server via secure shell
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('localhost', port=22, username=USERNAME, password=PASSWORD)

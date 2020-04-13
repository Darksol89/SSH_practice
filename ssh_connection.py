"""SSH client - open\close connection."""
import paramiko

host = '192.168.31.103'
port = 22
username = 'ichistov'
password = '1q2w3e$'

ssh_client = paramiko.SSHClient()


def ssh_client_connect():
    """SSH client connection to remote server"""
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)


def ssh_client_close():
    """SSH client close connection"""
    ssh_client.close()

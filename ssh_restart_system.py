"""Test for restart remote server and check status"""
import time
from ssh_connection import password
from ssh_connection import ssh_client_connect, ssh_client_close


def ssh_restart_system():
    # Authorizing via SSH
    ssh_client_connect()

    # Checking last date reboot
    stdin, stdout, stderr = ssh_client_connect().exec_command(
        'last reboot')
    data_reboot_before = stdout.read() + stderr.read()
    #print(data_reboot_before.decode())

    # Restart server
    ssh_client_connect().exec_command('sudo -S reboot -f')
    ssh_restart_system().write(password + '\n')

    # Close SSH connection
    ssh_client_close()

    # Waiting few time for restart system
    time.sleep(40)

    # Authorizing via SSH
    ssh_client_connect()

    # Checking last date reboot
    stdin, stdout, stderr = ssh_client_connect().exec_command(
        'last reboot')
    data_reboot_after = stdout.read() + stderr.read()
    #print(data_reboot_after.decode())

    # Check output message in terminal
    if data_reboot_before != data_reboot_after:
        print('System was successfully rebooted')
    elif data_reboot_before == data_reboot_after:
        assert False, 'Failed. System was not rebooted'
    else:
        assert False, 'Something wrong'

    # Close SSH connection
    ssh_client_close()


if __name__ == '__main__':
    ssh_restart_system()

"""Test for restart ufw service and check status"""
from ssh_connection import password
from ssh_connection import ssh_client_connect, ssh_client_close


def ssh_restart_service_ufw():
    # Authorizing via SSH
    ssh_client_connect()

    # Run command and restart service
    stdin, stdout, stderr = ssh_client_connect().exec_command(
        'sudo -S /etc/init.d/ufw restart')
    stdin.write(password + '\n')
    data_restart_service = stdout.read() + stderr.read()

    # Check output message in terminal
    if 'Restarting ufw' in data_restart_service.decode():
        print('Service was successfully restarted')
    elif 'Restarting ufw' not in data_restart_service.decode():
        assert False, 'Failed. Service was not restarted'
    else:
        assert False, 'Something wrong'

    # Close SSH connection
    ssh_client_close()


if __name__ == '__main__':
    ssh_restart_service_ufw()

from ssh_connection import ssh_client_connect, ssh_client_close, ssh_client


def test_restart_service():
    """Test for restart ufw service and check status"""

    # Authorizing via SSH
    ssh_client_connect()

    # Run command and restart service
    stdin, stdout, stderr = ssh_client.exec_command(
        'sudo -S /etc/init.d/ufw restart')
    data_restart_service = stdout.read() + stderr.read()

    # Check output message in terminal
    if 'Restarting' and 'ufw' in data_restart_service.decode():
        print('Service was successfully restarted')
    elif 'Restarting' and 'ufw' not in data_restart_service.decode():
        assert False, 'Failed. Service was not restarted'
    else:
        assert False, 'Something wrong'

    # Close SSH connection
    ssh_client_close()
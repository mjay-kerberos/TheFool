import paramiko
from scp import SCPClient

def create_ssh_client(host, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
    return client

def execute_script(ssh_client, script_path):
    command = f'python3 {script_path}'
    stdin, stdout, stderr = ssh_client.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())

# Configuration - fill this out with your details
host = 'your.remote.host'
port = 22
user = 'yourusername'
password = 'yourpassword'
local_script_path = 'path/to/your/local/script.py'
remote_script_path = '/remote/path/script.py'

# Establishing SSH connection
ssh_client = create_ssh_client(host, port, user, password)

# Transfer the script
with SCPClient(ssh_client.get_transport()) as scp:
    scp.put(local_script_path, remote_script_path)

# Execute the script remotely
execute_script(ssh_client, remote_script_path)

# Closing the connection
ssh_client.close()
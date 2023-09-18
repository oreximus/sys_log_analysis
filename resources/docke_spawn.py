import subprocess

def create_docker_network(network_name, subnet):
    # Check if the network already exists
    existing_networks = subprocess.run(["docker", "network", "ls", "--filter", f"name={network_name}", "--format", "{{.Name}}"], capture_output=True, text=True)
    
    if network_name not in existing_networks.stdout:
        network_create_command = [
            "docker",
            "network",
            "create",
            "--driver",
            "bridge",
            "--subnet",
            subnet,
            network_name
        ]

        subprocess.run(network_create_command, check=True)
    else:
        print(f"Network '{network_name}' already exists, skipping creation.")

def run_docker_container(container_name, network_name, container_ip):
    # Check if the container already exists
    existing_containers = subprocess.run(["docker", "ps", "-a", "--filter", f"name={container_name}", "--format", "{{.Names}}"], capture_output=True, text=True)
    
    if container_name not in existing_containers.stdout:
        container_run_command = [
            "docker",
            "run",
            "-d",
            "--name",
            container_name,
            "--network",
            network_name,
            "--ip",
            container_ip,
            "-it",
            "archlinux"
        ]

        subprocess.run(container_run_command, check=True)
    else:
        print(f"Container '{container_name}' already exists, skipping creation.")

# Define network and container parameters
network_name = "log_analysis_testing_network"
subnet = "172.19.0.0/16"

# Create the Docker network if it doesn't exist
create_docker_network(network_name, subnet)

# Run vulnerable_container1 if it doesn't exist
run_docker_container("vulnerable_container1", network_name, "172.19.0.2")

# Run vulnerable_container2 if it doesn't exist
run_docker_container("vulnerable_container2", network_name, "172.19.0.3")

# Run vulnerable_container3 if it doesn't exist
run_docker_container("vulnerable_container3", network_name, "172.19.0.4")

# Run vulnerable_container4 if it doesn't exist
run_docker_container("vulnerable_container4", network_name, "172.19.0.5")

# Run vulnerable_container5 if it doesn't exist
run_docker_container("vulnerable_container5", network_name, "172.19.0.6")

# Run vulnerable_container6 if it doesn't exist
run_docker_container("vulnerable_container6", network_name, "172.19.0.7")


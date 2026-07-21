import docker


client = docker.from_env()
containers = client.containers.list(all=True)
print(len(containers))
print([(container.name, container.status) for container in containers])
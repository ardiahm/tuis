import docker

client = docker.from_env()

all = client.containers.list(all=True)

for one in all:
    print(f"Name: {one.name}")
    print(f"Status: {one.status}")

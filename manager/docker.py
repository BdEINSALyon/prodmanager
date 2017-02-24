import docker


class DockerClient:
    """
    Define a DockerClient for this application
    """

    def __init__(self):
        self.docker = docker.from_env()

    @property
    def containers(self):
        return self.docker.containers.list(all=True)

    def get_container(self, container_id):
        return self.docker.containers.get(container_id)

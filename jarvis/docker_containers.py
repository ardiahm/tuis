import docker

from pathlib import Path

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Digits, Static, Label 
from textual.widget import Widget


class DockerContainers(Widget):
    """A widget to display docker containers and their status's"""

    DEFAULT_CSS = Path(Path(__file__).parent / "docker_containers.tcss").read_text(encoding="utf-8")


    def compose(self) -> ComposeResult:
        """Yield vertical container for all Label widgets."""
        yield Vertical(id="container-list")


    def on_mount(self) -> None:
        """Method called when widget is first mounted. """
        self.update_docker_containers()
        self.set_interval(10, self.update_docker_containers)

    def update_docker_containers(self) -> None:
        """Method to update docker container status to current. """

        container_list = self.query_one("#container-list", Vertical)

        try:
            # connect to docker client, store all container info in containers
            client = docker.from_env()
            containers = client.containers.list(all=True)

            labels = []  

            # Display count of Docker Containers
            count = Label(
                f"({len(containers)}) Docker Containers:"
            )

            # Append to labels
            labels.append(count)
            
            # check status, display container name and short_id (truncated to 6)
            # with appropriate styling
            for container in containers:
                if container.status in ("exited", "created"):
                    color = "$foreground"
                elif container.status == ("paused", "restarting"):
                    color = "$warning"
                else:
                    color = "$success"

                content = Label(
                        f"[{color}]{container.name} - {container.short_id[:6]}[/{color}]"
                    )
            
                # Append to labels
                labels.append(content)

            # If none found, state no Docker containers found.
            if not labels:
                labels = [Label("No Docker containers found.")]
            
            # Rather than appending containers to Labels each refresh,
            # we clear and then repopulate
            container_list.remove_children()
            container_list.mount(*labels)

        # Catch errors
        except docker.errors.DockerException:
            container_list.remove_children()
            container_list.mount(
                Label("Unable to connect to Docker")
            )


         



    
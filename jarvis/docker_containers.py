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
        """Map each container to corresponding Label widgets."""

        yield Vertical(id="container-list")


    def on_mount(self) -> None:
        """Method called when widget is first mounted. """
        self.update_docker_containers()
        self.set_interval(10, self.update_docker_containers)

    def update_docker_containers(self) -> None:
        """Method to update docker container status to current. """

        container_list = self.query_one("#container-list", Vertical)

        try:
            client = docker.from_env()
            containers = client.containers.list(all=True)

            labels = []  

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
            
                labels.append(content)


            if not labels:
                labels = [Label("No Docker containers found.")]
            
            container_list.remove_children()
            container_list.mount(*labels)

        except docker.errors:
            container_list.remove_children()
            container_list.mount(
                Label("Unable to connect to Docker", style="$error")
            )


         



    
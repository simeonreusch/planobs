import logging
import typer
from planobs.api import Queue


logger = logging.getLogger(__name__)


# -----------------------------------------------------------------
# Main app


app = typer.Typer()


@app.callback()
def callback(logging_level: str = "INFO"):
    logging.basicConfig(level=logging.getLevelName(logging_level))
    logging.getLogger("planobs").setLevel(logging.getLevelName(logging_level))


# Main app
# -----------------------------------------------------------------


# -----------------------------------------------------------------
# Queue commands


queue_app = typer.Typer()


@queue_app.command("too")
def check_too_queue(username: str):
    """
    Check the ToO queue for a given user
    """
    typer.echo(f"Checking ToO queue for {username}")

    q = Queue(user=username)
    existing_too_queue = q.get_too_queues_name_and_date()
    queue = ""
    for entry in existing_too_queue:
        queue += f"{entry}\n"
    queue = queue[:-1]

    if len(queue) == 0:
        message = "Currently, no ToO triggers are in the ZTF observation queue."
    else:
        message = f"The current ZTF ToO observation queue:\n{queue}"

    typer.echo(message)


@queue_app.command("all")
def check_all_queues(username: str):
    """
    Check all queues for a given user
    """
    typer.echo(f"Checking all queues for {username}")
    queue = "\n".join(Queue(user=username).get_all_queues_nameonly())
    if len(queue) == 0:
        message = "Currently, no triggers are in the ZTF observation queue."
    else:
        message = f"The current ZTF observation queue:\n{queue}"
    typer.echo(message)


# Queue commands
# -----------------------------------------------------------------


def main():
    app.add_typer(queue_app, name="queue")
    app()


if __name__ == "__main__":
    app()

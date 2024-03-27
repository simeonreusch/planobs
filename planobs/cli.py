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

@app.command("queue")
def check_queue(username: str, which: str = "too"):
    """
    Check queue for a given user
    """
    typer.echo(f"Checking {which} queues for {username}")
    q = Queue(user=username)
    match which:
        case "too":
            response = q.get_too_queues_name_and_date()
        case "all":
            response = q.get_all_queues_nameonly()
        case _:
            raise ValueError(f"Invalid queue type: {which}")
    queue = "\n".join(response)
    if len(queue) == 0:
        message = "Currently, no triggers are in the ZTF observation queue."
    else:
        message = f"The current ZTF observation queue:\n{queue}"
    typer.echo(message)

# Queue commands
# -----------------------------------------------------------------


def main():
    app()


if __name__ == "__main__":
    app()

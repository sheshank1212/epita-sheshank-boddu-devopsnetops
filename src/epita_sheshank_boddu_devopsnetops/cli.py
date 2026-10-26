
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .client import fetch_live_data

console = Console()


def main():
    """Display the authenticated GitHub profile."""
    try:
        profile = fetch_live_data()

        table = Table(title="GitHub Profile")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Status", str(profile["status"]))
        table.add_row("Username", str(profile["username"]))
        table.add_row("Public repositories", str(profile["public_repos"]))
        table.add_row("Followers", str(profile["followers"]))

        console.print(
            Panel(table, title="EPITA Group 3 — DevOps & NetOps")
        )

    except Exception as error:
        console.print(f"[red]Error: {error}[/red]")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

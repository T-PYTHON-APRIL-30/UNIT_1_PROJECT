# packages
from rich.tree import Tree
from rich import print as rprint


def status(movie_data: list):
    '''This function calculates the status of each list'''

    # Count the movies in the list
    watching_status: int = 0
    completed_status: int = 0
    plan_status: int = 0
    for data in movie_data:
        if data["section"] == "watching":
            watching_status += 1
        elif data["section"] == "completed":
            completed_status += 1
        elif data["section"] == "plan to watch":
            plan_status += 1

    func_status = lambda x, y, z: x + y + z
    all_status = func_status(watching_status, completed_status, plan_status) # Count all the movies in the list

    # Display the status of user movies list
    tree = Tree("Movie Stats")
    tree.add("[green]Watching").add(f"[green]{str(watching_status)} / {str(all_status)}")
    tree.add("[blue]Completed").add(f"[blue]{str(completed_status)} / {str(all_status)}")
    tree.add("[yellow]Plan to Watch").add(f"[yellow]{str(plan_status)} / {str(all_status)}")
    tree.add("Total Movies").add(str(all_status))

    return rprint(tree)
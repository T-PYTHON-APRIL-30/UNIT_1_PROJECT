import time
from rich.progress import Progress


def status(movie_data: list) -> int:
    '''This function calculates the status of each list'''

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

    all_status = lambda x, y, z: x + y + z
    return print(all_status(watching_status, completed_status, plan_status))
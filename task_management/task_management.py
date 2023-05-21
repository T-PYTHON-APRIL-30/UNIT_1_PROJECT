import json

FILE_PATH = "./task_management/Tasks.json"


def add_task(task_dict):
    with open(FILE_PATH, "r+") as file:
        objects: list = json.load(file)

        objects.append(task_dict)
        file.seek(0)
        json.dump(objects, file)


def read_tasks() -> list[dict]:
    try:
        with open(FILE_PATH) as file:
            tasks: list[dict] = json.load(file)

        sorted_list = sorted(tasks, key=lambda x: x["priority"])
    except FileNotFoundError:
        print(f"The specified file does not exist: {FILE_PATH}")

    return tasks


def current_task() -> list[dict]:
    tasks = read_tasks()
    return filter_task(tasks, "status", "New")


def completed_task() -> list[dict]:
    tasks = read_tasks()
    return filter_task(tasks, "status", "Completed")


def mark_as_completed(id):
    all_tasks = read_tasks()
    # for task in all_tasks:
    #     if task["id"] == id:
    #         task["status"] = "Completed"
    #         break
    task = next((task for task in all_tasks if task["id"] == id))
    task["status"] = "Completed"

    with open(FILE_PATH, "w") as file:
        json.dump(all_tasks, file)


# return the list without specific dict
def opposite_filter_task(tasks, key, value) -> list[dict]:
    return [d for d in tasks if d.get(key) != value]


# return the list matches specific dict
def filter_task(tasks, key, value) -> list[dict]:
    return [d for d in tasks if d.get(key) == value]


def print_tasks(list_of_tasks):
    print(f"{len(list_of_tasks)} tasks found")

    for task in list_of_tasks:
        print(
            f"Name: {task['name']} , Dicription: {task['task']} , Priority: {task['priority']} , Created_At: {task['created_at']} , Due_At: {task['due_at']} , Status: {task['status']}"
        )
        print()

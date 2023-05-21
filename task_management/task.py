import datetime

from shortuuid import uuid

from task_management.task_management import add_task


class Task:
    def __init__(self, name, task, priority, due_at):
        self.name = name
        self.task = task
        self.priority = priority
        self.due_at = due_at

        self.status = "New"
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d")

        add_task(self.to_json())

    def to_json(self):
        task_dict = {
            "id": uuid(),  # To avoid json issue
            "name": self.name,
            "task": self.task,
            "priority": self.priority,
            "created_at": self.created_at,
            "due_at": self.due_at,
            "status": self.status,
        }

        return task_dict

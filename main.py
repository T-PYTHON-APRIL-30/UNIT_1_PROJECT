from constants import FILTERS, PRIORITY
from task_management.task import Task
from task_management.task_management import *


print("Welcome To Your Task Manager Program \n")


def create_new_task():
    task_name = input("Enter The Task Name: ")
    task_disc = input("Enter A Description For Your Task: ")
    while True:
        priority_choose = input("What Is The Task Priority? 1. Low 2. Medium 3. High: ")

        if priority_choose not in PRIORITY.keys():
            print("You Entered Invalid Choose")
            continue

        priority = PRIORITY[priority_choose]

        break
        # if priority_choose == "1":
        #     priority = "Low"
        #     break
        # elif priority_choose == "2":
        #     priority = "Medium"
        #     break
        # elif priority_choose == "3":
        #     priority = "High"
        #     break
        # else:
        #     "You Entered Invalid Choose"
    due_at = input("Enter Task Due Date, Format is YYYY-MM-DD:")
    Task(task_name, task_disc, priority, due_at)
    print("The Task Has Been Added")


def display_current_task():
    tasks = current_task()

    print("Enter The Task Number To View : ")
    for index, task in enumerate(tasks):
        print(index, task["name"])

    task_choose = input("= ")

    for index, task in enumerate(tasks):
        if int(task_choose) == index:
            for k, v in task.items():
                if k != "id":
                    print(k, " : ", v)

            print(8 * ("_"))

            completed_or_not = input(
                "Do You Want To Mark This Task As Completed? 'y' or 'n' "
            )

            if completed_or_not.lower() == "y":
                mark_as_completed(task["id"])


def search_for_task():
    tasks = read_tasks()

    while True:
        print("Which Filter Do You Want To Use For Search: ")
        print("1. Name")
        print("2. Priority")
        print("3. Due_At")
        filter_choose = input(" = ")
        # if filter_choose == "1":
        #     search_factor = "name"

        # elif filter_choose == "2":
        #     search_factor = "priority"

        # elif filter_choose == "3":
        #     search_factor = "name"

        # else:
        if filter_choose not in FILTERS.keys():
            print("Wrong Entry")
            continue

        search_factor = FILTERS[filter_choose]

        name_filter = input("What Are You Searching For: ")
        filtered_tasks = filter_task(tasks, search_factor, name_filter)
        print_tasks(filtered_tasks)


while True:
    print("1. Add New Task ")
    print("2. Display Current Tasks")
    print("3. Display Completed Tasks")
    print("4. Search Task")
    print("5. Exit")

    choose = input("Enter Your Choose : ")

    # Add New Task
    if choose == "1":
        create_new_task()
        break

    # Display Current Tasks
    elif choose == "2":
        display_current_task()
        break

    # Display Completed Task
    elif choose == "3":
        completed_tasks = completed_task()
        print_tasks(completed_task)
        break

    # search
    elif choose == "4":
        search_for_task()
        break

    # exit
    elif choose == "5":
        print("Thanks For Using Task Manager Program, See You Next Time")
        break

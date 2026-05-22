from datetime import datetime
from models.schemas import Status

tasks_db = {}
task_counter = 1


def create_task(data, status):
    global task_counter

    # Duplicate title check
    for task in tasks_db.values():
        if task.title == data.title:
            raise Exception("Task with same title already exists")

    # HIGH priority rule
    if data.priority == "HIGH" and not data.description:
        raise Exception("HIGH priority task must have description")

    # Max 3 active tasks per user
    active_tasks = [
        t for t in tasks_db.values()
        if t.assigned_to == data.assigned_to and t.status != "DONE"
    ]
    if len(active_tasks) >= 3:
        raise Exception("User already has 3 active tasks")

    task = data.dict()
    task["task_id"] = task_counter
    task["status"] = status
    task["created_at"] = datetime.now()
    task["internal_notes"] = ""

    tasks_db[task_counter] = task
    task_counter += 1

    return task


def update_task(task_id, data):
    task = tasks_db.get(task_id)

    if not task:
        return None

    # Status rules
    if data.status:
        if task["status"] == Status.OPEN and data.status == Status.DONE:
            raise Exception("Invalid status transition")
        if task["status"] == Status.OPEN and data.status != Status.IN_PROGRESS:
            raise Exception("Must move to IN_PROGRESS first")

        task["status"] = data.status

    if data.title:
        task["title"] = data.title

    if data.priority:
        task["priority"] = data.priority

    return task

def get_tasks():
    return list(tasks_db.values())


def get_tasks_filtered(priority=None):
    tasks = list(tasks_db.values())
    if priority:
        tasks = [t for t in tasks if t["priority"] == priority]
    return tasks
'''
Module that saves and loads the tasks
'''
import json
from task import Task

def load_tasks():
    '''
    Loads the task
    '''
    try:
        with open("tasks.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            tasks = [Task.from_dict(item) for item in data]
            return tasks
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Unkown Error: {e}")
        return []

def save_tasks(tasks):
    '''
    Saves the task
    '''
    with open("tasks.json", 'w', encoding="utf-8") as f:
        data = [task.to_dict() for task in tasks]
        json.dump(data, f, indent=4, ensure_ascii=False)

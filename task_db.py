
__author__ = "Manuel Aigner"
__version__ = "1.0.0"
__maintainer__ = "Manuel Aigner"
__email__ = "manuelaigner@gmx.de"
__status__ = "Development"

import json_handler
from datetime import date


class Task:

    def __init__(self, title = '', description = '', priority = 0):
        self.id = 0
        self.title = ''
        self.date = str(date.today().strftime("%d-%m-%Y"))
        self.description = description
        self.priority = priority

    def from_json(self, title, id, date, description = '', priority = 0):
        self.id = id
        self.title = title
        self.date = date
        self.description = description
        self.priority = priority

    def __str__(self):
        print('['+ self.id + ']: ' + self.date + ':' + self.title)


def from_json(json_task):
    task = Task()

    if 'title' in json_task:
        task.title = json_task['title']
    
    if 'description' in json_task:
        task.description = json_task['description']
    
    if 'date' in json_task:
        task.date = json_task['date']
    else:
        print('Read task without date')

    if 'priority' in json_task:
        task.priority = json_task['priority']

    if 'id' in json_task:
        task.id = json_task['id']
    else:
        print('Read task without id')
        #error: trying to read task without id

    return task
    #conversion from json to Task required

def to_json(task):
    
    json_task = {}
    json_task['title'] = task.title
    json_task['id'] = task.id
    json_task['priority'] = task.priority
    json_task['date'] = task.date
    json_task['description'] = task.description
    return json_task
    #conversion from Task to json required


class TaskDBHandler:

    def __init__(self, filename):
        self.tasks = []
        self.json_handle = json_handler.JsonHandler(filename)
        self.load_tasks()

    def load_tasks(self):
        if self.json_handle.is_file_good():
            for json_task in self.json_handle.get_content()['tasks']:
                self.tasks.append(from_json(json_task))
    
    def write_tasks(self):
        _content = {}
        _content['tasks'] = []

        for task in self.tasks:
            _content['tasks'].append(to_json(task))    
        
        self.json_handle.write_content(_content)
        self.json_handle.write_to_json()
    
    def add_task(self, task):
        task.id = self.get_last_id() + 1
        self.tasks.append(task)
        self.write_tasks()

    def remove_task(self, id):
        for task in self.tasks:
            if (task['id']) == id:
                self.tasks.remove(task)
                self.write_tasks()
                return True
        return False
    
    def update_task(self, updated_task):

        for task in self.tasks:
            if updated_task.id == task.id:
                task = updated_task
                self.write_tasks()
                return True
        return False

    def get_last_id(self):
        try:
            return self.tasks[-1].id
        except:
            return 0



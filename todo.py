
__author__ = "Manuel Aigner"
__version__ = "1.0.0"
__maintainer__ = "Manuel Aigner"
__email__ = "manuelaigner@gmx.de"
__status__ = "Development"

import os
import sys
import argparse
import json
import task_db

META_FOLDER = 'C:/scripts/todo'
DATA = "C:/data/todo/database.json"
TASK_SECTION = 'tasks'

taskDBHandle = task_db.TaskDBHandler(DATA)

#def show_list():
#    database = load_todo_list_from_storage()
#    for todo in database[TASK_SECTION]:
#        print('[' + str(todo['id']) + ']: ' + todo['date'] + ' : ' + todo['title'])#

#def generate_id(database):
#    if not database[TASK_SECTION]:
#        return 0
#    else:
#        return int(database[TASK_SECTION][-1]['id']) + 1

#def remove_task(id):
#    database = load_todo_list_from_storage()
#    
#    for task in database[TASK_SECTION]:
#        if (task['id']) == id:
#            database[TASK_SECTION].remove(task)
#            store_todo_list(database)
#            return
#    
#    print('No task found with id: ' + str(id))
#    show_list()

def command_add_task(args):

    task = task_db.Task()

    if args.task:
        task.title = args.task[0]
    else:
        raise ValueError('When adding a task a title must be set. Use -t [TASK_TITLE] to specify it.')

    if args.description:
        task.description = args.description[0]

    if args.priority:
        task.priority = args.priority[0]

    taskDBHandle.add_task(task)

def command_list_task(args):
    
    if args.all:
        for task in taskDBHandle.tasks:
            print(task)
            
def command_edit(args):
    print('list all tasks')


def command_line():
    parser = argparse.ArgumentParser(description='This is a command line todo-list.')
    subparsers = parser.add_subparsers()

    #create parser for adding tasks
    add_parser = subparsers.add_parser('add', help='add new task')
    add_parser.set_defaults(func=command_add_task)
    add_parser.add_argument('-t', '--task', action='store', nargs=1, help="Adds an task.")
    add_parser.add_argument('-d', '--description', action='store', nargs=1, help="Adds an description to an task")
    add_parser.add_argument('-p', '--priority', action='store', nargs=1, help='adds a priority to a task')
    
    #create parser for listing tasks
    list_parser = subparsers.add_parser('list', help='list tasks and settings')
    list_parser.set_defaults(func=command_list_task)
    list_parser.add_argument('-a', '--all', action='store_true', help='lists all stored task in random order')
    list_parser.add_argument('-i', '--id', action='store', nargs=1, help='list task with specified id')
    list_parser.add_argument('-c', '--category', action='store', nargs=1, help='list all tasks with specified category')
    list_parser.add_argument('-p', '--priority', action='store', nargs=1, help='list all tasks with priority greater then or equal to specified number')
    
    #create parser for editing tasks
    edit_parser = subparsers.add_parser('edit', help='edit tasks and settings')
    edit_parser.set_defaults(func=command_edit)
    edit_parser.add_argument('-i', '--task', action='store', nargs=1, help='list task with specified id')
    edit_parser.add_argument('-t', '--title', action='store', nargs=1, help='list task with specified id')
    

    #create parser for removing tasks

    #create parser for workspace creator

    try:
        args = parser.parse_args()
        args.func(args)
    except SystemExit as e:
        if e.code != 0:
            print("Invalid arguments")
            sys.exit(e.code)
    except ValueError as e:
        print(e)

def main():
    command_line()

main()
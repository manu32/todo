
__author__ = "Manuel Aigner"
__version__ = "1.0.0"
__maintainer__ = "Manuel Aigner"
__email__ = "manuelaigner@gmx.de"
__status__ = "Development"

import os
import sys
import argparse
import json

from datetime import date

META_FOLDER = 'C:/scripts/todo'
DATA = "C:/data/todo/database.json"
TASK_SECTION = 'tasks'

def show_list():
    database = load_todo_list_from_storage()
    for todo in database[TASK_SECTION]:
        print('[' + str(todo['id']) + ']: ' + todo['date'] + ' : ' + todo['title'])

def add_task(arg):
    database = load_todo_list_from_storage()
    database[TASK_SECTION].append({
        'id': generate_id(database),
        'title': arg[0],
        'date': str(date.today().strftime("%d-%m-%Y"))
    })
    store_todo_list(database)

def generate_id(database):
    if not database[TASK_SECTION]:
        return 0
    else:
        return int(database[TASK_SECTION][-1]['id']) + 1

def remove_task(id):
    database = load_todo_list_from_storage()
    
    for task in database[TASK_SECTION]:
        if (task['id']) == id:
            database[TASK_SECTION].remove(task)
            store_todo_list(database)
            return
    
    print('No task found with id: ' + str(id))
    show_list()

def command_line():
    parser = argparse.ArgumentParser(prog='PROG', description='This is a command line todo-list.')
    parser.add_mutually_exclusive_group()
    parser.add_argument('-l', '--list', action='store_true')
    parser.add_argument('-a', '--add', action='store', nargs=1)
    parser.add_argument('-r', '--remove', action="store", nargs=1, type=int)
    parser.add_argument('-d', '--description', action='store', nargs=1)
    parser.add_argument('-p', '--priority', action="store", nargs=1)
        
    add_parser = subparsers.add_parser('add', help='add new task')
    add_parser.add_argument('-t', '--task', action='store', nargs=1, help="Adds an task.")
    add_parser.add_argument('-d', '--description', action='store', nargs=1, help="Adds an description to an task")
    add_parser.add_argument('-p', '--priority', action='store', nargs=1, help='adds a priority to a task')
    
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser('add', help='add new task')
    add_parser.add_argument('-t', '--task', action='store', nargs=1, help="Adds an task.")
    add_parser.add_argument('-d', '--description', action='store', nargs=1, help="Adds an description to an task")
    
    try:
        args = parser.parse_args()
    except SystemExit as e:
        if e.code != 0:
            print("Invalid arguments")
            sys.exit(e.code)

    if args.list:
        show_list()
    elif args.add:
        add_task(args.add)
    elif args.remove:
        remove_task(args.remove[0])
    elif args.task:
        print(args.task[0])
    if args.description:
        print(args.description[0])

def load_todo_list_from_storage():
    database = {}
    database[TASK_SECTION] = []
    
    if os.path.isfile(DATA):
        with open(DATA) as json_file:
            database = json.load(json_file)
    return database

def store_todo_list(database):
    with open(DATA, 'w') as json_file:
        json.dump(database, json_file, indent=2)

def main():
    command_line()

main()
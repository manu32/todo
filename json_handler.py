
__author__ = "Manuel Aigner"
__version__ = "1.0.0"
__maintainer__ = "Manuel Aigner"
__email__ = "manuelaigner@gmx.de"
__status__ = "Development"

import os
import sys
import json

class JsonHandler:

    def __init__(self, filename):
        self.filename = filename
        self.content_good = False
        self.json_content = {}
        self.load_content_from_file()

    def is_file_good(self):
        """Checks if persistency file is good"""
        return os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0

    def get_content(self):
        if self.content_good:
            return self.json_content

    def write_content(self, new_content):
        self.json_content = new_content
        self.write_to_json()

    def is_file_empty(self):
        return not self.json_content

    def load_content_from_file(self):
        if self.is_file_good():
            with open(self.filename) as json_file:
                self.json_content = json.load(json_file)
                self.content_good = True

    def write_to_json(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self.json_content, json_file, indent=2)
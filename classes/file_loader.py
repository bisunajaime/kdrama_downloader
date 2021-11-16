
import json

class FileLoader:
    def __init__(self, path):
        self.path = path
    
    def load_file(self):
        file = open(self.path)
        return json.load(file)

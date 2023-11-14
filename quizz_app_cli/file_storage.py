from questions import question
from quiz import quiz
import json
import os

class FileStorage():
    """this is the class which the instance will be used to save files"""
    file_path = "file.json"
    objects = {}

    def new(self, new_quiz):
        """adds a new quiz instance to the file storage"""
        print(type(new_quiz))
        name = new_quiz.get("name")
        FileStorage.objects.update({name: new_quiz})
    
    def reload(self):
        """this method reloads files from json"""
        if os.path.exists(FileStorage.file_path) and os.path.getsize(FileStorage.file_path) > 0:
            try:
                with open(FileStorage.file_path, 'r') as json_file:
                    FileStorage.objects = json.load(json_file)
                    print("---reloaded objects---")
                    print(FileStorage.objects)
            except Exception as e:
                return e
    
    def save(self):
        """saves a json file to storage"""
        with open(FileStorage.file_path, 'w') as json_file:
            json.dump(FileStorage.objects, json_file)
    

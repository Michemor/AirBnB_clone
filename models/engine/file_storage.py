import json
import os


class FileStorage:
    __file_path = "file.json"
    # will store all objects by class name and id
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)

    def reload(self):
         from models.base_model import BaseModel
         from models.user import User

         classes =  {"BaseModel": BaseModel, "User": User,}

         if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    objs = json.load(file)
            except Exception as e:
                raise e
            else:
                for key, obj in objs.items():
                    class_name = key.split(".")[0]
                    self.__objects[key] = classes[class_name](**obj)
         else:
            pass
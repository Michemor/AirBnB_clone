#!/usr/bin/python3

"""
Defines class HBNBCommand
"""

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes =  {"BaseModel": BaseModel, "User": User,
            "Place": Place, "State": State, "City": City,
           "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """
        Exits The Program
        """
        return True
    
    def do_quit(self, line):
        """
        Quit Command for program
        """
        return True
    
    def emptyline(self):
        """
        Ignores Empty Lines
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of a class, saves it(to the JSON file)
        and prints the id
        """
        if line:
            if line not in classes:
                print("** class doesn't exist **")
            else:
                obj = classes[line]()
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            objs = storage.all()
            if key in storage.all():
                print(objs[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id and saves the changes to JSON File
        (file.json)
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        args = line.split()
        # empty list but will store string representation of objects
        list_objs = []
        if len(args) == 0 or not args[0].strip() in classes:
            for obj in storage.all().keys():
                list_objs.append(str(storage.all()[obj]))
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on class name and id
        by adding or updating attribute and saves the changes
        into the JSON file(file.json)
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            if key in storage.all():
                storage.all()[key].__dict__[args[2]] = args[3]
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
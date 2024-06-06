#!/usr/bin/python3

"""
Defines class HBNBCommand
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
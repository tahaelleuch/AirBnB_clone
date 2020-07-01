#!/usr/bin/python3
"""Hbnb: The consol"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City


class HBNBCommand(cmd.Cmd):
    """Class to define consol's command"""

    prompt = "(hbnb) "
    class_name = {"BaseModel": BaseModel,
                  "User": User,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Place": Place,
                  "Review": Review
                  }

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def do_quit(self, arg):
        """(quit) to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldnt execute anything"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if args == []:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
            return
        else:
            if args[0] in HBNBCommand.class_name:
                models.storage.reload()
                new_inst = HBNBCommand.class_name[args[0]]()
                new_inst.save()
                print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            index = args[0] + "." + args[1]
            alls = models.storage.all()
            if index in alls:
                print(alls[index])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            index = args[0] + "." + args[1]
            alls = models.storage.all()
            if index not in alls:
                print("** no instance found **")
            else:
                if index in alls:
                    alls.pop(index)
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        pr_list = []
        models.storage.reload()
        if len(args) == 0:
            for key, values in models.storage.all().items():
                pr_list.append(str(values))
        else:
            if args[0] not in HBNBCommand.class_name:
                print("** class doesn't exist **")
                return
            if args[0] in HBNBCommand.class_name:
                for key, values in models.storage.all().items():
                    if values.__class__.__name__ == args[0]:
                        pr_list.append(values.__str__())
        print(pr_list)

    def do_update(self, arg):
        """Updates an instance based
        on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            index = args[0] + "." + args[1]
            alls = models.storage.all()
            if index not in alls:
                print("** no instance found **")
            else:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(alls[index], args[2], args[3])
                    models.storage.all()[index].save()

    def default(self, arg):
        """special command lineS"""
        cmd_all = arg.split('.')
        if (len(cmd_all) == 2):
            if cmd_all[0] in HBNBCommand.class_name and cmd_all[1] == "all()":
                self.do_all(cmd_all[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()

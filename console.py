#!/usr/bin/python3
"""Hbnb: The consol"""

import cmd
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class to define consol's command"""

    prompt = "(hbnb) "
    class_name = ["BaseModel"]

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def do_quit(self, arg):
        """(quit) to exit the program"""
        return True

    def do_help(self, arg: str):
        """Get help"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
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
            models.storage.reload()
            new_inst = eval(args[0])()
            new_inst.storage.save()
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
                for key, values in alls.items():
                    if key is index:
                        del(alls[key])
                        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        if args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
            return
        pr_list = []
        models.storage.reload()
        if len(args) == 0:
            for key, values in models.storage.all().items():
                pr_list.append(str(values))
        else:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
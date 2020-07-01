#!/usr/bin/python3
"""Hbnb: The consol"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
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

    def do_count(self, arg):
        """Get the  the number of instances of a class"""
        args = arg.split(" ")
        i = 0
        if args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif args[0] is not None:
            alls = models.storage.all()
            names = [""]
            for key in alls:
                names = key.split(".", 1)
                if names[0] == args[0]:
                    i += 1
        print(i)

    def default(self, arg):
        """special command lineS"""
        cmd_all = arg.split('.')
        if (len(cmd_all) == 2):
            if cmd_all[1].find("()") != -1:
                if cmd_all[0] in HBNBCommand.class_name \
                        and cmd_all[1] == "all()":
                    self.do_all(cmd_all[0])
                if cmd_all[0] in HBNBCommand.class_name \
                        and cmd_all[1] == "count()":
                    self.do_count(cmd_all[0])
            else:
                begin = cmd_all[1].find('(')
                end = (cmd_all[1].find(')')) + 1
                the_values = cmd_all[1][begin+1:end-1]
                the_id = cmd_all[1][begin + 2:end - 2]
                the_command = cmd_all[1][0:begin]
                if cmd_all[0] in HBNBCommand.class_name \
                        and the_command == "show":
                    self.do_show(cmd_all[0] + ' ' + the_id)
                    return
                if cmd_all[0] in HBNBCommand.class_name \
                        and the_command == "destroy":
                    self.do_destroy(cmd_all[0] + ' ' + the_id)
                    return
                if the_values.find(", ") != -1:
                    all_values = the_values.split(", ")
                    for i in all_values:
                        i = i[1:-1]
                if cmd_all[0] in HBNBCommand.class_name \
                        and the_command == "update":
                    self.do_update(cmd_all[0] + ' ' + all_values[0] +
                                   ' ' + all_values[1] +
                                   ' "' + all_values[2] + '"')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

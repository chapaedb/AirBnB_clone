#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = cls_name + "." + obj_id
            obj = storage.get(cls_name, obj_id)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = cls_name + "." + obj_id
            obj = storage.get(cls_name, obj_id)
            if obj:
                storage.delete(obj)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        args = arg.split()
        obj_list = []
        if not args:
            obj_list = list(storage.all().values())
        else:
            try:
                cls_name = args[0]
                obj_list = storage.all(cls_name)
            except NameError:
                print("** class doesn't exist **")
                return

        print([str(obj) for obj in obj_list])

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = cls_name + "." + obj_id
            obj = storage.get(cls_name, obj_id)
            if not obj:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def postcmd(self, stop, line):
        self.prompt = "(hbnb) "
        return stop

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

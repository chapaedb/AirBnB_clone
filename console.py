import cmd
from models.base_model import BaseModel
from models import file_storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.uuid)
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
            if key in storage.all():
                print(storage.all()[key])
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
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        args = arg.split()
        obj_list = []
        if not args:
            obj_list = list(storage.all().values())
        else:
            try:
                cls_name = args[0]
                for key in storage.all():
                    if key.split(".")[0] == cls_name:
                        obj_list.append(storage.all()[key])
            except NameError:
                print("** class doesn't exist **")
                return

        print([str(obj) for obj in obj_list])
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute."""
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
            if key not in storage.all():
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
            obj = storage.all()[key]
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

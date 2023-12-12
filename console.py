import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parses the argument into a list of tokens."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter for Airbnb project."""

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, line):
        """Create a new instance of a class."""
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
        """Show the string representation of an instance."""
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
        """Delete an instance based on the class name and id."""
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
        """Print all instances or instances of a specific class."""
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
        """Update an instance's attribute based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

```python
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
        """Exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program."""
        print()
        return True

    def postcmd(self, stop, line):
        """Executed after each command."""
        self.prompt = "(hbnb) "
        return stop

    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

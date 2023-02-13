#!/usr/bin/python3
<<<<<<< HEAD
""" Holberton AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
=======
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '
<<<<<<< HEAD
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()
=======
    myclasses = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                 "City"]

    def do_EOF(self, line):
        ''' exit the program '''
        return True

    def help_EOF(self):
        ''' help EOF'''
        print("EOF command to exit the program\n")

    def help_quit(self):
        ''' help quit '''
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        ''' quit interpreter '''
        return True
>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639

    def emptyline(self):
        ''' do nothing with empty line '''
        pass

<<<<<<< HEAD
    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')
=======
    def do_create(self, classname):
        ''' create a new instance of '''
        if len(classname) == 0:
            print('** class name missing **')
        elif classname not in self.myclasses:
                print('** class doesn\'t exist **')
                return False
        else:
            new = eval("{}()".format(classname))
            new.save()
            print(new.id)

    def help_create(self):
        ''' help create '''
        print("Create command to create a class\n")

    def do_show(self, line):
        '''represents an instance'''
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False

        if len(args) < 2:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        for i in all_objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objs[i])
                return False
        print('** no instance found **')

    def help_show(self):
        ''' help show '''
        print("Show command to display the string representation of class\n")

    def do_destroy(self, line):
        ''' deletes an instance based on the class id'''
        args = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        elif len(args) < 2:
            print('** instance id missing **')
            return False
        else:
            all_objs = storage.all()
            for i in all_objs:
                if i == "{}.{}".format(args[0], args[1]):
                    all_objs.pop(i)
                    storage.save()
                    return False
            print('** no instance found **')

    def help_destroy(self):
        ''' help destroy '''
        print("Destroy command to destroy an object\n")

    def do_all(self, line):
        ''' prints all string representations of instances'''
        args = line.split()
        all_objs = storage.all()

        if len(args) == 0:
            for i in all_objs:
                strarg = str(all_objs[i])
                print(strarg)
        elif line not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    strarg = str(all_objs[i])
                    print(strarg)
        return False

    def help_all(self):
        ''' help all'''
        print("All command to show all instances\n")

    def do_update(self, line):
        ''' updates an instance based on class name and id'''
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            instanceid = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attributename = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            updatevalue = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if updatevalue.isdecimal() is True:
            setattr(clschange, attributename, int(updatevalue))
            storage.save()
        else:
            try:
                setattr(clschange, attributename, float(updatevalue))
                storage.save()
            except:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()

    def help_update(self):
        '''help update'''
        print("update command to update attributes\n")

>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639

if __name__ == '__main__':
    HBNBCommand().cmdloop()

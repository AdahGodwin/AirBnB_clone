<<<<<<< HEAD
import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """ setup for tests """
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """ tear down method """
        sys.stdout = self.old_stdout

    def test_create(self):
        """ test create method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            string = f.getvalue()
            self.assertEqual(string[:-1], "cfb59c53-51e2-45c3-a049-85c52b648037\n")

    def test_show(self):
        """ test show method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            string = f.getvalue()
            bm_id = string[:-1]
            HBNBCommand().onecmd("show BaseModel " + bm_id)
            string = f.getvalue()
            self.assertIn("[BaseModel]", string)
            self.assertIn("'id': '" + bm_id + "'", string)
            self.assertIn("'created_at':", string)
            self.assertIn("'updated_at':", string)

    def test_destroy(self):
        """ test destroy method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            string = f.getvalue()
            bm_id = string[:-1]
            HBNBCommand().onecmd("destroy BaseModel " + bm_id)
            string = f.getvalue()
            self.assertIn("Deleted", string)
            HBNBCommand().onecmd("show BaseModel " + bm_id)
            string = f.getvalue()
            self.assertIn("** no instance found **", string)

    def test_all(self):
        """ test all method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
            HBNBCommand().onecmd("all")
            string = f.get

=======
#!/usr/bin/python3
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)


class TestHBNBCommandPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestHBNBCommand(unittest.TestCase):
    """ tests for class HBNBCommand """
    pass
>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639

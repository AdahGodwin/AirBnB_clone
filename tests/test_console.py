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


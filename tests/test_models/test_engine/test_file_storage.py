#!/usr/bin/python3
"""
module de test pour file storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    module de test
    """

    def test_instance_file_str(self):
        """
        test des attributs
        """
        self.assertIsInstance(storage, FileStorage)

    def test_path_file_strorage(self):
        """ Check file_path type """
        stor = FileStorage()
        self.assertIsInstance(stor.__file_path, str)

    def test_file_storage_dict(self):
        """
         test de dictionnaire
        """
        stor = storage.all()
        self.assertIsInstance(stor, dict)

#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""
classe init
"""

storage = FileStorage()
storage.reload()
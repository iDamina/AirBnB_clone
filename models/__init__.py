#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.storage.file_storage import FileStorage


storage = FileStorage()
storage.reload()

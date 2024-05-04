#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder
in the AirBnB Clone repository.
"""
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(filename))
    if os.path.exists(filename):
        return filename
    else:
        return None

#!/usr/bin/python3
"""
A script that distributes an archive to my web servers
"""
from os import path
from fabric.api import env, run, put, local
from datetime import datetime

env.hosts = ['54.86.218.226', '3.84.161.199']
env.user = 'ubuntu'


def do_pack():
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(filename))
    if path.exists(filename):
        return filename
    else:
        return None


def do_deploy(archive_path):
    if path.exists(archive_path):

        archive = archive_path.split('/')[1]

        ra_path = "/tmp/{}".format(archive)
        r_folder = archive.split('.')[0]
        rd_path = "/data/web_static/releases/{}/".format(r_folder)

        put(archive_path, ra_path)

        run("mkdir -p {}".format(rd_path))
        run("tar -xzf {} -C {}".format(ra_path, rd_path))
        run("rm {}".format(ra_path))
        run("mv -f {}web_static/* {}".format(rd_path, rd_path))
        run("rm -rf {}web_static".format(rd_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(rd_path))
        return True
    return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

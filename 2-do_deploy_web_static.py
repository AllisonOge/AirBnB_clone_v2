#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os import path


env.hosts = ['52.86.239.20', '100.26.241.183']
def do_deploy(archive_path):
    """Function to deploy"""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False

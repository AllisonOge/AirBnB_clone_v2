#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import env


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['52.86.239.20', '100.26.241.183']


def deploy():
    """Function to deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

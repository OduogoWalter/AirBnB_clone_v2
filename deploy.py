#!/usr/bin/python3
"""Deploy web_static using Fabric."""
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.87.238.72', '35.153.52.13']

def pack():
    """Generate a .tgz archive from web_static."""
    local("mkdir -p versions")
    archive_path = local("tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static", capture=True)
    return archive_path

def deploy():
    """Distribute the archive to web servers."""
    archive_path = pack()
    if archive_path.failed:
        return False
    remote_path = "/tmp/" + archive_path.split("/")[-1]
    put(archive_path, remote_path)
    remote_folder = "/data/web_static/releases/" + archive_path.split("/")[-1][:-4]
    run("mkdir -p {}".format(remote_folder))
    run("tar -xzf {} -C {}".format(remote_path, remote_folder))
    run("rm {}".format(remote_path))
    run("ln -sf {} /data/web_static/current".format(remote_folder))
    return True

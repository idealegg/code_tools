import MySshClient.MySshClient
import os
import sys


remote_dir = '/home/huangd/btma/src/'


def get_remote_file_name(cur_file, cur_project):
    cur_dir = os.getcwd()
    os.chdir(cur_project)
    rel_path = os.path.relpath(cur_file)
    os.chdir(cur_dir)
    return os.path.join(remote_dir, rel_path.replace(os.sep, '/'))


def upload_files(cur_file, cur_project):
    remote_file = get_remote_file_name(cur_file, cur_project)
    mc = MySshClient.MySshClient.MySshClient('id_rsa_2048', 'E:/Program Files (x86)/Git/.ssh/known_hosts',
                                             '192.168.118.119', 'huangd')
    mc.initialize()
    print mc.upload_file(cur_file, remote_file)
    mc.close()


if __name__ == '__main__':
    upload_files(sys.argv[1], sys.argv[2])



#!/bin/env python

import paramiko
import ssh
import os

def Main():

  print "1. Begin to login to tai2... init client"
  myclient=ssh.SSHClient()
  myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())

  print "2. Begin to login to tai2... connect to server"
  myclient.connect("192.168.118.119", port=22, username="****", password="****")

  print "3. Run script get_code in tai2"
  stdin,stdout,stderr=myclient.exec_command("/home/huangd/tools/get_code.ksh /home/huangd/tmp/stma_jv_ada")
  print stdout.read()

  print "4. Open sftp in tai2..."
  sftp=myclient.open_sftp()

  print "5. Get archive file from tai2..."
  sftp.get("/home/huangd/tmp/stma_jv_ada.tar.gz", "D:\\sourceCode\\stma_jv_ada\\stma_jv_ada.tar.gz")
  myclient.close()

  print "6. Start uncompressing the archive file..."
  os.system("\"H:\\Program Files\\WinRAR\\WinRAR\" x -y -ibck -ad D:\\sourceCode\\stma_jv_ada\\stma_jv_ada.tar.gz D:\\sourceCode\\stma_jv_ada")

  print "7. Upate code successfully..."


def Main2():

  key = paramiko.RSAKey.from_private_key_file('id_rsa_2048')
  s = paramiko.SSHClient()
  s.load_system_host_keys()

  s.load_system_host_keys('E:/Program Files (x86)/Git/.ssh/known_hosts')
  s.connect('192.168.118.119', 22, "huangd", pkey=key)
  stdin, stdout, stderr = myclient.exec_command("pwd")

  stdin, stdout, stderr = s.exec_command("pwd")
  print stdout.read()


if __name__ == "__main__":
  Main()

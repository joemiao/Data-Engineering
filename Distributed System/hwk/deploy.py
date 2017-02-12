
# coding: utf-8

# In[35]:

import tarfile
import sys
import argparse
import os
import json
import paramiko


# ### Set up command line syntax

# In[42]:

parser = argparse.ArgumentParser(description='This is a script for deploying tar.gz package to hdfs')
parser.add_argument('--package_path', help='Specify package path', type = str)
parser.add_argument('--upload_path',help='Specify the file path on the local server on the cluster (file name included)', type = str)
parser.add_argument('--install_root',help='The root path on hdfs where the package is installed', type = str)
args = parser.parse_args()


# ### Read command line inputs to variables 

# In[41]:

pkg_path = args.package_path
install_root = args.install_root
upload_path = args.upload_path

if not install_root.endswith("/"):
	install_root = install_root + "/"


# ### Connect to cluster

# In[37]:

config = json.load(open('/Users/zeyumiao/DE/config.txt'))
print(config['hostname'])


# In[39]:

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect(hostname=config['hostname'],username=config['username'], port = config['port'], password=config['passwd'])


# ### Upload tar to cluster

# In[43]:

sftp = ssh.open_sftp()
print(pkg_path, upload_path)
sftp.put(pkg_path, upload_path)
sftp.close()


# ### Create commands to be exeuted in the remote server's shell

# In[17]:

#Steps: 
#1.cd into the directory where the tar is uploaded to on the remote server
#2.unpack tar file
#3.copy folders to hdfs


# ### Copy and uncompress file to HDFS without unziping the file on local filesystem

# In[12]:

upload_root = "/".join(upload_path.split("/")[:-1]) + "/"


# In[1]:

tar_name = pkg_path.split("/")[-1]


# In[ ]:

cmds = "cd %s && mkdir temp && mv %s temp && cd temp && tar -xvzf %s && find -maxdepth 1 -mindepth 1 -type d \( ! -name '.*' \) -exec hdfs dfs -put {} %s \;"%(upload_root, tar_name, tar_name, install_root)
print(cmds)


# In[ ]:

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmds)


# In[ ]:

ssh.close()
print('Finished')


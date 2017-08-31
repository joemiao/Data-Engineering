# HDFS App Installer

A simple python script that deploys a distributted application to a Hadoop Cluster. 

It uploads an gzip'ed tar file ( .tar.gz ) on your local Unix computer to a remote server on a Hadoop cluster, unpackages the tar file on the remote and then copies the entire folder from the remote server to HDFS.

## Getting Started

Download the script and open it to change the file path of the config.txt
to your own.

Make sure the tar file is in the same local directory as deploy.py.

Command Line:

python deploy.py --package_path xxx.tar.gz --upload_path "full file path where you want to upload the tar file to on the remote"(including tar file name) --install_root "hdfs path where you want your app to deploy to"(do not include tar file name)

### Prerequisites

import tarfile
import sys
import argparse
import os
import json
import paramiko

```
Give examples

python deploy.py --package_path data-app-application-1.0.0-dataapp-assembly.tar.gz --upload_path /home/smith/installation/data-app-application-1.0.0-dataapp-assembly.tar.gz --install_root /user/smith/temp/

```

## Versioning

1.0

## Authors

Joe Miao (miaozeyu@gmail.com)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Paramiko

#!/bin/bash

sudo apt update
sudo apt install -y python3 python3-venv wget

archive_url="https://www.dropbox.com/s/ija7ax3sj6ysb0p/blocknote-master.tar.gz"
archive_name="blocknote-master.tar.gz"

wget -O "$archive_name" "$archive_url"

project_dir="project"
mkdir "$project_dir"
tar -xvf "$archive_name" -C "$project_dir"

cd "$project_dir"

python3 -m venv venv
source ./venv/bin/activate

which pip

./venv/bin/python -m pip install --upgrade pip
./venv/bin/python -m pip install -r ../requirements.txt
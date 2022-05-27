#!/usr/bin/env python

'''
notebook_converter.py

Copyright 2021 Abubakar Yagoub

Modified by Leshui He, 2022

This script converts a jupyter notebook to markdown
and moves converted markdown to posts and images to assets.
Requirements:
- jupyter (for converting notebooks to md)
'''

import glob
import os
from datetime import datetime
import subprocess

post_dir = "_posts/"
notebooks_dir = "notebooks/"
assets_dir = "assets/images/"
current_date = datetime.today().strftime('%Y-%m-%d')
# perm_link_str = datetime.strftime('/posts/%Y/%m/:title/')
front_matter = """---
title: {}
permalink: "/posts/:title/"
tags:
  - stata
  - python
excerpt_separator: <!--more-->
---\n\n"""

# get all notebook files
filenames = glob.glob(notebooks_dir + '*.ipynb')

def check_exists(file):
    """check if a post from a notebook has already been created"""
    for post in glob.glob(post_dir + "/*.md"):
        if file in post:
            return True
    return False

# debug
file = filenames[0]

for file in filenames:
    # get filename without directory prefix and extension
    name = file.split("/")[1].split(".")[0]
    new_name = f"{notebooks_dir}{current_date}-{name}.md"
    if check_exists(name):
        print(f"post for {name} has already been created.")
        continue

    # note: need nbconvert at lower version: pip install nbconvert==5.6.1
    os.system(f"jupyter nbconvert --to markdown {file}")

    # rename with date
    os.system(f"mv {notebooks_dir}{name}.md {new_name}")

    f = open(new_name, "r+")
    content = f.readlines()
    for i, line in enumerate(content):
        # fix assets path
        content[i] = content[i].replace("![png](", "![png](/assets/images/")
        content[i] = content[i].replace("![svg](", "![png](/assets/images/")
    f.seek(0)
    f.write(front_matter.format(name.replace("-", " ").title()))
    f.writelines(content)
    f.close()    

    # move file and assets
    os.system(f"mv {new_name} {post_dir}")
    os.system(f"rm -rf {assets_dir}{name}_files")
    os.system(f"mv {notebooks_dir}{name}_files {assets_dir}")
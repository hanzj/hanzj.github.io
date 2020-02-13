import sys
import os
import shutil
import git


file = "D:\\123.py"
dest = "E:\\Git\\Github\\hanzj.github.io"
img_path = "\\images\\"
(path, filename) = os.path.split(file)
print(dest + img_path + filename)
shutil.copy(file, dest + img_path + filename)
repo = git.Repo(dest)
remote = repo.remote()
remote.pull()
repo.git.add(dest + img_path + filename)
repo.git.commit(m='md')
remote.push()

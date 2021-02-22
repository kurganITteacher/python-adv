import os
import shutil

dir_name = 'src'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
else:
    os.rmdir(dir_name)

dir_name = 'docs/docker'
if not os.path.exists(dir_name):
    # os.mkdir(dir_name)
    os.makedirs(dir_name)
else:
    # os.rmdir(dir_name)
    shutil.rmtree(dir_name)

# python cmd: shutil.copyfile('my_file.txt', './new_dest/')
# os cmd: cp my_file.txt ./new_dest/
# os.rename(), shutil.move()

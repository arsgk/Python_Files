import os
import glob
import shutil

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'xyz_files')

if not os.path.exists(final_directory):
   os.makedirs(final_directory)


os.chdir(current_directory)
for file in glob.glob("*.xyz"):
    
    shutil.move(file, final_directory)
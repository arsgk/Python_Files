'''
module for creating 2 different directories in the working directory 
'''

import os
import glob



current_directory = os.getcwd()
G_blurred_directory = os.path.join(current_directory, r'G_blurred_files')
Thresh_directory = os.path.join(current_directory, r'Thresholded_files')

if not os.path.exists(G_blurred_directory):
   os.makedirs(G_blurred_directory)
   
if not os.path.exists(Thresh_directory):
   os.makedirs(Thresh_directory)
# acccess outside files Read and Write\

# .. means go up one directory level (i.e., the parent directory).

# . means "current directory

import os

from pathlib import Path
from datetime import datetime



# Absolute path
folder_path = "/home/ragu/ragu/project-storage/examples/test-create"

os.makedirs(folder_path, exist_ok=True)

print(f"Folder created: {folder_path}")



# Relative path

relative_folder_path = os.path.join("../../", "output_folder")
# relative_folder_path = os.path.join("../", "output_folder")


os.makedirs(relative_folder_path, exist_ok=True)

# exist_ok=True if file is exist it won't throw error. if define False it will throw error

print(f"Folder created: {relative_folder_path}")


# create dynamic folder

folder_name = "test-folder"
new_path = "/home/ragu/ragu/project-storage/examples/"

create_folder_path = os.path.join(new_path, folder_name)

os.makedirs(create_folder_path, exist_ok=True)

# --------------------------------------------------------------------------------------------

# folder creation using pathlib

# Dynamic folder name
folder_name_1 = f"r_output_folder_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Absolute base path (e.g., your home directory or specific directory)
base_path = Path.home() / "ragu-test-folder-creation"

# Full folder path
full_path = base_path / folder_name_1

# Create the directory
full_path.mkdir(parents=True, exist_ok=True)

print(f"Folder created at: {full_path.resolve()}")


# ------------------------------------------------------------------------------------------

# folder creation using  os

# Dynamic folder name (e.g., with timestamp) here we can call import inside string literal
# folder_name = f"r_output_folder_{__import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')}"
folder_name = "r_output_folder"

# Absolute base directory (e.g., your home directory or another fixed location)
base_dir = os.path.abspath(os.path.expanduser("~/ragu-test-folder-creation"))

# Join to create full absolute path
folder_path = os.path.join(base_dir, folder_name)

# Create the folder
os.makedirs(folder_path, exist_ok=True)

print(f"Folder created at: {folder_path}")



# File Write

test_file_path = os.path.join(folder_path, "data.txt")
file_write  = open(test_file_path, "a")
#\n print nextline- it will move to cursor next line

# single line write
file_write.write("welcome file path reading-1\n")
file_write.write("welcome file path reading-2\n")

# write with list data with single write command
multi_lines = ["welcome file path reading-3 \n", "welcome file path reading-4 \n", "welcome file path reading-5 \n", "welcome file path reading-6 \n"]
file_write.writelines(multi_lines)

file_write.close()


file_read = open(test_file_path, 'r')

for data in file_read:
    print("data", data, end="")
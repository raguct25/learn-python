# File handling

from io import StringIO
import csv

file_data = """1,ragu,yt1004
2,gandhi,yt1003
"""


file = StringIO(file_data)

#print is always print with newline. so print empty line, if want to avoid use end=""
# stripe() is remove begin and end white spaces
# if want to insert data use write method.
# When we write data we should write end of the line so we should move cursor to end - seek(2,0)
# if set cursor in end we should reset seek(0) it will go to top

file.seek(0, 2)
file.write("3, daniel, yt1002")
file.seek(0)

employees = []
for data in file:
    # print(data)
    test_data = data.strip().split(",")
    print(test_data)
    employees.append(test_data)

print("employees", employees)

# Access physical files

# File Write
file_write  = open("data.txt", "a")
#\n print nextline- it will move to cursor next line

# single line write
file_write.write("welcome file path reading-1\n")
file_write.write("welcome file path reading-2\n")

# write with list data with single write command
multi_lines = ["welcome file path reading-3 \n", "welcome file path reading-4 \n"]
file_write.writelines(multi_lines)

file_write.close()

# file read

file_read = open("data.txt", "r")
file_read_all = file_read.readlines() # don't use large file . if update with varible so it took large memory

# Reset pointer to beginning
file_read.seek(0) # if use readlines() the next for data in file_read: won't work. after readlines() opertions the cursor will go to end so we need reset

for data in file_read:
    print("single data", data , end="")

for data in file_read_all:
    print("data:", data , end="")

file_read.close()

# Access CSV file
# it return list of data, each row will make list []

#read mode
# with open("data.csv", "r") as file_csv_read:
#     # rows = csv.reader(file_csv_read) # it read by list view
#     rows = csv.DictReader(file_csv_read, delimiter=",") # it reads by dict view. delimiter=":" its take columns key and next rows will treats value
#     for data in rows:
#         print ("csv data", data)

# Write mode
# r+ read and write mode

field_names = ["emp_id", "emp_name", "emp_role"]
new_data = [{"emp_id": 4, "emp_name": "Test", "emp_role": "Intern"}]

with open("data.csv", "r+", newline="") as file_csv_write:
    rows = csv.reader(file_csv_write, delimiter=",")
    for data in rows:
        print("data", data)
    
     # Move file pointer to the end
    # file_csv_write.seek(0, 2)

    # Write a newline before writing the new row
    # file_csv_write.write("\n")
    
    write_data = csv.DictWriter(file_csv_write, fieldnames=field_names)

    write_data.writeheader() # create header. we should create header

    write_data.writerows(new_data)
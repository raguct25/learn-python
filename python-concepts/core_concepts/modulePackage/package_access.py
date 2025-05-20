from module_package import company, employee # way - 1


# need empty __init__.py file
import module_package # way - 2

import module_package.company as test # use by alias name   way -3

# way - 4
import module_package.company
import module_package.employee


# way - 5 initialized in __init__.py
# if declared from . import * in __init__.py file we can't access getCompanyDetails, getEmplyeeDetails
# from module_package import getCompanyDetails, getEmplyeeDetails , student

from module_package import student



# if not created __init__.py file the import module_package could not work
# error : ImportError: cannot import name 'company' from 'module_package'


# Using from and import
print("company", company.getCompanyDetails())
print("employee", employee.getEmplyeeDetails())


#using import
print("company", module_package.company.getCompanyDetails())
print("employee", module_package.employee.getEmplyeeDetails())


# Using alias name
print("company", test.getCompanyDetails())
print("employee", module_package.employee.getEmplyeeDetails())


#Using import
print("company", module_package.company.getCompanyDetails())
print("employee", module_package.employee.getEmplyeeDetails())


# Using from __init__.py import functions
# print("company", getCompanyDetails())
# print("employee", getEmplyeeDetails())


#Using from init and uninitialized

print("student", student.getStudentDetails())
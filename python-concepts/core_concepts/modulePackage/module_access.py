# def getCompanyDetails():
#     return "*** first  the company details fetch fun called ***"


from modulePackage.module_functions import getCompanyDetails, getEmployeeDetails # way - 1 

import modulePackage.module_functions as module_functions # way -2


# overwrite
# if define function name as same import function - it will overwrite the fucntion - it will run current file  function declared 

# def getCompanyDetails():
#     return "*** first  the company details fetch fun called ***"


company_details_1 = getCompanyDetails()
employee_details_1 = getEmployeeDetails()

# company_details = getCompanyDetails
# employee_details = getEmployeeDetails

# if call without parenthesis () . it return 
# company_details <function getCompanyDetails at 0x7f55983c2e80>
# employee_details <function getEmployeeDetails at 0x7f55983c2f20>


print("company_details - 1", company_details_1)
print("employee_details - 1", employee_details_1)



company_details_2 = module_functions.getCompanyDetails()
employee_details_2= module_functions.getEmployeeDetails()


print("company_details - 2", company_details_2)
print("employee_details - 2", employee_details_2)



# overwrite module functions example

def getCompanyDetails():
    return "*** second the company details fetch fun called ***"


overwrite_function = getCompanyDetails()

print("~~~~ overwrite function calling ~~~", overwrite_function)
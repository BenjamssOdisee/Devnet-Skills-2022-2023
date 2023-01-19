member_dict   =>  {"person_name": "x", "email": "y", "group":"z"}
member_list   =>  [member_dict]

group_dict    =>  {group_name, member_list} | {group_name, [member_dict]}  
group_list    =>  [group_dict]

groups_struc  =>  {group_list} | {[group_dict]}


### Simplified code: converting Excel in to initial Python dict
import xlrd   # library to manage excel spreadsheets
import json   # library to manage JSON classes and functions
wb = xlrd.open_workbook("webex_groups.xlsx")
sheet = wb.sheet_by_index(0)
# FIRST DATA ROW (ROW 0 contains column names)
member_dict["group"] = sheet.cell_value(1, 0) 
member_dict["person_name"]  = sheet.cell_value(1, 1)

member_dict["group"] = sheet.cell_value(2, 0) 
member_dict["person_name"]  = sheet.cell_value(2, 1)
member_dict["email"] = sheet.cell_value(2, 2)
print(member_dict)

### REWRITING RULES TO GENERATE THE DATA STRUCTURE

#Most of the time you will have to manage structures of type dict and list, as a result of the JSON exhange data types

member_dict   =>  {"person_name": "x", "email": "y", "group":"z"}
member_list   =>  [member_dict]

group_dict    =>  {group_name, member_list} | {group_name, [member_dict]}  
group_list    =>  [group_dict]

groups_struc  =>  {group_list} | {[group_dict]}



import csv

# csv reader and writter methods 
with open("user_details.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    print(list(csvreader))

# same as the writter fie 
# can do simple control flow like this 

#iterate it 
# with open("user_details.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     for line in csvreader:
#         print(line)

# here we are using the list - easy to navigate throught the information 
# treat this as a dataframe 
# treating as list of list 
# wanted to anything with this - we cna use any normal list indexing tht we would normally use 
# grab first thing use indexing 
# with open("user_details.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     for line in csvreader:
#         print(line[1])

# use indexing to extract firstname 

# often times need to skip over the line - need built in method - over the line 
# removing the header getting more meanigful information out 
# with open("user_details.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     # skip over the first line 
#     iterable_csv = iter(csvreader)
#     next(iterable_csv)
#     for line in iterable_csv:
#         # print(line)

# # trasnformation-------------------------------------
# # only apppliceable to list passing the old one and new one 
# def transfrom_user_deatails(csv_file_name):
#     new_user_data = []

#     with open(csv_file_name) as csvfile:
#         user_details_csv = csv.reader(csvfile)
#         for user in user_details_csv: # dealing with each row 
#             transformations = [] #each trandomrations added to new_user_data 
#             transformations.append(user[1])
#             transformations.append(user[2])
#             transformations.append(user[-1])
#             new_user_data.append(transformations) # trasnformation file happen in here 
#     return new_user_data

# print(transfrom_user_deatails("user_details.csv"))

# # run another function will use the naem transformation will grab specifi columns 
# # positoin 0 and 1 - need kind of function will put it in this place
# # situation when we know in this place- do it based on the header

# # wrtiing the data back to csv-----------------------
# def create_new_user_data(old_file = "user_details.csv",new_file = "new_user_details.csv"): # old file we have and the new file we about to create 
#     new_user_data = transfrom_user_deatails(old_file)
#     with open(new_file,"w") as newfile:
#         # do this first in order to add the dats in 
#         csv_writer = csv.writer(new_file) # write somthing to it 
#         csv_writer.writerows(new_user_data) # pass that data through

# create_new_user_data() # put nothin in there use this as default
# have thise saved as file 
# old file that is the ismilar nature use the tranform function and will wokr in the same way- this basically it is useable for any type fo file 
# .write row writitng different write rows 
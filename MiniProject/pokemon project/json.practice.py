import json
# # normal dictionary within python 
# course = {"name":"Celine","course":"Data"}
# # print(course["name"])
# # print(type(course))

# # passing throught this dictionary 
# # seralise json object to fomatted strings
# # programme expect a json string 
# # json looks similar to python - won't able to use the key refrence 
# course_json_str = json.dumps(course)
# # print(course_json_str["name"])
# # print(type(course_json_str))
# # looks like a dictionary it is a string 

# # to write to a file
# # with open("new_json_file.json","w") as jsonfile: #writtng the mode, read and write bunch of comobination
# #     json.dump(course, jsonfile) # dump going to create strong object
#     # whatever string objects
#     # things we are dumping and writting to 
# # as soon as it open will close it 

# # load going to load in a file 
# # loads going to take seralise data string - python dictions 
# with open("new_json_file.json") as jsonfile: # don't need to write the mode 
#    course_data = json.load(jsonfile)
# #    print(course_data) # getting the data 
# #    print(type(course_data)) # checking the data 
#    # load in this json format

# print(type(course_json_str))
# course_json = json.loads(course_json_str)
# print(type(course_json))

# when dealing with the loads and dumps changing out of teh json string 
# need to send the information with an API
# have to use dumpst o convert it and use loads to load that information
# using it user friendly 
# easier to deal with dictionary as strings 
# dealing files without pandas - not loading in the dataframe
# does require most basic type- really useful 

#________________________________________________________
import requests

# post_cods_req = requests.get("https://postcodes.io/postcodes/cv340dd")
# print(post_cods_req.status_code) # give the code itself 
# # all this stuff looking at this now 
# # benefical for testing 
# print(post_cods_req.headers)
# print(post_cods_req.content)
# # request can deal with us 
# print(post_cods_req.json())
# # content in form of json 
# # content as the python dictionary 
# # work with this as a python dictionary 
# # grab the request.json use as it is the dictionary 


#--------------------------------------------------
# any post API - data that has been passing through- that is the json body 
# trasnfrom simple dictionary- using json dump 
json_body = json.dumps({"postcodes" : ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
headers = {'Content-Type': 'application/json'} # always be this
post_multi_req = requests.post("https://postcodes.io/postcodes/", headers=headers, data=json_body) # going to the postcode URL
post_req = post_multi_req.json()

print(post_req["result"][0]) # convert into dataframe
# pay attention what you are doing each stage
# dictionary keys values of each stage

# two methods - creating this type of things
# two different ways of ingesting and loading 
# whether it is loaded on the data file 

# worth knowing this basi method and API
# NEEED TO UNDERSTAND OF DUMPS, DICTIONARY, SERALISED STRING, DUMP
# SEND in information with the dictionary 

#load read the file and 
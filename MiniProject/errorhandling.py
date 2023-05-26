# dealing with errors:
# file error, syntax file

# try:
#     file = open("order.txt")
# except:
#     print("There is an Error!")

# going to catch it and will excue whatever we had in the file 
# can capture specific expcetions 
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("There is an Error!")
#     print(errmsg)
# except TypeError:
#     print("There is an error")

# good for using file 
# missing some code 

# try:
#     file = open("order.txt", "r") # types of mode to open
#     lines = file.readlines() # should be able to print the content 
#     for line in lines:
#         print(line.rstrip('\n'))
#     file.close()
# except FileNotFoundError as errmsg:
#     print("There is an Error!")
#     print(errmsg)
# except TypeError:
#     print("There is an error")

# different using with open
# essntially do all of this stuff and don't need to do this anymore

try:
    with open ("order.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.rstrip('\n'))
except FileNotFoundError as errmsg:
    print("There is an Error!")
    print(errmsg)
finally:
    print("Excutions Complete")

def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + '\n')
    except FileNotFoundError as errmsg:
        print("There is an Error!")
        print(errmsg)

write_to_file("order.txt","Burger")
# going to chnage teh file- write mode will change 
# append mode- it will add addtional thing on 
# as writitng each order item and can wrtie the new line character 
# will work any piece fo code we have
# excet deal with any of the error that has happend
# variables when dealing with database
# using the if statament - might be better to handle if statement
# a lot thing we do so far - might be handle with the if statement 



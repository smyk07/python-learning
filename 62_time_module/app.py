import time 

# print(time.ctime(0)) # when my computer thinks time began AKA epoch

# print(time.time()) # seconds since epoch

# print(time.ctime(time.time())) # returns current date and time 

# time_object = time.localtime()
# print(time_object)
# print(time.strftime("%A %B %d %Y %I:%M:%S", time_object))

# time_string = "20 April, 2024"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# time_tuple = (2024, 4, 20, 4, 20, 0, 0, 0, 0)
# print(time.asctime(time_tuple))

# time_tuple = (2024, 4, 20, 4, 20, 0, 0, 0, 0)
# print(time.mktime(time_tuple))
# # Reading File
# file = open("demofile.txt", "r")
# print(file.read())
# file.close()

# file = open("demofile.txt", "r")
# print(file.read(5))
# file.close()

# file = open("demofile.txt", "r")
# print(file.readline())
# file.close()

# file = open("demofile.txt", "r")
# for x in file:
#     print(x, end="**")



# # Writing in a file
# # Using "a" = Append
# file = open("demofile_to_write.txt", "w")
# file.write("'w' removes the old data and then add new data.")
# file.close()

# file = open("demofile_to_write.txt", "a")
# file.write("'a' add the new data after old data.")
# file.close()

# Delete File
import os
print(os.path.exists("fileName.txt"))
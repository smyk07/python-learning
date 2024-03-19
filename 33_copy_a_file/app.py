import shutil 

shutil.copyfile("file.txt", "file_copy.txt") # (src, dst)


# copyfile() => copies contents of a file
# copy() => copyfile() + permission mode + destination can be a directory
# copy2() => copy() + copies metadata
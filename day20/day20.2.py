# Step-1 Open the file
path = r"C:\Users\home\Desktop\files\fileIntro"
f = open(path, 'r')

# Step-2 Read the data from the file
# print(f.read())

# print(f.readline())
# print(f.readline())

print(f.readlines())

# Step-3 Close the File
f.close()
print("Written Completed")
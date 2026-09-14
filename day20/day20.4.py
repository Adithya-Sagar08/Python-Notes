# Step-1 Open the file
path = r"C:\Users\home\Desktop\files\fileIntro"
f = open(path, 'r+')

# Step-2 Write the data to the file
print(f.read())
f.write(" Hello People")
f.seek(0)

# Step-3 Close the File
f.close()
print("Written Completed")
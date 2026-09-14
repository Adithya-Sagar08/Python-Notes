# Step-1 Open the file
path = r"C:\Users\home\Desktop\files\fileIntro"
f = open(path, 'a')

# Step-2 Append data to the file
f.write("\nPFS-064")

# Step-3 Close the File
f.close()
print("Written Completed")
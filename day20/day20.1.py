# Step-1 Open the file
path = r"C:\Users\home\Desktop\files\fileintro1"
f = open(path, 'w')

# Step-2 Write the data to the file
# f.write("Hi This is Adithya Sagar")
# f.write("I am from Hyderabad")
l = ['line1\n', 'line2\n', 'line3\n']
f.writelines(l)

# Step-3 Close the File
f.close()
print("Written Completed")
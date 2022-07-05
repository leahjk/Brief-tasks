# Program to read the entire text file using read() function
file = open("python.txt", "r")
content = file.read()
print(content)
file.close()
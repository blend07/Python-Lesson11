filepath = "C:/Users/Student/Desktop/New folder/Python-Lesson11/CV.txt"

# file = open(filepath, "r")

# content = file.read()

# print(content)

with open(filepath, "r") as file:
    # content = file.read()
    # print(content)

    # line1 = file.readline()
    # print(line1)
    # line1 = file.readlines()
    # print(line1)
    file.seek(20)
    line = file.read()
    print(line)

# with open(filepath, "w") as file:
#     file.write("Hello World")
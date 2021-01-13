import sys

try:
    with open("../results.txt", "r") as file:
        file_content = file.read()
        for i in file_content

except FileNotFoundError:
    print(0)
    sys.exit(2)


print(file_content)




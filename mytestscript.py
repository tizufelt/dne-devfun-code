# file = open("intro-python/parsing-json/pep20.txt", mode="r")

# file_contents = file.read()
# print(file_contents)
# file.close()


with open("intro-python/parsing-json/pep20.txt", mode="r") as file:
     file_firstline = file.readline()
     print(file_firstline)

f = open("names.txt", "r")
strings = f.readlines()
new_strings = [i.strip('\n') for i in strings]
print(new_strings)
f.close()
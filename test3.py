f = open("records.txt", "r")

string = f.read().split("\n")

d = {}
for x in string:
    n = [i for i in x[1:]]
    d[x[0]] = n
    
print(d)
    
import csv

f = open("bamboo.csv", "r")
x = csv.reader(f)
data = list(x)

titles = data.pop(0)
x = []
for records in data:
    x.append(records[titles.index('branch')])
    
branches = set(x)
print(branches)

for branch in branches:
    f = open(f"{branch}.csv", "w", newline='')
    write = csv.writer(f)
    
    for record in data:
        if(record[titles.index('branch')]==branch):
            write.writerow(record)
            
    f.close()


"""f1 = open("aec.csv", "w", newline='')
f2  = open("acet.csv", "w", newline='')
f3 = open("acoe.csv", "w", newline='')"""

"""titles = data.pop(0)

aec = csv.writer(f1)
acet = csv.writer(f2)
acoe = csv.writer(f3)

aec.writerow(titles)
acet.writerow(titles)
acoe.writerow(titles)"""


"""for record in data:
    if(record[3]=="AEC"):
        aec.writerow(record)
    elif(record[3]=="ACET"):
        acet.writerow(record)
    else:
        acoe.writerow(record)
        
f.close()
f1.close()
f2.close()
f3.close()"""
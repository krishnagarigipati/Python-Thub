import csv 

f = open("bamboo.csv", "r")
f1 = open("Codechef.csv", "w", newline='')
x = csv.reader(f)
writer = csv.writer(f1)

data  = list(x)
titles = data.pop(0)

def rating_chooser(rating):
    if rating>=0 and rating<=1399:
        return "1 star"
    elif rating>=1400 and rating<=1599:
        return "2 star"
    
    elif rating>=1600 and rating<=1799:
        return "3 star"
    
    
writer.writerow(['Roll Number', 'CC Stars'])
    
for record in data:
    rating = record[titles.index('cc_rating')]
    nu = int(rating)
    ans = rating_chooser(nu)
    writer.writerow([record[titles.index('roll_number')], ans])
    
f.close()
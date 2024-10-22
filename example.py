import csv

f = open("output.csv", "w", newline='')

x = csv.writer(f)

titles = [["name", "roll_no", "sumbmissions"],
            ["Rama", 122, 100],
            ["Sita", 123, 90],
            ["Lakshman", 124, 95],
            ["Hanuman", 125, 98],
            ["Bharat", 126, 92],
            ["Shatrughan", 127, 88],
            ["Krishna", 128, 99],
            ["Arjun", 129, 96],
            ["Bheem", 130, 94],
            ["Nakul", 131, 91],
            ["Sahadev", 132, 89],
            ["Duryodhan", 133, 85],
            ["Dushasan", 134, 82],
            ["Karna", 135, 97],
            ["Bhishma", 136, 93],
            ["Dronacharya", 137, 87],
            ["Ashwatthama", 138, 84],
            ["Yudhishthir", 139, 86],
            ["Bhima", 140, 83],
            ["Arjun", 141, 81],
            ["Nakul", 142, 80],
            ["Sahadev", 143, 79],
            ["Draupadi", 144, 78],
            ["Subhadra", 145, 77],
            ["Abhimanyu", 146, 76],
            ["Ghatotkach", 147, 75],
            ["Bhagadatta", 148, 74],
            ["Shalya", 149, 73],
            ["Shakuni", 150, 72]]

x.writerows(titles)

f.close()
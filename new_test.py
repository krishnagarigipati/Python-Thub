import csv
import pandas as pd
f = open("bamboo.csv", "r")

x = csv.reader(f)
student_data = list(x)
#print(student_data)

d = {'Male': 0, 'Female': 0}

titles = student_data.pop(0)

for i in student_data:
    if(i[titles.index('gender')]=='Male'):
        d['Male'] += 1
    else:
        d['Female'] += 1
        
print("Male count: ", d['Male'])
print("Female Count: ", d['Female'])

li = []

for i in student_data:
    ans = int(i[titles.index('lc_easy')]) + int(i[titles.index('lc_medium')]) + int(i[titles.index('lc_hard')])
    li.append(ans)
    
max_score = max(li)
idx = li.index(max_score)
print(student_data[idx][titles.index('roll_number')])
print(student_data[idx][titles.index('name')])


aec_hack = 0

for i in student_data:
    if(i[titles.index('college')] == "AEC"):
        if(int(i[titles.index('hr_c')])>=3):
            aec_hack += 1
            
print("The no.of students in AEC Having more than or eq to 3 stars in Hacker Rank: ", aec_hack)

aec_count = 0
acet_count = 0
for i in student_data:
    if(i[titles.index('college')]=="AEC"):
        aec_count += 1
    elif(i[titles.index('college')]=="ACET"):
        acet_count += 1

print("The abs diff between aec and acet is: ", abs(aec_count-acet_count))


college_data = {}

for i in student_data:
    college = i[titles.index('college')]
    branch = i[titles.index('branch')]
    gender = i[titles.index('gender')]
    lc_easy = int(i[titles.index('lc_easy')])
    lc_medium = int(i[titles.index('lc_medium')])
    lc_hard = int(i[titles.index('lc_hard')])
    gfg_school = int(i[titles.index('gfg_school')])
    gfg_basic = int(i[titles.index('gfg_basic')])
    gfg_easy = int(i[titles.index('gfg_easy')])
    gfg_medium = int(i[titles.index('gfg_medium')])
    gfg_hard = int(i[titles.index('gfg_hard')])
    cc_total_problems = int(i[titles.index('cc_total_problems')])

    if college not in college_data:
        college_data[college] = {
            'total_students': 0,
            'total_branches': 0,
            'branches': set(),
            'number_of_male_students': 0,
            'number_of_female_students': 0,
            'total_problems_solved': 0
        }

    college_data[college]['total_students'] += 1
    college_data[college]['branches'].add(branch)
    if gender == 'Male':
        college_data[college]['number_of_male_students'] += 1
    else:
        college_data[college]['number_of_female_students'] += 1
    college_data[college]['total_problems_solved'] += lc_easy + lc_medium + lc_hard + gfg_school + gfg_basic + gfg_easy + gfg_medium + gfg_hard + cc_total_problems

for college in college_data:
    college_data[college]['total_branches'] = len(college_data[college]['branches'])
    college_data[college]['branches'] = list(college_data[college]['branches'])

print(college_data)
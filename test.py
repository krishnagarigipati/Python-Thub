# OPENING THE FILE

f = open("example.txt", "r")

string = f.read()
nums = list(map(int, string.split()))
print(sum(nums))
f.close()
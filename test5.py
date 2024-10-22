def is_prime(n):
    
    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
        
    return True

fn = open("range.txt", "r")

s = fn.read().split()

a = int(s[0])
b = int(s[1])

print(a,b)
f = open("prime.txt", "w")
for i in range(a,b):
    if(is_prime(i)==True):
        f.write(str(i) + "\n")
        
fn.close()
f.close()
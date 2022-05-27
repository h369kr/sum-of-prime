num = int(input("Enter number: "))
bet = []
for i in range(2,num-1):
    bet.append(i)
print(f"Number to be checked for prime {bet}")    

def isPrime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True          

pl = []
for i in bet:
    if isPrime(i):
        pl.append(i)

print(f"Prime number before {num} are {pl}")       

for i in pl:
    for j in range(2,len(pl)):
        if i+pl[j] == num:
            print(f"The number {num} can be expanded as the sum of primes are {i} and {pl[j]}")
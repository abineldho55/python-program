m=int(input("Enter number:"))
n=int(input("Enter number:"))
gcd=1
for i in range(1,m+1):
  if n % i==0 and m % i==0:
    gcd=i
print(gcd)
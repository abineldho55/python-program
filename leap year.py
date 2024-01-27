a=int(input("Enter the starting leap year"))
b=int(input("Enter the last year"))

for i in range(a,b):
    if(i%4==0  and i%100!=0):
      print(i,"is a leap year")
    else:
      print(i,"is not a leap year")
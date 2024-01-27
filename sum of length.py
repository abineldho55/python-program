a=[1,2,3,4,5,7]
b=[5,15,2,7]
s=int(0)
c=int(0)
if len(a)==len(b):
 print("length are equal")
else:
  print("different length")
  for i in range(0,len(a)):
   s=s+a[i]
  for i in range(0,len(b)):
   c=c+b[i]
  if (s==c):
    print("sum are equal")
  else:
   print("sum is different")

   for i in range(0,len(a)):
    s=s=a[i]
    print(s)
    for i in range(0,len(b)):
      c=c=b[i]
      print(c)
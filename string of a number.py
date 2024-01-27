test_str=str(input("Enter string"))
freq={}
for i in test_str:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
print("Count of all characters:"+str(freq))
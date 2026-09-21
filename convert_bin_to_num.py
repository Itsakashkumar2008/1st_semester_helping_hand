len=int(input("total len of your binary: "))
total=0
bin=[]
print(" ")
print("put binary from right to left example like 11001 enter first len is 5 then 1st enter 1 then 0 then 0 then 1 then 1 ...")
print(" ")
a=" "
for i in range(0,len):
  binary=int(input("enter digit of index number "+str(-(i+1))+" of your binary : "))
  bin=bin+[binary]
  if(binary==1):
    total+=2**i
  elif(binary==0):
    continue
  else:
    print("invalid input")
    a="invalid"
    break
if(a=="invalid"):
  print("please try again since binary contain only 1 and 0 and you enter wrong input... ")
else:
  print("your binary is",bin[::-1])
  print("your output of binary in number is \n",total)

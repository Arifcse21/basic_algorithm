n=int(input("Enter a number: "))
flag = 1
for i in range(2,int(n/2),1):
    if(n%i == 0):
        flag = 0
        break
if(flag == 0):
    print("Your Entered number is NOT PRIME")
else:
    print("Your Entered number is PRIME")














t1,t2=(0,1)
print(t1)
print(t2)

for i in range(t2,1001):
    tm=t2
    t2=t2+t1
    t1=tm
    print(t2)


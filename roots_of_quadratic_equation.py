import math as m
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
D=m.pow(b,2)-4*a*c

if (D>=0):
    r1=(-b+m.sqrt(D))/(2*a)
    r2=(-b-m.sqrt(D))/(2*a)
    print("Roots of the eqation are  "+str(r1)+" and  "+str(r2))
else:
    rp=round(b/(2*a),2)
    #print(rp)
    ip=round(m.sqrt(-D)/(2*a),2)
    #print(ip)
    print("Roots of the equation are "+str(-rp)+"+j("+str(ip)+") and  "+str(-rp)+"-j("+str(ip)+")")






'''
write a python script  to check whether a given quadratic equation has two real & distinct roots,real & quadratic roots or  immaginary roots

'''
a=float(input("enter  the value of a"))
b=float(input("enter the value of b"))
c=float(input("enter the value of c"))
d=b**2-(4*a*c)
if(d>0):
    print("real & distinct roots")
elif(d==0):
    print("real or equal root")
else:
    print("imaginary root")

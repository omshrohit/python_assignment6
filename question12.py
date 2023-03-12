# write a python script to accept one complex number from  the user and display the greater number between real part and imaginary part
number=complex(input("enter the  complex number"))
real=number.real
imag=number.imag
if real>imag:
    print("real part is greater")
else:
    print("imaginary part is greater")
# write a python script to print greater between  two numbers.print number only once even the numbers are the same
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num1==num2:
    print(num1,"\nboth are same")
else:
    if(num1>num2):
        print(f"{num1} is greater then {num2}")
    else:
        print(f"{num2} is greater then {num1}")
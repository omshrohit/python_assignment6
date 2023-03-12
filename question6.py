# write a python script  to check whether a given number is three digit or  not
num=int(input("enter the number"))
if num>=100 and num<=999:
    print(f"given number {num} is three digit number")
else:
    print(f"given number {num} is not three digit number")
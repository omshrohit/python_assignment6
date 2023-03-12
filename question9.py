# write a python script to  check  whether a given year is   leap year or not
year=int(input("enter the year"))

if year%400==0 or (year%4==0 and  year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
# write  a pyhon script  to take the month value in numeric format and display the number of days in  it.
month=int(input("enter  the month name in the form  of numeric"))
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month in [4,6,9,11]:
    print("30 days")
else:
    year=int(input("enter the year"))
    if year%400==0 or (year%4==0 and year%100!=0):
        print("29 day")
    else:
        print("28 days")
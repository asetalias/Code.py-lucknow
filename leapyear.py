year = int(input("Enter the year? "))
if year%4==0:
    if year%100==0:
        if year%400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap year")
    else:
        print("leap year")

else:
    print("not a leap yaer")
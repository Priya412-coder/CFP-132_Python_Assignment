def find(year):
    if year > 999 & year <= 9999:
        if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
            print("Year is leap year");
        else:
            print("Year is not leap year");
    else:
        print("Enter valid year");


year = int(input("Enter the year you want to check :\n"))
print(find(year))

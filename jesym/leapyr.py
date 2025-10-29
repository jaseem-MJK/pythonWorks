
final_year = int(input("Enter the final year: "))
print(f"\nleap years from 2025 to (final_year):")


#loop through each year in the range
for year in range(2025,final_year + 1):
    #check leap year condition
    if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print(year)


print("\nprogram finished!")

#program to display future leap years from current year  to user-entered final year

        

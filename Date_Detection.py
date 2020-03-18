#!python 3
#Date Detection
import re

def validate_date(date):
    dateformat=re.compile(r"(\d{2})/([0-1]\d)/(\d{4})")#Create regex
        
    day=int(dateformat.search(date).group(1))   #Set variables 
    month=int(dateformat.search(date).group(2))
    year=int(dateformat.search(date).group(3))
    #Check if the year is vaild
    if day>31:
        return False
    if month>12:
        return False
    if year>2999:
        return False
    if month==4 and day>30:
        return False 
    if month==6 and day>30:
        return False
    if month==9and day>30:
        return False 
    if month==11 and day>30:
        return False           
    #check if february is in a leap year
    if month == 2:
         if day > 28 and year % 4 != 0:  # the year is not leap year
             return False
         elif day > 28 and year % 4 == 0 and year % 100 == 0:
             return False
         elif day > 29 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
             return False
         elif day > 29 and year % 4 == 0:  # it is leap year
              return False
    return True
        


print(validate_date('30/06/2061'))  # True
print(validate_date('31/11/2019'))  # false, no 31st of november

print(validate_date('29/02/2004'))  # True, february can have 29 days in leap years
print(validate_date('29/02/2100'))  # False, february can't have more than 28 days in leap years divisible by 100
print(validate_date('29/02/2000'))  # True, february can have 29 days in leap years divisible by 100 and 400
    

    
    



    


        
        
        
    
    

                      
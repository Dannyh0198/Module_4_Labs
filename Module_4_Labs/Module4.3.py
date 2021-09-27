# 4.3.1.6 
# Your task is to write and test a function which takes one argument (a year) 
# and returns True if the year is a leap year, or False otherwise. 

def is_year_leap(year): # create a function called is leap year with the parameter called (year)
    if ((year) % 2 == 0): # Set the conditions for the function
        return True

# Remainder of the code provided by Cisco
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    year = test_data[i]
    print(year,"->",end="")
    result = is_year_leap(year)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# 4.3.1.7 Don't understand the logic.
def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


# 4.3.1.8 Don't understand the logic.
def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):
	days = 0
	for m in range(1, month):
		md = days_in_month(year, m)
		if md == None:
			return None
		days += md
	md = days_in_month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_of_year(2000, 12, 31))



# 4.3.1.9 LAB: Prime numbers - how to find them
# Will require taking through this one.
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# 4.3.1.10 LAB: Converting fuel consumption
def liters_100km_to_miles_gallon(litres): # Create function to convert the ammount of fuel needed for 100km into miles per gallon.
    liters = (100000 / 1609.344) / liters * 3.785411784 # Take the ammount of litres and convert into gallons by * 3.7. Then convert 100000 into miles by / 1609m. Divide that number by that gallons to make the MPG figure.
    return liters # Returns the calculated value of the litres into MPG.

def miles_gallon_to_liters_100km(miles): # Create function to convert the MPG figure into the litres required to cover 100km.
    miles = (miles * 1609.344) * 100000 / 3.785411784 # Take the MPG number and convert into metres by * by 1609. Muliply by 100000 to make gallons per 100km. Then take that number and divide by 3.7 to make litres per 100km.
    return miles

# Sample code.
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

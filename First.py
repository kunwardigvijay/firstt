"""print (" Hello World")
print('Hellow world')
print("hello 'Kd' World")
print("Hello \t \"KD\" \n world")

print("user_name" + 3)
print("user_name" + "3")
name = input ("Type your name ")
print ("your "+ name)

number_one = int ( input ("Enter First Number"))
number_Second = int (input ("Enter second Number"))
Total = number_one + number_Second
print (Total)

name = "Digvijay"
age = 25
print ("Hello My name is {} and my age is {}".format (name , age));

num1 = input ("Enter First Number")
num2 = input ("Enter Second Number")
num3 = input ("Enter third number")

print(f"average of three number :{(int(num1) + int (num2) + int (num3)) / 3}")

language = " Python"
print (language[4])
print (language[2: 4])
print (language [ : ])

name = input (" Enter your name and I wil convert your name in reverse order ")
print (name [ -1::-1])

name = "Digvijay"
print (len(name))
print(name.upper())
print(name.title())
print(name.format())
print(name.split())

world = "amazing"
print(world[1:6:2])
print(world[-7:-3:3])
print(world[ : :-2])
print(world[ : :-1])

demo = " Aakash is a good boy"
print (demo.replace("boy", "Girl"))

list =[1, 2, 3, 4, 5, 6, 8, 12]
print(list.append(7))
print(list)
list.insert(1, 1)
print(list)

a =10
b =15
b = a
a = b
print(a,b)"""

# Problem solving 1
"""age = int(input("Give the age number = "))
if age < 13:
    print("child")
elif age < 19:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior citizen")          
"""
# Problem solving 2
"""age = int(input("Enter the age = "))
day = "wednesday"

price = 12 if age >=18 else 8
if day == "wednesday":
    price -=2
print("Ticket price for you is $ ", price)

# Problem solving 3
score = int(input("Enter your grade = "))
if score >= 101:
    exit()
elif score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
else:
    grade = "F"
print(grade)

# Problem solution 4
colour = str(input("Enter colour name = "))
# name = str(input("Enter fruit name = "))
if colour == "Green":
    x= "unripe"
elif colour == "Yellow":
    x = "etable"
elif colour == "Brown":
    x = "non etable"
else:
    x = "enter again"
print(x)            

# Problem solving 5 
weather = str(input("Enter colour name = "))
# name = str(input("Enter fruit name = "))
if weather == "Sunny":
    x = "Go for walk"
elif weather == "Rainy":
    x = "Read a Book"
elif weather == "Snowy":
    x = "Built a snowman"
print(x)

# Problem solving 6
distance = 5
if distance <= 3:
     mode = " walk"
elif distance <= 15:
    mode = " Bike "
else:
    mode = "Car"
print(mode)     

# Problem solving 7 
order_size = "medium"
extra_shot = True
if extra_shot:
    coffee = order_size + "Coffee with extra shot"
else:
    coffee = order_size + "coffee"    
print(coffee)

# Problem solution 8
password = "password"
password_length = len(password)
if password_length < 6:
    strength = "weak"
elif password_length < 8 :
    strength = "medium"
else:
    strength = "strong"
print (strength)        

# problem solution 9
year = 2025
if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print (year,"is leap year")
else:
    print(year," is not leap year")    


# problem loop 1
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num  > 0:
        positive_number_count = positive_number_count + 1
print("Final count of positive number : ", positive_number_count)        


# problem loop 2
n = 10000
sum_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
print("sum of even number is " , sum_even)

# problem loop 3

number = int(input())

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

# problem loop 4

input_string = "Python"
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(reversed_string)    

# problem loop 5

input_string = "teeteraabbs"
for chr in input_string:
    print(chr)
    if input_string.count(chr) == 1:
        print("result",chr)
        break
# problem loop 6

number = 5
factorial = 1        
while number > 0:
    factorial = factorial * number
    number = number - 1
print("factorial"factorial)
 
 # problem loop 7   
while True:
    number = int(input("Enter the number = "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("error")]
        
       
# problem loop 8
number = int(input())
is_prime = True
if number > 1:
    for i in range (2, number):
        if(number % i) ==0:
            is_prime = False
            break
print(is_prime)         
  """       
# problem loop 9

# items = ["apple", "banana", "orange", "banana", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print(item)
#         break
#     unique_item.add(item)
# print(unique_item)    
    
# problem loop 10

# import time
# wait_time = 1
# max_retries = 9
# attempts = 0
# while attempts < max_retries:
#     print("attempt ",attempts + 1, "- waittime ",wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1

# Basic Function Syntex    
 
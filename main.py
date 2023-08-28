my_name = input("how old are you?")
my_age = int(input("what is your name?"))
print(f"my name is {my_name} and i am {my_age} years old")

first_number = int(input("what is your first number?"))
secound_number = int(input("what is your secound number?"))

opperation = input ("what is your opperation")
if opperation == "+":
    print (first_number+secound_number)
elif opperation == "*":
    print (first_number*secound_number)
elif opperation == "-":
    print (first_number-secound_number)
elif opperation =="/":
    print (first_number/secound_number)
else:
    print('operation not valid')

bus_capcity=(11)
people_inbus= int(input("enter the number of people who wants to ride the bus"))
waiting= int(input("how many people are waiting?"))


empty_seats= bus_capcity - people_inbus

if empty_seats <= waiting :
   print (f'there are empty_seats {empty_seats}')
else:
    print("opps the bus is full")

  



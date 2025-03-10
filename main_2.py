#1
#a = len(input("What's your name? "))
#print(a)

#2
#a = float(input("Type the first number: "))
#b = float(input("Type the second number: "))
#print(a+b)

# Challenge

employee = str(input("What's your name? "))
salary = float(input("What's your monthly salary? "))
bonus_percent = float(input("What's your bonus percentage? "))

final_bonus = 1000 + salary * bonus_percent/100

print(f"Hey, {employee}! Acording to your bonus, this is you bonus for the month: {final_bonus}")
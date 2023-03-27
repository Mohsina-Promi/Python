# num = len(input("what's ur name?"))
# new_num = str(num)
# print("ur name has " + new_num + " characters" )

a =  123
print(type(a))
print(70 + float("100.6"))
print(str(70) + str("100.6"))

# #exercise
two_digit_number = input("Type a two digit number: ")
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

two_digit_number = num1 + num2
print(two_digit_number)

# #exercise2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

print(round(8 // 3))

#f-String
score = 1
height = 1.8 

print(f"your score is {score}, your height is {height}")

#exercise3

age = input("What is your current age?")

age_int = int(age)

years = 90-age_int
months = years*12
weeks = years*52
days = years*365

message = f"You have {days} days, {months} months, {weeks} weeks remainining"
print(message)

#tip_calculator
print("welcome to the tip calculator!")
t_bill = float(input("what was the total bill? $"))
tip = int(input("% tip you like to give?"))
split = int(input("how many to split the bill?"))
bill_with_tip = tip / 100 * t_bill + t_bill
print(f"Bill with tip ${bill_with_tip}")
bill_per_person = bill_with_tip / split
final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_bill}")






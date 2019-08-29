#Exercise 1: Hello!
"""name = input('What is your name?')
print(f'Hello, {name}')

#Exercise 2: HELLO!
name = input('WHAT IS YOUR NAME?')
number_of_letters = len(name)
print(f'O HAI THERE, {name}!\n YOUR NAME HAS {number_of_letters} LETTERS IN IT!')

#Exercise 3: Madlib
name = input('What is your name?')
fav_subject = input('What is your favorite subject in school?')
print(f"{name}\'s favorite subject in school is {fav_subject}")

#Exercise 4: Day of the Week
day = int(input('Day of the Week (0-6)?'))
name_of_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
entered_day = name_of_day[day]
print(f'It\'s {entered_day}!')


#Exercise 5: Work or Sleep In?
day = int(input('Day of the Week (0-6)?'))
if day == 0:
    print('Sleep in.')
elif day == 6:
    print('Sleep in!')
else:
    print('Go to work!')


#Exercise 6: Celsius to Fahrenheit
celsius = int(input('Temperature in C?'))
fahrenheit = celsius *1.8 + 32
print(fahrenheit)
elif level_of_service == 'Fair':
    print(f'Tip Amount is {bill_amount * .15}')


#Exercise 7: Tip Calculator
bill_amount = int(input('Total Bill Amount?'))
level_of_service = input('How was your service? (Good, Fair, Bad)')
if level_of_service == 'Good':
    print(f'Tip Amount is {bill_amount * .20} \n Total Amount is {bill_amount + bill_amount *.20} ')
elif level_of_service == 'Fair':
    print(f'Tip Amount is {bill_amount * .15} \n Total Amount is {bill_amount + bill_amount *.15} ')
elif level_of_service == 'Bad':
    print(f'Tip Amount is {bill_amount * .10} \n Total Amount is {bill_amount + bill_amount *.10} ')

#Exercise 8: Tip Calculator Part 2: Electric Boogaloo
bill_amount = int(input('Total Bill Amount?'))
level_of_service = input('How was your service? (Good, Fair, Bad)')
split_amount = int(input('Split between how many people?'))
if level_of_service == 'Good':
    print(f'Tip Amount is {bill_amount * .20} \n Total Amount is {bill_amount + bill_amount *.20} \n Amount per person is {(bill_amount + bill_amount *.20) / split_amount } ')
elif level_of_service == 'Fair':
    print(f'Tip Amount is {bill_amount * .15} \n Total Amount is {bill_amount + bill_amount *.15} \n Amount per person is {(bill_amount + bill_amount *.15) / split_amount } ')
elif level_of_service == 'Bad':
    print(f'Tip Amount is {bill_amount * .10} \n Total Amount is {bill_amount + bill_amount *.10} \n Amount per person is {(bill_amount + bill_amount *.10) / split_amount } ')
"""

#Exercise 9: 1 to 10
iteration = 0
while iteration > 11:
    print(f'Number {iteration}')
    iteration +=1
    
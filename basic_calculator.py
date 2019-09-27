name = input('What is your name?')
print('Hello', name, 'would you like to try my calculator?')
answer = input('Yes or No :')

if answer == 'Yes':
    print("OK, let's go!")
elif answer == 'yes':
    print("OK, let's go!")
else:
    print("Fine!")

num_1, operator, num_2 = input('Enter calculation :').split()
num_1 = int(num_1)
num_2 = int(num_2)


if operator == '+':
    print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
elif operator == '-':
    print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
elif operator == '*':
    print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
elif operator == '/':
    print("{} / {} = {}".format(num_1,num_2, num_1 / num_2))
else:
    print("invalid operation")
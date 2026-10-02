# operators 


# a =10
# b = 20

# print(a+b)

# print(a>b)


# comparison operators 

# age = 20

# print(age>18)

# print(age == 18)

# print(age !=18)


# age = 18

# if age >= 18:
#     print('You are eligible to vote')
# else:
#     print('You are not eligible to vote')


# for i in range(1,11):
#     print(i)



# practicle 1

# number = int(input('Enter a number :'))

# if number % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')




# practicle 2

# number = int(input('Enter a number :'))

# if number > 0:
#     print('The number is positive')
# elif number < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')


# practicle 3

name = "Yaseen"
password = "1234"

name1 = input('Enter your name :')
password1 = input('Enter your password :')


if name1 == name and password1 == password:
    print('Login successful')
elif name1 != name and password1 == password:
    print('Invalid name')    
elif name1 == name and password1 != password:
    print('Invalid password')
else:
    print('Invalid name and password')        
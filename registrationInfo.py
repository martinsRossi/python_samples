import random

print ("Hello there! It's a pleasure to have you as our client. \n\nFor the conclusion of your registration, please enter the following information:");

first_name = input ("First name: ")
last_name = input ("Last name: ")
email = input ("Email address: ")
phone_number = input ("Phone number: ")
job_title = input ("Job Title: ")
id_number = input ("ID Number: ")

print ()
print ("The ID card is: ")
print ("-"*80)
print (f'{last_name.upper()}, {first_name}')
print (job_title.title())
print (f'ID: {id_number}')
print ()
print (email.lower())
print (f'({phone_number[0:3]})  {phone_number[3:6]}-{phone_number[6:10]}')
print ()

hair=["Brown", "Blonde", "Brunette", "Grey", "Ginger", "Fair"]
eyes=["Blue", "Black", "Brown", "Hazel", "Amber", "Green", "Gray"]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
training=["Yes", "No"]

print(('Hair: ' + random.choice(hair) + '\t' + 'Eyes: ' + random.choice(eyes)).expandtabs(30))
print(('Month: ' + random.choice(months) + '\t' + 'Training: ' + random.choice(training)).expandtabs(30))
print ("-"*80)

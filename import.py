from time import sleep
from turtle import color
import colorama
from colorama import Fore, Back, Style

print ('Hi there! \n')
y = input("Please tell us, what is your name? My name is: ")
print('\n')

sleep(0.5)

print (y + ', this is the colors that you may pick as your ' + "\033[1m" + 'font line' + "\033[1m" + ':')

print(Fore.BLACK + 'Black')
sleep(0.5)
print(Fore.WHITE + 'White')
sleep(0.5)
print(Fore.RED + 'Red')
sleep(0.5)
print(Fore.GREEN + 'Green')
sleep(0.5)
print(Fore.YELLOW + 'Yellow')
sleep(0.5)
print(Fore.BLUE + 'Blue')
sleep(0.5)
print(Fore.MAGENTA + 'Magenta')
sleep(0.5)
print(Fore.CYAN + 'Cyan')
sleep(0.5)

print (Fore.RESET)

print (y + ', between those colors, what is your favorite color? (this is going to be your font color)')
sleep(2)

usersColor = input('My favorite color is: ')

color = usersColor.upper()

print('\n')

print('So, your favorite color is: ' + getattr(Fore,color) + color + '.')

print (getattr(Fore,color) + 'Thats good to know... Now tell check it out the background colors:')

print (getattr(Fore,color) + Back.BLACK + 'Black')
sleep(0.5)
print (getattr(Fore,color) + Back.WHITE + 'White')
sleep(0.5)
print (getattr(Fore,color) + Back.RED + 'Red')
sleep(0.5)
print (getattr(Fore,color) + Back.GREEN + 'Green')
sleep(0.5)
print (getattr(Fore,color) + Back.YELLOW + 'Yellow')
sleep(0.5)
print (getattr(Fore,color) + Back.BLUE + 'Blue')
sleep(0.5)
print (getattr(Fore,color) + Back.MAGENTA + 'Magenta')
sleep(0.5)
print (getattr(Fore,color) + Back.CYAN + 'Cyan')
sleep(0.5)

print (Back.RESET)

print ('Which one combine the best?')

secondUsersColor = input ('The color that combined the best was: ')
secondColor = secondUsersColor.upper()

print (getattr(Fore,color) + getattr(Back,secondColor) + "That's nice! Look how awesome your text font looks like!")
answer = input (getattr(Fore,color) + getattr(Back,secondColor) + "Did you like it? Type any comment as you wish. ")

print (getattr(Fore,color) + getattr(Back,secondColor) + y + ", your response was: " + answer + "\n We've submitted that for our support crew! Thank you for your time")

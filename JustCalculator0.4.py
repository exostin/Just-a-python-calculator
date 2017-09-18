#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"
# or do first step and then "phyton pycalc.py"
import webbrowser

print('Welcome to JustCalculator0.4! :D')

while True:
    def add(opt1, opt2):
        return opt1 + opt2

    def subtract(opt1, opt2):
        return opt1 - opt2

    def multiply(opt1, opt2):
        return opt1 * opt2

    def divide(opt1, opt2):
        return opt1 / opt2

    def modulo(opt1, opt2):
        return opt1 % opt2

    def power(opt1, opt2):
        return opt1 ** opt2

    op_dict = {'+': add,
               '-': subtract,
               '*': multiply,
               '/': divide,
               '%': modulo,
               '^': power}

    print('Add (+)')
    print('Subtract (-)')
    print('Multiply (*)')
    print('Divide (/)')
    print('Modulo (%)')
    print('Power (^)')
    print('GitHub Respository (Git)')
    choice = input("Your choice: ")

    if choice in op_dict:
        opt1 = float(input("First number: "))
        opt2 = float(input("Second number: "))

        try:
            print('{} {} {} = {}'.format(opt1, choice,
                                         opt2, op_dict[choice](opt1, opt2)))
        except ZeroDivisionError:
            print("Can't divide by zero!")

    elif choice == "Git":
        webbrowser.open("https://github.com/exostin/Just-a-python-calculator")
    else:
        print('Wrong input!')

    exit = input('Do you want to do next calculation? [y/n] ').lower()
    if exit == 'y' or 'yes' or 'yeah':
        continue
    else:
        break

#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"

print('Welcome to Just-a-calculator 0.01 :D')


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


print('Add (+)')
print('Subtract (-)')
print('Mulitply (*)')
print('Divide (/)')
print('Modulo (%)')
print('Power (^)')
choice = input("Your choice: ")


opt1 = float(input("First number: "))
opt2 = float(input("Second number: "))

if choice == "+":
    print(opt1, "+", opt2, "=", add(opt1, opt2))


elif choice == "-":
    print(opt1, "-", opt2, "=", subtract(opt1, opt2))


elif choice == "*":
    print(opt1, "x", opt2, "=", multiply(opt1, opt2))


elif choice == "/":
    print(opt1, ":", opt2, "=", divide(opt1, opt2))


elif choice == "%":
    print(opt1, "%", opt2, "=", modulo(opt1, opt2))


elif choice == "^":
    print(opt1, "^", opt2, "=", power(opt1, opt2))
else:
    print('  Wrong input!  ')

#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"
# or do first step and then "phyton pycalc.py"
import webbrowser

print('Welcome to PyCalc 0.1v2 :D')

print('Add (+)')
print('Subtract (-)')
print('Multiply (*)')
print('Divide (/)')
print('Modulo (%)')
print('Power (^)')
print('GitHub Respository (Git)')
choice = input("Your choice: ")

if choice == "+":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, "+", opt2, "=", opt1 + opt2)
elif choice == "-":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, "-", opt2, "=", opt1 - opt2)
elif choice == "*":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, "x", opt2, "=", opt1 * opt2)
elif choice == "/":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, ":", opt2, "=", opt1 / opt2)
elif choice == "%":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, "%", opt2, "=", opt1 % opt2)
elif choice == "^":
    opt1 = float(input("First number: "))
    opt2 = float(input("Second number: "))
    print(opt1, "^", opt2, "=", opt1 ** opt2)
elif choice == "Git":
    webbrowser.open("https://github.com/exostin/Just-a-python-calculator")
else:
    print('  Wrong input!  ')

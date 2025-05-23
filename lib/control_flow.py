#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    if  temperature < 40:
        response = "brisk"
    elif (40 < temperature < 65):
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"

def fizzbuzz(num):
    if (num %3 == 0) and (num %5 == 0):
        response = "FizzBuzz"
    elif num %3 == 0:
        response = "Fizz"
    elif num %5 == 0:
        response = "Buzz"
    else:
        response = num
    return response
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        print("Invalid operation!")
        return None
    

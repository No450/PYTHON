"""
1. Accepts a function as an argument or returns a function (in python, functions are also trated as objects)
"""

def loud (text): #maiusculo  
    return text.upper()
    
def quiet (text):# minusculo 
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(quiet)

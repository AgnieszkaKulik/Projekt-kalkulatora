import math

expression = ""

def press(character, flag):
    global expression

    if flag and character.isnumeric() or expression == "ERROR":
        expression = str(character)

    elif len(expression) == 0 and not character.isnumeric():
        if str(character) is '-':
            expression = '-'

    elif len(expression) > 0 and str(character) in ['+', '-', '/', '*', '.']:
        if expression[-1] in  ['+', '-', '/', '*']:
            expression = expression[:-1] + str(character)
        else:
            expression += str(character)

    else:
        expression += str(character)

    return expression, 0

def power2_fun():
    global expression

    value = str(eval(expression)**2)
    return expression

def sqrt_fun():
    global expression

    try:
        expression = str(math.sqrt(eval(expression)))
        return expression

    except:
        return "ERROR"

def equal_fun():
    global expression

    try:
        expression = str(eval(expression))
        return expression

    except:
        expression = ""
        return "ERROR"
        
def comma():
    global expression

    if expression == "":
        expression = "0."

    else:
        i = len(expression) - 1
        while i >= 0:
            if expression[i] == '.':
                return expression
            if expression[i] in ['+', '-', '/', '*']:
                if i == len(expression) -1:
                    expression += '0'
                break
            i -= 1
        expression += '.'
    return expression

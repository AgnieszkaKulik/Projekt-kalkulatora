import cmath, re

expression = ""
operators = ['+', '-', '/', '*'] #,'(',')'


# obsługa po naciśnięciu przycisku
def press(character, flag=0):
    global expression, operators

    # sprawdza czy naciśnięty znak po równa się jest cyfrą (tworzy nowe równanie), sprawdza czy jest liczba lub czy jest to błąd
    if flag and character.isnumeric() or expression  == "ERROR":
        expression = str(character)
    # sprawdza czy pierwszy znak to minus lub początek nawiasu
    elif len(expression) == 0 and not character.isnumeric():
        if str(character) in ['-', '(', 'j']:
            expression = str(character)
    # sprawdza czy poprzedni znak to operator jeśli tak to zamienia go
    elif len(expression) > 0:      #i== '+' or '-'or '/' or '*':
        if str(character) in operators and expression[-1] in operators:  #['+', '-', '/', '*']:
            expression = expression[:-1] + str(character)
            #niepozwala po znaku j wpisać ciąg dalczy liczby zespolonej
        elif not(expression[-1] == 'j' and character.isnumeric()):
            expression += str(character)
            
    else:
        expression += str(character)

    return expression, 0

# podnoszenie wpisanego równania do kwadratu
def power2_fun():
    global expression
    try:
        value = str(eval(expression) ** 2)
        return value
    except:
        expression = ""
        return "ERROR"


# pierwiastek kwadratowy

def sqrt_fun():
    global expression

    try:
        expression = str(cmath.sqrt(eval(expression)))
        return expression

    except:
        expression = ""
        return "ERROR"
    
#wylicza równianie, gdy wykreyje błąd zwraca error
def equal_fun():
    global expression

    try:
        expression = str(eval(expression))
        return expression
    except:
        expression = ""
        return "ERROR"

# sprawdza czy jest w ciągu znaków przecinek jeśli jest to nie pozwala na kolejne wstawienie
def comma():
    global expression
    
    pattern = r'(\+|\-|\*|\/|\(|\))'
    numbers = re.split(pattern, expression)  

    if numbers == [] or numbers[-1] == '':
        expression += "0."
    elif '.' not in numbers[-1]:
        expression += '.'
    return expression

def reset_fun():
    global expression
    expression = ""
    return expression

def imaginary_part(flag):
    global expression
    if expression == "" or flag:
        expression = "1j"
    if expression[-1] == '.':
        return expression, 0

    i = len(expression) - 1
    while i >= 0:
        if expression[i] == 'j':
            return expression, 0
        if expression[i] in operators:
            if i == len(expression) - 1:
                expression += '1'
            break
        i -= 1
    expression += 'j'
    return expression, 0

def change_char():
    global expression, operators

    if not expression:
        expression = '-'
        return expression

    i = len(expression) - 1
    while i > 0 and expression[i] not in operators:
        i -= 1

    if i == 0 and expression[0] == '-':
        expression = expression[1:]
    elif i == 0:
        expression = '-' + expression
    else:
        if expression[i] == '-':
            expression = expression[:i] + '+' + expression[i+1:]
        elif expression[i] == '+':
            expression = expression[:i] + '-' + expression[i+1:]
        else:
            expression = expression[:i+1] + '-' + expression[i+1:]

    return expression
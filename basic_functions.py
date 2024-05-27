import math
import cmath

expression = ""
operators = ['+', '-', '/', '*'] #,'(',')'


# obsługa po naciśnięciu przycisku
def press(character, flag):
    global expression

    # sprawdza czy naciśnięty znak po równa się jest cyfrą (tworzy nowe równanie), sprawdza czy jest liczba lub czy jest to błąd
    if flag and character.isnumeric() or expression == "ERROR":
        expression = str(character)
    # sprawdza czy pierwszy znak to minus
    elif len(expression) == 0 and not character.isnumeric():
        if str(character) == '-':
            expression = '-'
    # sprawdza czy poprzedni znak to operator jeśli tak to zamienia go
    elif len(expression) > 0 and str(character) in operators:      #i== '+' or '-'or '/' or '*':
        if expression[-1] in operators:  #['+', '-', '/', '*']:
            expression = expression[:-1] + str(character)
        else:
            expression += str(character)

    else:
        expression += str(character)

    return expression, 0


# podnoszenie wpisanego równania do kwadratu
def power2_fun():
    global expression

    value = str(eval(expression) ** 2)
    return value


# pierwiastek kwadratowy
def sqrt_fun():
    global expression

    try:
        expression = str(cmath.sqrt(eval(expression)))
        return expression

    except:
        expression = ""
        return "ERROR"


# wylicza równianie, gdy wykreyje błąd zwraca error
def equal_fun():
    global expression

    try:
        expression = str(eval(expression))
        return expression

    # except:
    #     expression

    except:
        expression = ""
        return "ERROR"


# sprawdza czy jest w ciągu znaków przecinek jeśli jest to nie pozwala na kolejne wstawienie
def comma():
    global expression

    if expression == "":
        expression = "0."

    else:
        i = len(expression) - 1
        while i >= 0:
            if expression[i] == '.':
                return expression
            if expression[i] in operators:
                if i == len(expression) - 1:
                    expression += '0'
                break
            i -= 1
        expression += '.'
    return expression


# import math
# import cmath
#
# expression = ""
# operators = ['+', '-', '/', '*']
# #obsługa po naciśnięciu przycisku
# def press(character, flag):
#      global expression
#
#
#     if character:
# #sprawdza czy naciśnięty znak po równa się jest cyfrą (tworzy nowe równanie), sprawdza czy jest liczba lub czy jest to błąd
#     if flag and character.isnumeric() or expression == "ERROR":
#         expression = str(character)
#     #sprawdza czy pierwszy znak to minus
#     elif len(expression) == 0 and not character.isnumeric():
#         if str(character) == '-':
#             expression = '-'
#     #sprawdza czy poprzedni znak to operator jeśli tak to zamienia go
#     elif len(expression) > 0 and str(character) in operators:
#         if expression[-1] in operators:
#             expression = expression[:-1] + str(character)
#         else:
#             expression += str(character)
#
#     else:
#         expression += str(character)
#
#     return expression, 0
# #podnoszenie wpisanego równania do kwadratu
# def power2_fun():
#     global expression
#
#     value = str(eval(expression)**2)
#     return value
#
# #pierwiastek kwadratowy
# def sqrt_fun():
#     global expression
#
#     try:
#         expression = str(math.sqrt(eval(expression)))
#         return expression
#
#     except:
#         expression = ""
#         return "ERROR"
# #wylicza równianie, gdy wykreyje błąd zwraca error
# def equal_fun():
#     global expression
#
#     try:
#         expression = str(eval(expression))
#         return expression
#
#     except:
#         expression = ""
#         return "ERROR"
#
# #sprawdza czy jest w ciągu znaków przecinek jeśli jest to nie pozwala na kolejne wstawienie
# def comma():
#     global expression
#
#     if expression == "":
#         expression = "0."
#
#     else:
#         i = len(expression) - 1
#         while i >= 0:
#             if expression[i] == '.':
#                 return expression
#             if expression[i] in operators:
#                 if i == len(expression) -1:
#                     expression += '0'
#                 break
#             i -= 1
#         expression += '.'
#     return expression
#
def imaginary_part():
    global expression
    if expression == "":
        expression = "j"

    i = len(expression) - 1
    while i >= 0:
        if expression[i] == 'j':
            return expression
        if expression[i] in operators:
            if i == len(expression) - 1:
                expression += '0'
            break
        i -= 1
    expression += 'j'
    return expression


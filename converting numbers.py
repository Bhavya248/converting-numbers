# python program to convert decimal numbers to binary,octal,hexadecimal numers

print('"Enter a integer number"')
num = int(input())
result = []

# decimal to binary
def detobi(number) :
    while number >= 1 :
        if (number % 2) == 0:
            result.append('0')
            number = (number/2)
        else :
            number = (number-1)/2
            result.append('1')
    print("The binary      value for ",num," is --> ","".join(reversed(result)))
    result.clear()

detobi(num)
# decimal to octal
def detooc(number) :
    while number >= 1 :
        if (number % 8) == 0:
            result.append('0')
            number = (number/8)
        elif (number % 8) == 1 :
            result.append('1')
            number = (number - 1)/8
        elif (number % 8) == 2 :
            result.append('2')
            number = (number - 2)/8
        elif (number % 8) == 3 :
            result.append('3')
            number = (number - 3)/8
        elif (number % 8) == 4 :
            result.append('4')
            number = (number - 4)/8
        elif (number % 8) == 5 :
            result.append('5')
            number = (number - 5)/8
        elif (number % 8) == 6 :
            result.append('6')
            number = (number - 6)/8
        else  :
            result.append('7')
            number = (number - 7)/8
    print("The octal       value for ",num," is --> ","".join(reversed(result)))
    result.clear()
detooc(num)

# decimal to hexadecimal
def detohe(number) :
    while number >= 1 :
        if (number % 16) == 0:
            result.append('0')
            number = (number/16)
        elif (number % 16) == 1 :
            result.append('1')
            number = (number - 1)/16
        elif (number % 16) == 2 :
            result.append('2')
            number = (number - 2)/16
        elif (number % 16) == 3 :
            result.append('3')
            number = (number - 3)/16
        elif (number % 16) == 4 :
            result.append('4')
            number = (number - 4)/16
        elif (number % 16) == 5 :
            result.append('5')
            number = (number - 5)/16
        elif (number % 16) == 6 :
            result.append('6')
            number = (number - 6)/16
        elif (number % 16) == 7:
            result.append('7')
            number = (number - 7)/16
        elif (number % 16) == 8 :
            result.append('8')
            number = (number - 8)/16
        elif (number % 16) == 9 :
            result.append('9')
            number = (number - 2)/16
        elif (number % 16) == 10 :
            result.append('A')
            number = (number - 10)/16
        elif (number % 16) == 11 :
            result.append('B')
            number = (number - 11)/16
        elif (number % 16) == 12 :
            result.append('C')
            number = (number - 12)/16
        elif (number % 16) == 13 :
            result.append('D')
            number = (number - 13)/16
        elif (number % 16) == 14 :
            result.append('E')
            number = (number - 13)/16
        else :
            result.append("F")
            number = (number - 15)/16
    print("The hexadecimal value for ",num," is --> ","".join(reversed(result)))
    result.clear()
detohe(num)    
        
            

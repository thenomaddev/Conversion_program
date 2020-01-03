# FUNCTION DEFINITIONS
#------------------------------
def main():
    userSel = getMenuSelection()
    while userSel != 'Q':
        if userSel == 'T':
            userValue = getValueToConvert(userSel)
            theResult = calculateCelcius(userValue)
            printResult(userSel, userValue, theResult)
            print('\n', '\n')
            userSel = getMenuSelection()
        elif userSel == 'D':
            userValue = getValueToConvert(userSel)
            theResult = calculateKilometers(userValue)
            printResult(userSel, userValue, theResult)
            print('\n', '\n')
            userSel = getMenuSelection()
        elif userSel == 'W':
            userValue = getValueToConvert(userSel)
            theResult = calculateKilograms(userValue)
            printResult(userSel, userValue, theResult)
            print('\n', '\n')
            userSel = getMenuSelection()
        else:
            print('Error - Invalid option selected. You may only enter T, D,or W.')
            print('\n', '\n')
            userSel = getMenuSelection()

def menu():
    print('------------------')
    print('CONVERSION PROGRAM')
    print('------------------')
    print()
    print('T = Convert Fahrenheit to Celcius')
    print('D = Convert Miles to Kilometers')
    print('W = Convert pounds into kilograms')
    print()

def getMenuSelection():
    menu()
    conversionType = input("Select conversion to perform ('T'emperature, 'D'istance, 'W'eight), or 'Q'uit? ").upper()
    print()
    return conversionType
    
def getValueToConvert(conversion):
    if conversion == 'T' :
        fahrenheit = float(input('Please enter the temperature in fahrenheit: '))
        return fahrenheit
    elif conversion == 'D':
        miles = float(input('Please enter the distance in miles: '))
        return miles
    elif conversion == 'W':
        pounds = float(input('Please enter the weight in pounds: '))
        return pounds
    else:
        print('\n', '\n')
    
def calculateCelcius(fahrenheit):
    celcius = (fahrenheit - 32) / 1.8
    return celcius
def calculateKilometers(miles):
    kilometers = miles / 0.621371192237
    return kilometers
def calculateKilograms(pounds):
    kilograms = pounds / 2.2
    return kilograms
 
def printResult(first, second, third):
    if first == 'T':
        print(second, 'fahrenheit is ', round(third, 3), 'celcius.')
    elif first == 'D':
        print(second, 'miles is ', round(third, 3), 'kilometers.')
    else:
        print(second, 'pounds is ', round(third, 3), 'kilograms.')

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#
main()
input("\nRun complete. Press the Enter key to exit.")

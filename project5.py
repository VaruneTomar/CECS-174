def getRomanN(number):
    #asking user to input roman number and storing as uppercase
    roman_num = input("Enter " + str(number) + " Roman Number (no spaces): ").upper()

    #while the function return false, keep asking the user for input until it returns true 
    while not isValidRoman(roman_num):
        roman_num = input("Please enter a valid roman numeral: ").upper()

    #return value to the main function 
    return roman_num

def isValidRoman(roman):
    #creating variables 
    count = 0
    consecutive_three = 0
    consecutive_twice = 0
    #length of the string
    length = len(roman)
    #list of numerals
    numerals = ["I", "V", "X", "L", "C"]

    #loops for each index in the string
    for i in range(len(roman)):
        #if not a value from the list, count += 1
        if roman[i] not in numerals:
            count += 1
        
        if length > 1:
            #if one of the 3 numerals that can be repeated
            if roman[i] == 'I' or roman[i] == "X" or roman[i] == "C":
                if i > 0:
                    #if the value in the index is the same as last, adds to consecutive variable
                    if roman[i] == roman[i-1]:
                        consecutive_three += 1
                    elif roman[i] != roman[i-1]:
                        consecutive_three += 0
                        if consecutive_three < 3:
                            consecutive_three = 0
            #if one of the two numerals that can't repeat
            if roman[i] == "V" or roman[i] == "L":
                #if value in the index is the same as the last, adds to consecutive variable
                if roman[i] == roman[i-1]:
                    consecutive_twice += 1
                #if the other 3 numerals didnt repeat more then 3 times and V or L comes after, the variable for consecutive resets 
                if consecutive_three < 3:
                    consecutive_three = 0
                    
        
        #splits the string into pairs to check for certain errors
        for i in range(len(roman)):
            split = roman[i:i + 2]
            if "LC" in split: 
                count+= 1
            elif "VX" in split:
                count += 1
            elif "IL" in split: 
                count += 1
            elif "IC" in split:  
                count += 1

    #if there are no errors, the function returns as Valid 
    if count == 0 and consecutive_twice == 0 and consecutive_three < 3:
        #call conversion function to check for subtraction rule
        valid_subtraction = romanToArabic(roman)
        #if returns true, this function returns true and the value passed is valid
        if valid_subtraction == False:
            return False
        elif valid_subtraction == True:
            return True
    else:
        return False


def romanToArabic(roman):
    #turns string into a list
    romanlist= list(roman)
    #Finds length of the string 
    length = len(roman)
    #list of numerals
    numerals = ["I", "V", "X", "L", "C"]
    #lists of numbers matching the numerals
    numbers = [1, 5, 10, 50, 100]
    #empty list
    empty = []
    #creating variables
    testing = True
    total = 0
    num = 0
    
    for i in range(len(roman)):
        #finds value of index, looks for it in the numerals list, and uses corresponding index in numbers list to convert it
        #the value of the index from the list is stored as x
        x = romanlist[i]
        #finds the index of the value taken from roman list and stores it as y 
        y = numerals.index(x)
        #corresponding index from numbers list is stored in letter value,  
        letter_value = numbers[y]
        #adds the number to the list 
        empty.append(letter_value)
   
    

    #runs until all the indices are evaluated and numeral is fully converted 
    while num < (len(empty)):

        #if the length of the numeral is greater then 1
        if length > 1:

            #testing to see if numeral is valid and violates certain rules
            #if 3 or more indices to iterate are left, will check for errors in that situation
            if num + 3 < len(empty):
                #if the value in the current index equals that of index+2 while the middle index value is greater then both, the numeral is invalid
                #if the value in index + 1 equals that of index + 3 and the middle index is greater then both, the numeral is invalid 
                if empty[num+1] != empty[num+2] and empty[num+1] == empty[num+3] and empty[num+2] > empty[num+1]:
                    testing = False
                #if more then one value is less then that in front, the numeral is invalid
                if (empty[num] <= empty[num+1] and empty[num] <= empty[num+2] and empty[num] < empty[num+3]) or (empty[num] < empty[num+3] and empty[num+1] < empty[num+3] and empty[num+2] < empty[num+3]):
                    testing = False

            #if 2 or more indices to iterate are left, will check for errors in that situation
            if num + 2 < len(empty):
                #if value in current index equals the value in index + 2 while the middle index value is greater, the numeral is invalid 
                if empty[num] != empty[num+1] and empty[num+2] == empty[num] and empty[num] < empty[num+1]:
                    testing = False
                #if more then value is less then that in front, numeral is invalid
                #if value in first index is less then that of index + 1 and index + 2, the numeral is invalid 
                if (empty[num] <= empty[num+1] and empty[num] < empty[num+2]) or (empty[num] < empty[num+2] and empty[num+1] < empty[num+2]):
                    testing = False

            #converting the numeral to arabic
            #if 2 or more indices left, will evaluate for a certain situation
            if num + 2 < len(empty):
                if empty[num] > empty[num+1] and empty[num+2] > empty[num+1]:
                    total += empty[num] + (empty[num+2] - empty[num+1])
                    #num += 3 because 3 indices are evaluated in this process
                    num += 3

            if num + 1 < len(empty):
                #if the value in this index is greater then the next, add the two values 
                if empty[num] >= empty[num+1]:
                    total += empty[num] + empty[num+1]
                    #num += 2 because 2 indices are evaluated in this process
                    num += 2
                #if the value in this index is less then the next, subtract it from the next value
                elif empty[num] < empty[num+1]:
                    total += empty[num+1] - empty[num]
                    #num += 2 because 2 indices are evaluated in this process
                    num += 2
            #if there is only one value, then that is added to the total         
            else:
                total += empty[num]
                num += 1  
        #if the length is 1, the total is that of the one value    
        else:
            total += empty[num]
            num += 1

    #if there are no errors, the numeral is valid
    if testing == True:
        #global value is the numerical value of the roman numeral passed
        global value
        value = total
    #returns true or false depending on if the roman numeral is valid 
    return testing


def arabicToRoman(arabic):
    #list of numbers and list of corresponding numeral
    numbers = [100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    #creating empty string
    roman_total = ""
    #creating variable
    z = 0

    #if zero, no numeral to match zero
    if arabic == 0:
        return 0
    #runs until arabic number is fully converted
    while arabic > 0:
        #loop runs until number can no longer be divided 
        for x in range(arabic // numbers[z]):
            #adds the corresponding roman numeral to empty string 
            roman_total += numerals[z]
            #removes value converted to a numeral from the number
            arabic -= numbers[z]
        #adds to z for the next index or value
        z += 1

    #returns the roman numeral fully converted in what started as an empty string 
    return(roman_total) 

        
def add(roman1, roman2):
    #global value for numerical total after adding
    global add_total

    #total after adding stored as variable
    add_total = roman1 + roman2

    #calls arabictoroman function to convert total into roman numeral
    roman_conversion = arabicToRoman(add_total)

    #returns total after adding as a roman numeral
    return roman_conversion


def sub(roman1, roman2):
    #global values for numerical total and whether to put a negative sign in front
    global sub_total
    global negative_sign

    #total when subtracting the numbers
    sub_total = roman1 - roman2

    negative_sign = 0
    #if the total is less then 0, the negative sign value become 1 and a negative sign will be placed in the main function
    if sub_total < 0:
        negative_sign += 1
        #calls arabictoroman functio to convert into roman numeral and store
        roman_conversion = arabicToRoman(abs(sub_total))
    else:
        roman_conversion = arabicToRoman(sub_total)

    #returns total after subtracting as a roman numeral
    return roman_conversion


def mul(roman1, roman2):
    #global value for numerical total after multiplying
    global mul_total

    #total after multipling the numbers
    mul_total = roman1 * roman2

    #calls arabictoroman function to convert total into roman numerals
    roman_conversion = arabicToRoman(mul_total)

    #returns total after multiplying as roman numerals
    return roman_conversion

def div(roman1, roman2):
    #global value for numerical total after dividing
    global div_total

    #total after dividing the two numbers
    div_total = roman1 // roman2

    #global numerical remainder value
    global remainder
    remainder = roman1 % roman2

    #converting total after dividing and remainder into roman numerals
    roman_conversion = arabicToRoman(div_total)
    remainder_conversion = arabicToRoman(remainder)

    #returns total and remainder after dividing as roman numerals
    return (roman_conversion, remainder_conversion)

def menu():
    #prints menu and options to the user
    print("")
    print("Welcome to the Roman Numerals Calculator")
    print("Please select from the following:")
    print("")
    print("A - Add two Roman Numerals")
    print("S - Subtract two Roman Numerals")
    print("M - Multiply two Roman Numerals")
    print("D - Divide two Roman Numerals")
    print("Q - Quit")


def main():
    #the variable is true
    run_again = True

    #the program will loop until the user enters Q and run_again becomes false
    while run_again == True:
        menu()
        #asking the user for what they want to calculate
        user_option = input("Select A, S, M, D, or Q only. ").upper()
        print("")

        #if statements to perform certain actions depending on what option they choose

        if user_option == "A":
            #calling function to ask user for numeral and see if its valid 
            first  = getRomanN("First")
            #numerical value coming from global variable
            first_number = value
            print("Value of " + str(first) + " : " + str(first_number))
            second = getRomanN("Second")
            #numerical vallue of second # coming from global variable
            second_number = value
            #telling the user the results of the calculations
            print("Value of " + str(second) + " : " + str(second_number))

            #calling addition function to add numbers and return as numeral
            addition = add(first_number, second_number)
            print("")
            print(first, "+", second, "=", addition)
            print(first_number, "+", second_number, "=", add_total)

        elif user_option == "S":
            first  = getRomanN("First")
            first_number = value
            print("Value of " + str(first) + " : " + str(first_number))
            second = getRomanN("Second")
            second_number = value
            print("Value of " + str(second) + " : " + str(second_number))

            #calling subtraction function to subtract numbers and return result as a numeral 
            subtraction = sub(first_number, second_number)
            print("")
            #if the value is greater then zero from the global variable, there needs to be a negative sign in front 
            if negative_sign > 0:
                print(first, "-", second, "= -", subtraction)
            else:
                print(first, "-", second, "= ", subtraction)
            print(first_number, "-", second_number, "=", sub_total)

        elif user_option == "M":
            first  = getRomanN("First")
            first_number = value
            print("Value of " + str(first) + " : " + str(first_number))
            second = getRomanN("Second")
            second_number = value
            print("Value of " + str(second) + " : " + str(second_number))

            #calling multiplication function to multiply numbers and return product as a numeral 
            multiplication = mul(first_number, second_number)
            print("")    
            print(first, "*", second, "= ", multiplication)
            print(first_number, "*", second_number, "=", mul_total)

            
        elif user_option == "D":
            first  = getRomanN("First")
            first_number = value
            print("Value of " + str(first) + " : " + str(first_number))
            second = getRomanN("Second")
            second_number = value
            print("Value of " + str(second) + " : " + str(second_number))

            #calling division function to divide numbers and return result and remainder as a numeral
            (division,remainder_roman) = div(first_number, second_number)
            print("")
            #if the global remainder is greater then zero, need to tell the user the result with the remainder in numerals
            if remainder > 0:
                print(first, "/", second, "= ", division)
                print("remainder: ", remainder_roman)
                print(first_number, "/", second_number, "=", div_total)
                print("remainder:", remainder)
            else:
                print(first, "/", second, "= ", division)
                print(first_number, "/", second_number, "=", div_total)

        elif user_option == "Q":
            print("Good Bye.")
            run_again = False

        else:
            print("Invalid entry, please try again")

#calling the main function to run          
main()
    
    
    

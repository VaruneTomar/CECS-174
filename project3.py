#Varune Tomar Project 3

run_program = False

while run_program == False:
    
    #asking the user to input the customer code
    customer_code = (input("Enter the customer code: "))

    valid_customer_code = False

    #loop to validate the customer code and keeps asking the user to enter again until the entry is correct
    while valid_customer_code == False:
        if (customer_code == 'r' or customer_code == 'R') or (customer_code == 'c' or customer_code == 'C') or (customer_code == 'i' or customer_code == 'i'):
            valid_customer_code  = True
        else:
            customer_code = (input("Invalid entry try again, please enter: "))
            valid_customer_code = False

    #asking the user to enter the beginning meter reading
    beginning_m = int(input("Enter the beginning meter reading: "))

    valid_beginning_m = False

    #loop to validate the beginning meter reading and keeps asking the user to re-enter a value until validated
    while valid_beginning_m == False:
        if (0 <= beginning_m <= 999999999):
            valid_beginning_m = True
        else:
            beginning_m = int(input("Invalid entry try again, please enter: "))
            valid_beginning_m = False

    #asking the user to enter the ending meter reading
    ending_m = int(input("Enter the ending meter reading: "))

    valid_ending_m = False

    #loop to validate the ending meter reading and keeps asking the user to re-enter a value until validated 
    while valid_ending_m == False:
        if (0 <= ending_m <= 999999999):
            valid_ending_m = True
        else:
            ending_m = int(input("Invalid entry try again, please enter: "))
            valid_ending_m = False


    #declaring variables 
    water_gallons = 0.0
    amount_billed = 0.0 

    #if statement to perform certain calculations based on the customer code 
    if (customer_code == 'r' or customer_code == 'R'):
        if ending_m > beginning_m:
            water_gallons = (ending_m - beginning_m) / 10
        elif ending_m < beginning_m:
            water_gallons = ((ending_m - beginning_m) % 10) / 10

        #calculation to find the amount billed 
        amount_billed = 5 + (water_gallons * 0.0005)

        #telling the user their inputs, water gallons used, and amount billed 
        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')
        print("")

        #asking the user if they want to do the calculation again
        do_again = input("Do you want to perform the calculation again: ")

        validate_do_again = False

        #while loop to validate entry for do_again, will ask the user to re-enter if 
        while validate_do_again == False:
            #the entire program will either run again or end based on the user response
            if do_again == "Y" or do_again == "y":
                validate_do_again = True
                run_program = False
            elif do_again == "N" or do_again == "n":
                validate_do_again = True
                run_program = True
                print("Goodbye")
            else:
                do_again = input("Invalid entry try again, please enter: ")
                validate_do_again = False
                

    #if statement to perform certain calculations based on the customer code
    elif (customer_code == 'c' or customer_code == 'C'):
        if ending_m > beginning_m:
            water_gallons = (ending_m - beginning_m) / 10
        elif ending_m < beginning_m:
            water_gallons = ((ending_m - beginning_m) % 10) / 10
        #if statements to calulate the amount billed based off the amount of water used 
        if water_gallons <= 4000000:
            amount_billed = 1000
        else:
            amount_billed = 1000 + ((water_gallons - 4000000) * 0.00025)

        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')

        #asking the user if they want to do the calculation again
        do_again = input("Do you want to perform the calculation again: ")

        validate_do_again = False

        #while loop to validate entry for do_again, will ask the user to re-enter if 
        while validate_do_again == False:
            #the entire program will either run again or end based on the user response
            if do_again == "Y" or do_again == "y":
                validate_do_again = True
                run_program = False
            elif do_again == "N" or do_again == "n":
                validate_do_again = True
                run_program = True
                print("Goodbye")
            else:
                do_again = input("Invalid entry try again, please enter: ")
                validate_do_again = False
                

    #if statement to perform certain calculations based on the customer code
    elif (customer_code == 'i' or customer_code == 'I'):
        if ending_m > beginning_m:
            water_gallons = (ending_m - beginning_m) / 10
        elif ending_m < beginning_m:
            water_gallons = ((ending_m - beginning_m) % 10) / 10
        #depending on how much water is used, changes calculation to find the amount billed 
        if water_gallons <= 4000000:
            amount_billed = 1000
        elif 4000000 < water_gallons < 10000000:
            amount_billed = 2000
        else:
            amount_billed = 2000 + ((water_gallons - 10000000) * 0.00025)

        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')

        #asking the user if they want to do the calculation again
        do_again = input("Do you want to perform the calculation again: ")

        validate_do_again = False

        #while loop to validate entry for do_again, will ask the user to re-enter if 
        while validate_do_again == False:
            #the entire program will either run again or end based on the user response
            if do_again == "Y" or do_again == "y":
                validate_do_again = True
                run_program = False
            elif do_again == "N" or do_again == "n":
                validate_do_again = True
                run_program = True
                print("Goodbye")
            else:
                do_again = input("Invalid entry try again, please enter: ")
                validate_do_again = False
                

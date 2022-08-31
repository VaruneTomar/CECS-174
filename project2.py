#Varune Tomar Project 2

#asking the user to input the code, beginning meter reading, and ending meter reading
customer_code = (input("Enter the customer code: "))
beginning_m = int(input("Enter the beginning meter reading: "))
ending_m = int(input("Enter the ending meter reading: "))

#declaring variables 
water_gallons = 0.0
amount_billed = 0.0 

#the first if statement is to perform different actions based on the customer code and check for errors
if (customer_code == 'r' or customer_code == 'R'):
    #the second if statement is to check if the meter values are between 0 and 999999999
    if (0 <= beginning_m <= 999999999) and (0 <= ending_m <= 999999999):
        #the third if statement is to calculate the gallons using different formulas based on the meter inequalities 
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
        print("Process finished with exit code 0")
        
    #if the user enters a value not in the range of 0 and 999999999, this error appears 
    else:
        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Invalid Entry")
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')
        print("Process finished with exit code 0")

elif (customer_code == 'c' or customer_code == 'C'):
    if (0 <= beginning_m <= 999999999) and (0 <= ending_m <= 999999999):
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
        print("Process finished with exit code 0")
        

    else:
        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Invalid Entry")
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')
        print("Process finished with exit code 0")

elif (customer_code == 'i' or customer_code == 'I'):
    if (0 <= beginning_m <= 999999999) and (0 <= ending_m <= 999999999):
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
        print("Process finished with exit code 0")
        

    else:
        print("")
        print("Customer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(beginning_m))
        print("Ending meter reading: {:0>9}".format(ending_m))
        print("Invalid Entry")
        print("Gallons of water used:", water_gallons)
        print("Amount billed: $", format(amount_billed,'.2f'),sep='')
        print("Process finished with exit code 0")

#if the user doesnt enter a valid customer code, this error appears 
else:
    print("")
    print("Customer code:", customer_code)
    print("Beginning meter reading: {:0>9}".format(beginning_m))
    print("Ending meter reading: {:0>9}".format(ending_m))
    print("Invalid Entry")
    print("Gallons of water used:", water_gallons)
    print("Amount billed: $", format(amount_billed,'.2f'),sep='')
    print("Process finished with exit code 0")



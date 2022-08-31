run_again = True

#loop will run as long as user enters a postive integer
while run_again == True:

    #asking the user to input an integer
    user_number = int(input("Please enter an integer (negative to quit): "))

    #declaring variables 
    add_persist = 0
    mult_persist = 0
    mult_root = 0
    add_root = 0
    mult_root = 0

    #if the input is postive but a single digit, the persistences are 0 and the roots equals the number
    if 0 <= user_number < 10:
        print("Additive Persistence: 0",",Additive Root:",user_number)
        print("Multiplicative Persistence: 0","Multiplicative Root:",user_number)

    #if the number is not a single digit, will have to calulate the roots and persistences
    elif user_number >= 10:

        #storing user number into a different variable to use for calculating
        add_root = user_number

        #this loop runs until the number becomes a single digit, and finds the additive root and persistence
        while add_root >= 10:

            #storing add_root into a different variable for the next loop
            add_loop = add_root

            #if the loop repeats, the total resets to 0 to find the sum of the new integer
            total = 0

            #loop to add each digit of the number, finding the sum
            while add_loop > 0:
                #pulling out each individual digit in a loop and adding them together, sum of digits is stored in total
                total += (add_loop % 10)

                #after pulling a single digit, removes the digit from the larger total number
                add_loop = add_loop // 10

            #the larger while loop repeats using the new integer if it's not a single digit
            add_root = total

            #each cycle is a persistence
            add_persist += 1



        #storing user number into a different variable used for calulating
        mult_root = user_number

        #this loop runs until the number becomes a single digit, and find the mulitplicative root and persistence
        while mult_root >= 10:
        
            mult_loop = mult_root

            #each time the loop repeats, the total resets to 1 so the digits of the number can be stored 
            total = 1
            
            while mult_loop > 0:
                #pulling out each indidual digit in a loop and adding them together each time until loop stops
                total *= (mult_loop % 10)

                #after pulling a single digit, removes the digit from the larger total number
                mult_loop = mult_loop // 10

            #if the cycle doesnt produce a single digit, the loop repeats for the new integer
            mult_root = total

            #each cycle is a persistence
            mult_persist += 1

        #telling the user the results 
        print("Additive Persistence:",add_persist,",Additive Root:",add_root)
        print("Multiplicative Persistence:",mult_persist,"Multiplicative Root:",mult_root)
        print("")

    #if the user inputs a negative number, prints a message and the program ends 
    elif user_number < 0:

        #larger while loop will stop repeating
        run_again = False

        print("Thanks for playing with numbers...Goodbye")
    
        

# Andrew Robinson 2/5/19

import random

def main():
    # Calls user_guess function
    user_guess()
    

def user_guess():
    again = "y"
    guess = 0
    # While the response to the Yes or No question is "Y", the loop will 
    # continue
    while again.upper() == "Y":
        num_guesses = 0
        # Generates a random number from 1 to 100
        number = random.randint(1,100)
        # Allows at most 100 guesses
        for num in range(1,101):
           # While the user's guess doesn't match the random number, the
           # loop will continue
           while guess != number:
               # Asks the user to guess the random number
               guess = int(input("Please enter a number from 1 to 100: "))   
               
               # If the user's guess is too low, it will print this message
               if guess < number:
                   print("Too low, try again.")
               # If the user's guess is too high, it will print this message
               elif guess > number:
                   print("Too high, try again.")
               # Once the correct number is guessed, this message will printed,
               # which inclues a congratulations and what the correct number 
               # was
               else:
                   print("\nCongratulations! You guessed the right number!")
                   print("\nThe correct number was: %d" % (number))
               
                   while True:
                       # Asks the user if they want to play again
                       again = input("Do you want to play again? Y or N: ")
                       
                       # If the user answers "Y" the program will restart with
                       # a new random number. If the user answers "N" the
                       # the program will end.
                       if again.upper() == "Y" or again.upper() == "N":
                          break 
                           # If the user answers anything other than, "Y" or
                           # "N" it will tell them to enter one of those
                           # options and ask the question again.
                       if again.upper() != "Y" and again.upper() != "N":
                          print("\nPlease enter ""Y"" or ""N!""" )
                          
               
               # Tallies up the number of guesses
               num_guesses += num
               
               # The first time the user guesses the number, it will print
               # "time" instead of "times"
               if num_guesses == 1:
                   print("\nYou've guessed the number %d time!" 
                         % (num_guesses))
               else:
                   print("\nYou've guessed the number %d times!" 
                         % (num_guesses))
               
    return number  

# Calls main function
main()             
       
        
         
        




#numberguess 
#written for python v3x

#This contains the criteria for who wins
def the_judge(computer_guess,user_guess,num2guess):
	if user_guess == num2guess:
		print("You won! Nice job, now if only you could find a way out of the matrix...")
	elif computer_guess == num2guess:
		print("Darn, looks like the computer out-smarted you on this one, good luck keeping your job!")
	elif user_guess == computer_guess:
		print("WOW, what are the odds of that! You copied the computer! Nice one. ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print("...")
		print("The odds are 1 in 100... if you were woundering")
	else:
		print("Okay neither you or the computer guessed the right number exactly")
		print("However...")
		if abs(int(num2guess) - int(user_guess)) > abs(int(num2guess)-int(computer_guess)):
			print("")
			print("The computer was a liiiitle closer than you, sorry bud.")
		else:
			print("")
			print("You beat the machine! Congratulations, now go play outside")




print("This is a game that will test your guessing skill")
print(" ")

high = input("Please enter the difficlty you would like by entering 3, 5, 10... ect : ")
high = int(high)


print("Okay the number you will be guessing is between 1 & {} ".format(high))
print("")
user_guess = input("Now please enter your guesss and try to beat the computer! Your guess: ")


#generates a random number 
import random
num2guess = random.randrange(1,high,1)
print(" ")


#generates another random number
computer_guess = random.randrange(0,high,1)

#sends numbers to the function I made to determine winner
the_judge(computer_guess,user_guess,num2guess)

#For debugging-----------------------------------------
print("")
print("user said: {}  comp said: {}  actual num is: {}".format(user_guess,computer_guess,num2guess))
print("")
#------------------------------------------------------




#to make even harder could have if statemts that if the computer's guess is more than 
#3 away from goal than the computers guess has 2 subtracted from it(or some other number) 
#and if the computers guess is lower by more than three it has two added to it
#maybe instead of adding/subtracting 2 use some fraction of the upper limit, so it gives the computer an 
#even lager advatange
#the latter could be 'extreme' mode while using 2 is just 'hard' mode

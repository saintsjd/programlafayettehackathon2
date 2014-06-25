#
# Higher/lower guessing game
#

import random

secret = random.randrange(1,100)
guess = 0

while guess != secret:

    guess = int(raw_input("Guess my number: "))

    if guess < secret:
        print "too low"
    elif guess > secret:
        print "too high"
    else:
        print "You got it!", guess




#
# advanced variation limits user to 5 tries
#       
# Guess my number: 50
# too low.  5  guesses remain
# Guess my number: 75
# too high.  4  guesses remain
#

import random

MAX_GUESSES = 5
secret = random.randrange(1,100)
guess_count = 0
guess = 0

while guess != secret:

    guess = int(raw_input("Guess my number: "))
    guess_count += 1

    if guess < secret:
        print "too low. ", MAX_GUESSES - guess_count, " guesses remain"
    
    if guess > secret:
        print "too high. ", MAX_GUESSES - guess_count, " guesses remain"
    
    if guess == secret:
        print "You got it!", guess
        break
	elif guess_count == MAX_GUESSES:
        print "Too many guesses!"
        break

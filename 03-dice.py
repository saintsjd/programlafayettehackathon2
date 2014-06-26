#
# Roll a die. Try to get as close to eleven without going over.
# Play against a computer opponent
#

import random

human_score = 0
computer_score = 0
MAX = 11

print "Roll a die, get as close to 11 without going over"
print

choice = None

while choice != "s" and human_score < 11:
    print "Your score is ", human_score
    choice = raw_input("What do you want to do? Roll(r) or Stand(s)? ")

    if choice == "r":
    	human_score += random.randrange(1,6)

    if choice == "s":
    	break

while computer_score < 8:
	computer_score += random.randrange(1,6)

print "You: ", human_score, " computer: ", computer_score

if human_score > MAX:
	print "BUSTED! You lose."
elif computer_score > MAX:
	print "Computer BUSTED! You win."
elif human_score < computer_score:
	print "You lose!"
elif human_score > computer_score:
	print "You win!"
elif human_score == computer_score:
	print "Tie!"
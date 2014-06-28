import random
myscore = 0
compscore = 0
choice = "Nothing"
while choice != 'n' and myscore < 11:
    roll = random.randrange(1,7)
    myscore = myscore + roll 
    print "You rolled a ", roll 
    print "Your score is ", myscore
    choice = raw_input("Roll Again?")

while compscore < 8:
    compscore += random.randrange(1,7)

print "Your score is ", myscore
print "Computer score is ", compscore

if myscore > 11:
    print "You BUSTED!!"
elif compscore > 11:
    print "Computer BUSTED!!!"
elif myscore == compscore:
    print "TIE!!"
elif myscore < compscore:
    print "You Lose!"
elif myscore > compscore:
    print "YOU WIN!!! FIZZ BUZZZZ"


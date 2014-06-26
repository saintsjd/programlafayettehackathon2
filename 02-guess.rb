#
# Higher/lower guessing game
#

secret = Random.rand(100)
guess = 0

while guess != secret do
  print "Guess my number> "
  guess = Integer(gets.chomp)

  if guess < secret
    puts "Too low"
  elsif guess > secret
    puts "Too high"
  else
    puts "You got it! #{guess} was my number."
  end
end

#
# advanced variation limits user to 5 tries
#
# Guess my number: 50
# too low.  5  guesses remain
# Guess my number: 75
# too high.  4  guesses remain
#

MAX_GUESSES = 5
secret = Random.rand(100)
guess_count = 0
guess = 0

while guess != secret do
  print "Guess my number> "
  guess = Integer(gets.chomp)
  guess_count += 1

  if guess < secret
    puts "Too low. #{MAX_GUESSES-guess_count} guesses remain!"
  end

  if guess > secret
    puts "Too high. #{MAX_GUESSES-guess_count} guesses remain!"
  end

  if guess == secret
    puts "You got it! #{guess}"
  elsif guess_count == MAX_GUESSES
    puts "Too many guesses!"
    break
  end
end

#
# Roll a die. Try to get as close to eleven without going over.
# Play against a computer opponent
#
human_score = 0
computer_score = 0
MAX = 11

puts " <><> Roll a die, get as close to 11 without going over <><>"

choice = ""

while choice != "s" && human_score < 11 do
  puts "Your score is #{human_score}."
  print "What do you want to do? Roll(r) or Stand(s)? "
  choice = gets.chomp
  if choice == "r"
    human_score += Random.rand(1...6) # not including 6
  end

  if choice == "s"
    break
  end

end

while computer_score < 8 do
  computer_score += Random.rand(1...6) # not including 6
end

puts "You: #{human_score} Computer: #{computer_score}"

if human_score > MAX
  puts "BUSTED! You lose!"
elsif computer_score > MAX
  puts "Computer BUSTED! You win!"
elsif human_score < computer_score
  puts "You lose!"
elsif human_score > computer_score
  puts "You win!"
elsif human_score == computer_score
  puts "Tie!"
end
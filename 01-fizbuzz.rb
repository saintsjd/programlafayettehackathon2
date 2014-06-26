while true do
  print "Enter a number> "
  number = Integer(gets.chomp)

  if number == -1
    break
  end

  if number % 3 == 0 && number % 5 == 0
    puts "FIZZBUZZ"
  elsif number % 3 == 0
    puts "FIZZ"
  elsif number % 5 == 0
    puts "BUZZ"
  end
end

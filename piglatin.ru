input_string = gets.chomp
string_array = input_string.split(" ")
string_array.each do |word|
    pig_latin = word[1...word.length]+word[0]+"ay"+" "
    print pig_latin 
end

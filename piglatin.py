#My attempt at Pig Latin 

string = input().split()
string_arr = []
for word in string:
    new_word = word[1:len(word)]+word[0]+"ay"+" "
    string_arr.append(new_word)
print("".join(string_arr))
   
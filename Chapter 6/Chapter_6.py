# immutable - some not changable
# mutable - can be changed after creation

string = "!!!!!!!!!!i am dhruba!!!!!!!!!!\n"
heading = "welcome to my website"
num = "90"
space = " "
ascii_string = "@"

print(string.upper())   # convert all characters in string into uppercase
print(string.lower())   # convert all characters in string into lowercase
print(heading.capitalize())   # capitalize only the first character of the heading
print(heading.title())     # title() is similar to capitalize(), but it converts the first character of each word to
print(string.count('!'))
print(string.find('d'))       # returns index of 'd' if found, else returns -1
print(string.replace('dhruba', 'Ankit'))   # replaces 'Dhruba' with 'Ankit'
print(string.lstrip('!'))      # removes leading '!' from the string from left
print(string.rstrip('!'))      # removes trailing '!' from the string from right
print(string.swapcase())      # swap case of all alphabets (convert uppercase to lowercase and vice versa)
print(string.center(100, '#'))   # center aligns the string with specified length
print(string.split())
print(string.endswith('b'))    # checks whether the string ends with 'b' or not
print(string.startswith('!'))  # checks whether the string starts with '!' or not
print(string.index('h'))      # returns the position where 'h' is
print(num.isalnum())             # check whether it is a number or not
print(num.isdigit())            # check whether it contains digits only or not
print(space.isspace())         # check whether it contains space only or not
print(string.isalpha())         # check whether it contains alphabet only or not
print(string.isprintable())      # check whether all characters are printable or not
print(string.istitle())           # title case means that each word should startwith an uppercase letter 
print(string.isupper())           # check whether it is a uppercase string or not
print(string.islower())           # check whether it is a lowercase string or not
print(ascii_string.isascii())           # check whether it contains ASCII characters only or not

# Example 1:Take string from user and return the middle 3 characters of the given String
String = input("Enter the String ")
middleIndex = int(len(String)/2)
print(middleIndex) 
print(String[middleIndex])
print(String[middleIndex-1:middleIndex+2])





# Example 2:Create a string made of the first, middle and last character
#Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = "james"
print("Original string is", str1)
res  = str1[0] # get first character
l = len(str1)  # get string size
mi = int(l / 2) # get middle index number
res = res + str1[mi] # get middle character and get into the result
res = res + str1[l-1]  # get last character and add into  the result
print("new string:", res)





#Example 3:Append new string in the middle of a given string
str1 = "priya"
str2 = "chauhan"
l = len(str1) #first we take length of the str1
mi = int(l/2)  # then divide the str1 into the 2 part
str3 = str1[:mi]+str2+str1[mi:] # concatenate them all
print("new string is:",str3)






#Example 4:Create a new string made of the first, middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.










#Exercise 5: Arrange string characters such that lowercase letters should come first
#Given:str1 = PyNaTive
str1 = "pyNaTive"
print("original string:",str1)
lower = []
upper = []
for char in str1:
    if char .islower():
        lower.append(char)
    else:
        upper.append(char)
Sorted_str = ''.join(lower+upper)
print('Result:',Sorted_str) 








#Exercise 6: Count all letters, digits, and special symbols from a given string
#Given:str1 = "P@#yn26at^&i5ve"          
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)







#Exercise 6: Create a mixed String using the following rules
#Given two strings, s1 and s2. Write a program to create a new string s3 made of 
#the first char of s1, then the last char of s2, Next, the second char of s1 
#then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# given:s1="abc",s2 ="xyz"

s1 = "abc"
s2 = "xyz"
# get string length
s1_length = len(s1)
s2_length = len(s2)
#get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""
# reverse s2
s2 = s2[::-1]
#iterate string
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    
    if i < s2_length:
        result = result +s2[i]
print(result) 

    



#Exercise 7: String characters balance Test
#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.      
#Given:

#Case 1:

#s1 = "Yn"
#s2 = "PYnative"
#Expected Output:

#True
#Case 2:

#s1 = "Ynf"
#s2 = "PYnative"
#Expected Output:

#False  

def string_balance_test(s1,s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag =  False
    return flag

s1 = "yn"
s2 = "pynative"
flag = string_balance_test(s1,s2)
print("s1 ans s2 are balanced:", flag)

s1 = "ynf"
s2 = "pynative"
flag = string_balance_test(s1,s2)
print("s1 and s2 are balanced:",flag)






  
  
  
# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Given:str1 = "Welcome to USA. usa awesome, isn't it?" find usa occurences
str1 =  "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"
temp_str = str1.lower() #convert string to a lower function
count = temp_str.count(sub_string.lower())
print("The usa count is:",count)







#Exercise 9: Calculate the sum and average of the digits present in a string
#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
#Given:str1 = "PYnative29@#8496"

str1 = "PYnative29@#8496"
total = 0
cnt = 0
for char in str1:
    if char.isdigit():
        total += int(char)
        cnt +=1
avg = total / cnt
print("Sum is:",total,"Average is",avg)







#Exercise 10: Write a program to count occurrences of all characters within a string
# given: str1 = "Apple"  
#expected output: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 ="Apple"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print("result:",char_dict)  



  
             

#Exercise 11: Reverse a given string
#Given: str1 = "PYnative"

str1 = "PYnative"
print("original string is:",str1)
str1 = str1[::-1]
print("reversed string is:",str1)






#Exercise 12: Find the last position of a given substring
#Write a program to find the last position of a substring “Emma” in a given string.
#Given:str1 = "Emma is a data scientist who knows Python. Emma works at google."


str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("oroginal string is:",str1)
index = str1.rfind("Emma")
print("last occurence of Emma starts at index:",index)


#Exercise 13: Split a string on hyphens
#Write a program to split a given string on hyphens and display each substring.
#given:str1 = Emma-is-a-data-scientist

str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)
    
    
    
#Exercise 14: Remove empty strings from a list of strings
#Given: str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]   
res_list =[]
for s in str_list:
    if s:
        res_list.append(s)
print(res_list) 


#Exercise 15: Remove special symbols / punctuation from a string
#given:str1 = "/*Jon is @developer & musician"

import string
str1 = "/*Jon is @developer & musician"
print("original string is",str1)

new_str = str1.translate(str.maketrans('','',string.punctuation))
print("new string is:",new_str)   


#Exercise 16: Removal all characters from a string except integers
#Given:str1 = 'I am 25 years and 10 months old'

str1 = 'I am 25 years and 10 months old'
print("original string is:",str1)

res = "".join([item for item in str1 if item.isdigit()])
print(res)


#Exercise 17: Find words with both alphabets and numbers
#Write a program to find words with both alphabets and numbers from an input string.
#Given:str1 = "Emma25 is Data scientist50 and AI Expert"

str1 = "Emma25 is Data scientist50 and AI Expert"
print("original string is:", str1)

res = []
res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
    
    
#Exercise 18: Replace each special symbol with # in the following string
#Given:str1 = '/*Jon is @developer & musician!!'    

import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1) 






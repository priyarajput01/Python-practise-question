#Exercise 1: Calculate the multiplication and sum of two numbers
# given number=20,number=30 expected output-600
#given number=40,number=30  expected output-70

def multiplication_or_sum(num1,num2):
    product=num1*num2
    if product <= 1000:
        return product
    else:
        return num1+num2
result = multiplication_or_sum(20,30)
print("The result is",result)

result = multiplication_or_sum(40,30)
print("The result is",result)   



#Exercise 2: Print the Sum of a Current Number and a Previous number 

print("Printing current and previous number and their sum in the range(1, 11):")
previous_num = 0  # Initialize previous number as 0
# Loop through numbers 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i  # Calculate the sum of current and previous numbers
    print("Current number:", i, "Previous number:", previous_num, "Sum:", x_sum)  
    
    
#Exercise 3: Print characters present at an even index number
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
word = input("Enter word")
print("original string:",word)
size=len(word)
print("print only even index chars")
for i in range(0, size -1, 2):
    print("index[", i, "]", word[i])
    
    
    
#Exercise 5: Check if the first and last numbers of a list are the same
#given numbers_x = [10, 20, 30, 40, 10]
    # numbers_y = [75, 65, 35, 75, 30]    
    def first_last_same(numberlist):
        print("Given list:",numberlist)
        
        first_num = numberlist[0]
        last_num = numberlist[-1]
        
        if first_num == first_num:
            return True
        else:
            return False
number_x = [10,20,30,40,50]
print("result is",first_last_same(number_x))


number_y = [10,20,30,40,50]
print("result is",first_last_same(number_x))


# Exercise 6: Display numbers divisible by 5
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55
num_list = [10,20,30,40,50]
print("given_list:",num_list)
print('divisible by 5')
for num in num_list:
    if num % 5 == 0:
        print(num)
        
        
# Exercise 7: Find the number of occurrences of a substring in a string
# Given: str_x = "Emma is good developer. Emma is a writer"        
str_x = "Emma is good developer. Emma is a writer"
count = str_x.count("Emma")
print(count)




# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for num in range(5):
    for i in range(num):
        print(num, end="")
    print("/n") 
    
       

# example:9 print the pattern
# *
# * *
# * * *
# * * * * 
# * * * * *

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print("/n")    
    
    
    
#example:10  print this pattern
# * * * * *
# * * * *
# * * *
# * * 
# *

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")  
    
    
# Exercise 11: Check Palindrome Number
value = input("Enter the value")
reversed_value=[]
if value == reversed_value:
    print("its a palindrome value")
else:
    print("its not a palindrome value")    
    
    
# Exercise 12: Merge two lists using the following condition
def merge_list(list1,list2):
    result_list=[]
    
    for num in list1:
        if num%2==0:
            result_list.append(num)
            
    for num in list2:
        if num%2==0:
            result_list.append(num)
    return result_list

list1=[10,20,25,30,35] 
list2=[40,45,60,75,90] 
print("result list:",merge_list(list1, list2))   



# Exercise 13: Print characters present at an even index number 
str = input("enter a string:")
print(str)
print(len(str))
len=len(str)
for i in range(0,len,2):
    print(str[i])
  


#Exercise 14: Print multiplication table from 1 to 10  
for i in range(1,11):
    for j in range(1,11):
        print(i * j, end=" ")
    print("\t\t")    
    
    
    
#Exercise 15: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *    
for i in range(6,0,-1):
    for j in range(0,i,-1):
        print("i",end="")
    print("")    
    
    
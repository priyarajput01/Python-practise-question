# Exercise 1: Print first 10 natural numbers using for  loop
for i in range(1,11):
    print(i)
    
# Example 2: Print the following pattern   
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
print("print numbers")
row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')    
    
    
#  Example 3: Calculate sum of all numbers from 1 to a given number in python
 # Take input from the user
value1 = int(input("Enter a number: "))
  # Initialize sum variable to 0
Sum = 0
# Iterate through numbers from 1 to value1 (inclusive)
for i in range(1, value1 + 1):
    Sum += i  # Add the current number to Sum
# Print the final sum
print("Sum is:", Sum)


# Example 4 print multiplication of a given number
n=9
for i in range(1,11):
    product=n*i
    print(product)
    
# Example 5 :display numbers from a list using a loop
# given=[12,75,150,180,145,525,50]
numbers=[12,75,150,180,145,525,50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item%5==0:
        print(item) 
        
        
# Example  6: Count the total number of digits in a number     
#given-75869
num = 75869
count = 0
while num != 0:
    num=num//10
    count=count+1
print("total digits are:",count)    


# Example 7: print the pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5 

n=int(input("Enter number of row needed"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print() 
    
# Example 8: print the pattern    
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1 












# Exercise 9: Print list in reverse order using a loop
# Given:list1 = [10, 20, 30, 40, 50] 
list1 = [10,20,30,40,50]
new_list = reversed(list1)
for item in new_list:
    print(item)
    
    
# Exercise 10: Display numbers from -10 to -1 using for loop 
for i in range(-10,0,1):
    print(i)    

# Exercise 11: Display a message “Done” after the successful execution of the for loop
#Given:for i in range(5):
#    print(i)

for i in range(0,6):
    print(i)
print("Done")  

#Exercise 12: Print all prime numbers within a range  
#Given range start =25,end=50
start = 25
end = 50  
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
            
#Example 13 Display Fibonacci series up to 10 terms
no = int(input("Enter the no till what you want to the series:"))
a = 0
b = 1
c = 0
print(a)
print(b)
i = 1
while i<no:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)
              
              
#Example 14 Find the factorial of a given number
num = int(input("Enter a number"))
fact = 1

if num<0:
    print("Factorial of 0 does not exits")
if num==0:
    print("Factorial is 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of the given number is",fact)     


#Example 15 Reverse a integer number
num = int(input("enter a number:"))
renum = 0
for i in range(0,len(str(num))):
    lastdigit = num%10
    renum = (renum*10)+lastdigit
    num = num//10
print("reversed number=",renum) 




#Example 16 print element from a given list present at odd index number
my_list=[10,20,30,40,50,60,70,80,90,100] 
for i in my_list[1::2]:
    print(i,end=" ")   
    
    
# Example 17 calculate the cube of all the numbers from 1 to given number
input_number = 6
for i in range(1,input_number+1):
    print("current number is:",i," and the cube is",(i*i*i)) 
    
    
#Example 18 print the pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *
rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(4,0,-1):
    for j in range(0,i-1):
        print("*",end = " ")
    print("\r")                                         
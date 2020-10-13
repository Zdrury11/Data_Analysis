#!/usr/bin/env python
# coding: utf-8

# # Homework 1 (20 pts)
# 
# ## Due Date: 10/13/2020 ( Tuesday 11:59AM)
# 
# Save Notebook file as :HW1_LastFourDigitsofYourStudentID_YourName.ipynb
# 
# Email to: jzhang@eastwest.edu
# 
# Subject: CI280 Homework 1 

# Ch02 Input, Output
# 
# Problem 1: Computer present value ( Input , compute and output: 2 points)
# 
# present_value = future_value / ( 1.0 + rate) ** years

# In[9]:


# Problem 1: (2 pts)

# Input (1 point)
future_value = 0
interest_rate = 0
years = 0

future_value = float(input("Enter future value: "))
interest_rate = float(input("Enter interest rate: "))
years = float(input("Enter a year: "))

# Compute (1 point)
present_value = future_value/(1.0+interest_rate)**years

# Output 
print('Present value: $', format(present_value, ".2f"))


# # Chapter 03 - Decision -- if ... else ...
# 
# Problem 2: Software Sales (Page 154) ( 5 pts)
# A softare company sells a package that retais for $99. Quantity discounts are given according to following table:
#     Quantity     Discount
#     10 - 19       10%
#     20 - 49       20%
#     50 - 99       30%
#     100 or more   40%
#     
# Write a program that ask the uer to enter number of packages, and display the dicount rate, discount and total pay.
# 
#     Declare constant variables -- 1 pt
#     Input                      -- 1 pt
#     Compute discount rate      -- 2 pts
#     Compute other              -- 1 pt
#     -----------------------------------
#     Total points                  5 pts

# In[49]:


# Problem 2: (5 pts)
retail_price = 99

# Get input
packages = int(input ("Enter the number of packages: "))


# Compute
if packages < 10:
    discount = 0
elif 10 <= packages and packages < 20:      
    discount = 0.1                         # 10%
elif 20 <= packages and packages < 50:      
    discount = 0.2                         # 20%
elif 50 <= quantity and quantity < 100:     
    discount = 0.3                         # 30%
else:
    discount = 0.4                         # 40%
    
original_cost = retail_price * packages
discount_rate = packages * discount
total_savings = original_cost - retail_price 
discount_saving = original_cost / packages

# Print Results
print()
print("====Summary====")
print("Number of packages purchased: ", packages)
print("Discount rate: ", discount_rate)
print("Original Cost: $", original_cost)
print("Cost after discount: $", total_savings)
print("Your discount saving: $", discount_saving)


# In[ ]:


## OUTPUT
Number of packages purchased: 10
Discount rate: 10.0 %
Original Cost:  $ 990
Cost After Discount:  $ 891.0
Your discount saving:  $ 99.0


# # Chapter 04 - Loop
# 
# Problem 3: Tuition Increase ( 3 pts) At one college, the tuition for a full-time student is $8000 per semsestr. The college will incease the tuituin by 3% per year for next five years. Write a program to display the projected tuition amount for the next five years
# 
# Declare constant variables 
# loop and Compute           -- 2 pts
# Display format             -- 1 pts
# -----------------------------------
# Total points                  3 pts

# In[3]:


tuition = 8000
rate = 0.03

#Display
print('Project  Tuition for the next five years')
print('Year \t\t Tuition')
print('---------------------------')

# Compute
for year in range (1, 6):
    tuition += ( rate ) * tuition
    
#Display Data    
    print(str(year) + "\t\t $" + format( tuition, ".2f"))
    

## OUTPUT
Projected Tuition for the next five years
Year 		 Tuition
--------------------------
1 		$ 8000.0
2 		$ 8240.0
3 		$ 8487.2
4 		$ 8741.8
5 		$ 9004.1
# # Chapter 05  - Function
# 
# Problem 4: ( 4 pts)
# Write a function to generate random numbers, and keep a count how many are even numbers, and how many are odd numbers,
# and return two counts
# 
# Generate 100 random numbers to show the ratio.
# Generate 1000 random numbers to show the ratio.
# Generate 10000 random numbers to show the ratio.
# 
# Hints: 
# Use random.randint(0,x) to generate a random number
# Use num%2 == 0 to check is it is even number
# 
#     Define function: 3 pts
#     Invoke function: 1 pts
#     Total: 4 pts

# In[7]:


import random

# Define the function here
def countNo(x):
    even = 0
    odd = 0
    for i in range(1,x+1):
        num = random.randint(0,100)
        if num%2 == 0:
            even=even+1
        else:
            odd=odd+1
    return even,odd

# Display 100 random numbers
x=100
even,odd=countNo(x)
print(float(even/odd))

# Display 1000 random numbers
x=1000
even,odd=countNo(x)
print(float(even/odd))

# Display 10000 random numbers
x=10000
even,odd=countNo(x)
print(float(even/odd)) 


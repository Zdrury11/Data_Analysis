#!/usr/bin/env python
# coding: utf-8

# # CI280 Lab02 – List
# 
# Upload your answer to GitHub
# 
# Email the link to: jzhang@eastwest.edu
# 
# Name: _________________

# In[ ]:


## A. Show the output: ( 10 pts)


# In[1]:


# 1)
numbers = [50, 20, 10, 80, 10]
print(numbers)
print(numbers[2])

max_value = max(numbers)
max_index = numbers.index(max_value)
print('max =' ,max_value)
print( max_index)

min_value = min(numbers)
min_index = numbers.index(min_value)
print('min =' ,min_value)
print(min_index)

print('length =' ,len(numbers))
print('Element =' ,numbers[len(numbers)-1])


# In[2]:


# 2)
print() # line break
names=['Steven', 'Will', 'Alicia']
print(names)

print('--')
for name in names:
      print(name)
print('--')
index = 2
while index <len(names):
      print(names[index])
      index += 1


# In[3]:


# 3)
print() # line break
num1 = list(range(0,20, 5))
print(num1)

num2 = num1 * 3
print(num2)

index = 0
while index < len(num1):
    num1[index]= num1[index]*3
    index +=1
print(num1)

print(sum(num1))
print(sum(num1)/len(num1))


# In[4]:


# 4)
print() # line break
numbers = list(range(0,101,10))
print(numbers)

print(numbers[:5])
print(numbers[2:5])
print(numbers[7:])
print(numbers[-3:])


# In[5]:


# 5)
print() # line break
cities = ['Chicago', 'Paris']
print(cities)

city_index = cities.index('Paris')
print(city_index)

cities.insert(1, 'New York')
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)
          
cities.remove('New York')
print(cities)


# In[ ]:


# B. Write a program. ( 10 pts)
# The amounts daily sales of one week is stored in a list. 
# 1) Write a program that asks the user to enter a store’s sales for each day of the week. 
# 2) Display the sales for each week day. 
# 3) Display Sales summary: total sales, average sales, highest and lowest sales. (4 pts)


# In[12]:


# Ask user to enter a stores sales for each day of the week.

# variables used
total_sales = [0.0]*days
days_of_week = 7

# Compute
daily_sales = [0.0] * days
days_of_week = ['Sunday', 'Monday', 'Tuesday',  'Wednesday', 'Thursday', 'Friday','Saturday']

for 1 in range(7):
    daily_sales[i] = float(input("Enter the sales for" + days_of_week[i] + ': '))

print ('Weekly Sales')
print('--------')

for index in range(7):
    print(days_of_week [index], ': $', format(daily_sales[index], ',.2f'))

for number in daily_sales
total_sales






#User input
sun = float(input("Enter the sales for Sunday: "))
mon = float(input("Enter the sales for Monday: "))
tue = float(input("Enter the sales for Tuesday: "))
wed = float(input("Enter the sales for Wednesday: "))
thur = float(input("Enter the sales for Thursday: "))
fri = float(input("Enter the sales for Friday: "))
sat = float(input("Enter the sales for Saturday: "))
print("Weekly Sales")
print("----------")
print("Sunday: $", sun)
print("Monday: $", mon)
print("Tuesday: $", tue)
print("Wednesday: $", wed)
print("Thursday: $", thur)
print("Friday: $", fri)
print("Saturday: $", sat)
print()
print("Weekly Sales Summary")
print("--------")
print("Total sales: $", format(sun+mon+tue+wed+thur+fri+sat, '.2f'))
print("Average sales: $", format((sun+mon+tue+wed+thur+fri+sat)/7, '.2f'))
print("The highest sales is on Tuesday: $",daily_sales )
print("The lowest sales in on Sunday: $",)




# In[ ]:





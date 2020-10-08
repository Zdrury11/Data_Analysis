# Lab: 2
# Date: 10/8/2020
# Programmer: Zach Drury

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

# 4)
print() # line break
numbers = list(range(0,101,10))
print(numbers)

print(numbers[:5])
print(numbers[2:5])
print(numbers[7:])
print(numbers[-3:])

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







          



















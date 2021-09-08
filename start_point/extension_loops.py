# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for number in numbers:
    if number%2 == 0:
        print(number)


# 2. Print the difference between the largest and smallest value:

# I know this isn't right as there is no way of iknowing that the number i initiated smallest with is smaller than an existing one in the list??

smallest = 100
largest = 0
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(smallest)
print(largest)
diff_in_nums = largest - smallest
print(f'the difference between the largest and the smallest number in the list is {diff_in_nums}')

#other solution 

sorted = number.sort()
min_num = sorted[0]
max_num = sorted[-1]
print(max - min)

#other solution

largest_num = max(numbers)
smallest_num = min(numbers)

print(largest_num - smallest_num)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

result = False
index = 0
for number in numbers:
    if (number == 2 and numbers[index-1] == 2):
        result = True
    index +=1
print(result)    


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
found_6 = False
for number in numbers: 
    if number == 6:
        found_6 = True
    elif found_6:
        if number == 7:
            found_6 = False
    else:
        total += number

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


index = 0 
total = 0
for number in numbers:
    if number == 13 or numbers[index-1] == 13:
        pass
    else:
     total += number
    index += 1
print(total)






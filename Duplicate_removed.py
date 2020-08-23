# This programm removes duplicate numbers from
# list of numbers

#Here is a list of numbers stored in a declared
#variable, named numbers
numbers = [4, 3, 3, 2, 10, 1, 1, 5, 6, 6, 7, 6, 5, 5, 9, 4, 8, 3, 9]

#Creat an empty list to store new numbers excluding the duplicates
duplicate_removed = []

#iterate through numbers(list) to eradicate the duplicated numbers
for number in numbers:
    if number not in duplicate_removed:
        duplicate_removed.append(number)

print(duplicate_removed)
#>>[4, 3, 2, 10, 1, 5, 6, 7, 9, 8]

#To sort the output, after removing the duplicates are removed
#We Call sort on duplicate_removed
duplicate_removed.sort()
print(duplicate_removed)
#>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



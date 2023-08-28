# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for individual_number in numbers:
    if individual_number % 2 == 0:
        print(individual_number)

# 2. Print the difference between the largest and smallest value:
difference = max(numbers) - min (numbers)
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
def duplicates(numbers):
    for individual_number in range(len(numbers)-1):
        if numbers[individual_number] == numbers[individual_number+1]:
            return True
print(duplicates(numbers)) #circle back- see if there is a way to do this just for 2
#I will admit I did a bit of googling for this one, however I didn't just copy the first thing I saw & did actually break down the various parts

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
# Output: numbers = [1, 1] --> 2

def grand_total(input_numbers):
    running_total = 0
    for individual_number in input_numbers:
        running_total += individual_number
    return running_total
print(grand_total(numbers))




# needs to loop through the numbers
# needs to skip 6-7 --> how do I do this

# -can't just exclude 6s & 7s
# could add unless it is followed by a 6 or proceeded by a 7 --> would work in this case but not always



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 








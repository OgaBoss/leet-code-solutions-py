# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
def two_number_sum(array, target_sum):
    value = []

    # Write your code here.
    for num in array:
        possible_num = target_sum - num

        if num != possible_num and possible_num in array:
            value = [num, possible_num]

    return value

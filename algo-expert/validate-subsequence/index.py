# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the first one.
def is_valid_subsequence(array, sequence):
    # Write your code here
    count = 0

    for num in array:
        if count == len(sequence):
            break

        if num in sequence and sequence[count] == num:
            count += 1

    return len(sequence) == count

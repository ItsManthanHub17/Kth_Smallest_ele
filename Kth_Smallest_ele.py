def kth_smallest_el(lst, k):
    # Sort the list in ascending order
    lst.sort()
    # Return the kth smallest element (0-based index, so k-1)
    return lst[k - 1]


# Create a list of numbers
nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

# Print the original list
print("Original list:")
print(nums)

# Initialize 'k' to 1
k = 1

# Iterate from k = 1 to k = 10
for i in range(1, 11):
    # Print a message indicating the value of 'k'
    print("kth smallest element in the said list, when k =", k)

    # Call the kth_smallest_el function with 'k' and print the result
    print(kth_smallest_el(nums, k))

    # Increment 'k' by 1 for the next iteration
    k = k + 1

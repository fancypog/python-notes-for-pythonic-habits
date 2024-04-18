# 1. snake case

# python recommends snake case where lowercase words are connected by underscore
# like how you write the name of a function

# Examples: get_maximum_number, merge_sort

# 2. declare the expected types of input and output , which is good practice
def get_maximum_number(nums1: List[int]) -> int:
      # Check if the list is empty
    if not nums1:
        raise ValueError("The list is empty")
    
    # Initialize the maximum number to the first element of the list
    max_number = nums1[0]
    
    # Iterate through the list starting from the second element
    for num in nums1[1:]:
        # Update max_number if a larger number is found
        if num > max_number:
            max_number = num
    
    return max_number
  
  



# 2. use f strings 


# 3. Comparison operators "==" and "is" 
# "==" is for value comparison, while "is" is for identity comparison

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True, because the values of x and y are the same
print(x is y)  # False, because x and y are two different objects in memory







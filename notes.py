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
      
  # Example with documentation strings
  def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b

def greet(name: str) -> str:
    """
    Greet a person.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return "Hello, " + name + "!"

# Examples
print(add_numbers.__annotations__)
print(add_numbers(2, 3))  # Output: 5

print(greet.__annotations__)
print(greet("Alice"))  # Output: Hello, Alice!






# 2. use f strings for concatenation to make it plain and simple, easy to read, less to code
item = "book"
price = 19.99
quantity = 3

# Using f-string to concatenate variables within a string
invoice = f"You have purchased {quantity} {item}s at ${price:.2f} each. Total cost: ${price * quantity:.2f}."

print(invoice)



# 3. Comparison operators "==" and "is" 
# "==" is for value comparison, while "is" is for identity comparison

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True, because the values of x and y are the same
print(x is y)  # False, because x and y are two different objects in memory




# 4. Naming for classes follows the PascalCase convention
class MyClass:
    def __init__(self):
        pass







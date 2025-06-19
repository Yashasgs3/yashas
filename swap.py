# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display values before swapping
print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swapping the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Display values after swapping
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

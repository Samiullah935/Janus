# Add two numbers
num1 = 10
num2 = 5

# Calculate the sum
result = num1 + num2

# Print the result
print(f"The sum of {num1} and {num2} is: {result}")

# Alternative: Get input from user
print("\n--- Interactive Version ---")
try:
    user_num1 = float(input("Enter the first number: "))
    user_num2 = float(input("Enter the second number: "))
    user_result = user_num1 + user_num2
    print(f"The sum of {user_num1} and {user_num2} is: {user_result}")
except ValueError:
    print("Please enter valid numbers!")
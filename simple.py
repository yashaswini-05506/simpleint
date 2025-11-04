# Simple Interest Calculator with User Input

# Prompt the user for input
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (R) in %: "))
time = float(input("Enter the time period (T) in years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("\n--- Simple Interest Calculation ---")
print(f"Principal (P): ₹{principal}")
print(f"Rate (R): {rate}%")
print(f"Time (T): {time} years")
print(f"Simple Interest: ₹{simple_interest:.2f}")
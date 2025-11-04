# 📘 Simple Interest Calculator with Predefined Input

# Predefined values
principal = 15000      # Principal amount in currency units
rate = 6.5             # Annual interest rate in percent
time = 3               # Time period in years

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(" Simple Interest Calculation:")
print(f"Principal (P): {principal}")
print(f"Rate (R): {rate}%")
print(f"Time (T): {time} years")
print(f"Simple Interest: ₹{simple_interest:.2f}")
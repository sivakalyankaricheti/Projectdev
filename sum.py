import sys

# Step 1: Check if two arguments are provided
if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
    sys.exit(1)

try:
    # Step 2: Convert arguments to float (to support decimals)
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    # Step 3: Compute sum
    result = num1 + num2

    # Step 4: Print result
    print(result)

except ValueError:
    print("Error: Please provide valid numbers.")
    sys.exit(1)

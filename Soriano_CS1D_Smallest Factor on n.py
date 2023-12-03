def look_for_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater number than 2.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} is: {i}")
            break

# Get the user to enter a value
try:
    n = int(input("Enter a number, greater than or equal to 2: "))
    look_for_smallest_factor(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

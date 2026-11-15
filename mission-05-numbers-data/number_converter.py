"""Convert a positive decimal integer to binary and hexadecimal."""

number = int(input("Enter a positive whole number: "))
if number < 0:
    raise ValueError("Please enter a positive whole number.")
print("Binary:", bin(number)[2:])
print("Hexadecimal:", hex(number)[2:])

digits = input("Enter digits separated by spaces: ").split()

reversed_digits = digits[::-1]

result_number = "".join(reversed_digits)
print(result_number)

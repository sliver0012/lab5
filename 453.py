numbers = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))
squares = [num ** 2 for num in numbers]
print(squares)
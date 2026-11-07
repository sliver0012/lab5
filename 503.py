def roman_to_decimal(roman_str):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    decimal_value = 0
    length = len(roman_str)
    
    for i in range(length):
        current_val = roman_map[roman_str[i]]
        if i + 1 < length and current_val < roman_map[roman_str[i + 1]]:
            decimal_value -= current_val
        else:
            decimal_value += current_val
            
    return decimal_value

user_input = input("Enter a Roman numeral: ").strip().upper()
result = roman_to_decimal(user_input)

print(result)

def calculate_sum(input_string):  # Function define garne jasma input_string lincha
    # Input string bata curly braces hatayera number extract garne
    cleaned_string = input_string.strip('{}')  # Curly braces hatauna strip() use gareko

    # String lai comma le split garera numbers ko list banaucha
    number_list = cleaned_string.split(',')  # Comma le split garera numbers ko list banaucha

    # Sabai elements lai integer ma convert garera sum calculate garne
    total_sum = sum(int(num.strip()) for num in number_list)  # Strip() le whitespace hataera integer ma convert garne

    return total_sum  # Final sum return garne

# User bata input liene
user_input = input("Enter the numbers in the format {6, 2, 15}: ")  # User lai prompt garera input liene

# Remove any surrounding quotes from the input
user_input = user_input.strip('"\'')  # Remove both double and single quotes if they exist

# Function call garne ra result store garne
result = calculate_sum(user_input)  # Function lai call garne ra result store garne

# Result print garne
print(f"The sum is: {result}")  # Result print garne

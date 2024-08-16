def mutate_string(string, position, character):
    # Convert the string to a list to make it mutable
    string_list = list(string)  # String lai list ma convert garne

    # Change the character at the specified position
    string_list[position] = character  # List ma specified position ma character update garne

    # Join the list back into a string
    mutated_string = ''.join(string_list)  # List lai join garera string banaucha

    return mutated_string  # Modified string return garne

# Input lina
input_string = input("Enter the string: ")  # User bata string input lina

# Position ra character alag-alag input lina
position = int(input("Enter the position (index) start with 0 as 1 : "))  # Position lai integer ma convert garne
character = input("Enter the character to insert: ")  # Character input lina

# Function call garne ra result print garne
result = mutate_string(input_string, position, character)  # Function lai call garne
print(result)  # Result print garne

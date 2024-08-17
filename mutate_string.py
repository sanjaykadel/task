def mutate_string(string, position, character):
    # String lai list ma convert garne
    string_list = list(string)  

    # List ma specified position ma character update garne
    string_list[position] = character 

    # List lai join garera string banaucha
    mutated_string = ''.join(string_list)  

    return mutated_string  # Modified string return garne

# Input lina
input_string = input("Enter the string: ")  # User bata string input lina
position, character = input("Enter the position and character separated by space: ").split()  # Position ra character input lina
position = int(position)  # Position lai integer ma convert garne

# Function call garne ra result print garne
result = mutate_string(input_string, position, character)  # Function lai call garne
print(result)  # Result print garne

# Number ko list define garne
numbers = [2, 4, 6, 8, 10]  # Yo given numbers ko list ho

# Pair milaye ki namilaye vanera check garna flag rakheko
pair_found = False  # Yo flag use garera check garne ki pair milcha ki milchaena

# Outer loop sabai numbers ko lagi iterate garna
for i in range(len(numbers)):  # Loop first number dekhi last number samma jancha
    # Inner loop current number sanga arko sabai numbers ko pair banaucha
    for j in range(i, len(numbers)):  # Current index bata sabai numbers lai loop garchha
        # Check garne ki pair ko sum 16 cha ki chaina
        if numbers[i] + numbers[j] == 16:  # Condition check garne ki sum 16 cha ki chaina
            # Pair valid bhaye print garne
            print(f"Pair found: {numbers[i]} + {numbers[j]}")  # 16 sum bhaye pair print garne
            pair_found = True  # Flag true set garne kinaki pair milisakyo

# Sabai loop sakisake pachi check garne ki kunai pair nai milena ki kya ho
if not pair_found:  # Flag still False cha bhane, kunai pair milena
    print("No pair found.")  # User lai inform garne ki pair milena

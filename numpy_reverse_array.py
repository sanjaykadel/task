import numpy as np  # NumPy module import garne

# User input space separated numbers ko form ma liene
print(" enter the list :")
arr = input().split()  # Input split garera list banaucha

# List lai float type ko NumPy array ma convert garne
arr = np.array(arr, float)  # List lai float array ma change garne

# Array lai reverse garne
reversed_arr = arr[::-1]  # Reverse garnu ko lagi slicing use gareko

# Reverse bhayeko array print garne
print(reversed_arr)  # Final reversed array display garne

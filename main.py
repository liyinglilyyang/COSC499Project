from factorial import calculate_factorial
from max import calculate_max
from average import calculate_average
from factorial import calculate_factorial
from findMin import calculate_min

def create_list():
    a_list = []
    for i in range(9):
        x = a_list.append(int(input("Please enter an integer: ")))
    return a_list
              
a_list = create_list()
print("The minimum number is: ", calculate_min(a_list))

oddEven_list()
calculate_average()
calculate_max()
calculate_factorial()

# Average reviewed by: Jason
# Max reviewed by: Karim
# Min reviewed by: Amneet
# Factorial reviewed by: Karim
# Odd/Even reviewed by : Lily

from max import calculate_max
from average import calculate_average
def create_list():
    a_list = []
    for i in range(9):
        x = a_list.append(int(input("Please enter an integer: ")))
              
create_list()


def oddEven_list():
    number = int(input("Enter a number: "))  
    if (number% 2) == 0:  
        print("Even")  
    else:  
        print("Odd")

oddEven_list()
calculate_average()
calculate_max()
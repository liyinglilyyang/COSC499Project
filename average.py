def calculate_average():
    a_list = []
    for i in range(9):
        x = a_list.append(int(input("Please enter an integer: ")))
    Sum = float(sum(a_list))
    average = Sum/float((len(a_list)))
    print()
    print("The average is:", average)
    print("The numbers greater that the average are:")
    for i in range(len(a_list)):
        if a_list[i] > average:
            print(a_list[i] , end = "  ")
    print()
calculate_average()
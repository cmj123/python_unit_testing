# Define the function to be tested
def avg(*list_numbers:float) -> float:
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num 
        else:
            raise TypeError("Wrong input data. Please make sure that everything is a number")

    return total/len(list_numbers)

# print(avg(1,2,3,4,5,"hi"))
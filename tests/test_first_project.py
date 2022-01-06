# Define the function to be tested
def avg(*list_numbers):
    total = 0
    for num in list_numbers:
        total += num 

    return total/len(list_numbers)

print(avg(1,2,3,4,5))
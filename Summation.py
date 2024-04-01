#Create a Function that Calculate the sum of all the input number
def main():
    x = get_number()
    print(f'The Summation of the Numbers is: {x}')

#Create the Get number function
def get_number(*n):
    n = map(int, input('Enter Numbers: ').split(","))
    total_sum = 0
    for x in n:
      total_sum += x
    return total_sum

main()
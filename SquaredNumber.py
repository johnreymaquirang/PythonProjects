#Create a Function that multiplies the number to itself
def squared():
    while True:
      try:
        n = int(input('Enter a Number: '))
      except ValueError:
        print('Invalid Number')
      else:
        break
    x = n*n
    print('The Squared of', n, f'is {x}')
    return n

squared()
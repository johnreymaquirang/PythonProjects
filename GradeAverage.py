def average():
    while True:
        try:
            first_grade = int(input('Enter Math Grade: '))
            second_grade = int(input('Enter Science Grade: '))
            third_grade = int(input('Enter English Grade: '))
            Average = (first_grade + second_grade + third_grade)/3
            remarks(Average)
            break
        except ValueError:
            print('Invalid Input')

def remarks(ave):
    if ave > 100 or ave <= 50:
      print('Invalid Grade')
    elif ave >= 98 :
      print(f'Your Grade is {ave :.2f} Remarks: With Highest Honors.')
    elif ave >= 95:
      print(f'Your Grade is {ave :.2f} Remarks: With High Honors.')
    elif ave >= 90:
      print(f'Your Grade is {ave :.2f} Remarks: With Honors.')
    elif ave >= 75:
      print(f'Your Grade is {ave :.2f} Remarks: Passed.')
    else:
      print(f'Your Grade is {ave :.2f} Remarks: Failed.')

average()
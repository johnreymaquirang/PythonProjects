def main():
    weight = float(input('Enter Your Weight (kg): '))
    height = float(input('Enter Your Height (m) : '))
    body_mass_index(weight, height)

def body_mass_index(w, h):
  bmi = w/(h*h)
  print(f'Your Body Mass Index (BMI) is {bmi:.2f}')
  bmi_category(bmi)

def bmi_category(x):
  if x < 18.5:
    print('You Are Underweight Category')
  elif 18.5 <= x <= 24.9:
    print('You Are Healthy Weight Category')
  elif 25 <= x <= 29.9:
    print('You Are  Overweight Category')
  elif 30 <= x <= 34.9:
    print('You Are Obese Category')
  elif 35 <= x <= 39.9:
    print('You Are Severely Obese Category')
  elif x <= 40:
    print('You Are Morbidly Obese Category')

main()
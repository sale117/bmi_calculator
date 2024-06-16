height = float(input('Please enter your height in meters as a decimal number (e.g., 1.75): '))
weight = int(input('Please enter your weight in kilograms: '))
bmi = round(weight / height ** 2)
print(f'Your BMI is {bmi}')
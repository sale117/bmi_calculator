# BMI Calculator Script

This script calculates your Body Mass Index (BMI) based on your height and weight inputs.

## Detailed Steps

### Input Collection:
The script asks the user to enter their height in meters and their weight in kilograms using the input function.  
`height = float(input('Please enter your height in meters as a decimal number (e.g., 1.75): ')`  
`weight = int(input('Please enter your weight in kilograms: '))`

### BMI Calculation:
The BMI is calculated using the formula _weight / (height ** 2)_, which is weight divided by the square of the height.
The result is rounded to the nearest whole number using the round function.  
`bmi = round(weight_int / height_int ** 2)`

### Output:
The final BMI value is printed to the console.  
`print(f'Your BMI is: {bmi}')`
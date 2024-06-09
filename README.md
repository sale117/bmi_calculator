# BMI Calculator Script

This script calculates your Body Mass Index (BMI) based on your height and weight inputs.

## Detailed Steps

### Input Collection:
The script asks the user to enter their height in meters and their weight in kilograms using the input function.  
`height = input('Please enter your height in meters as a decimal number (e.g., 1.75): ')`  
`weight = input('Please enter your weight in kilograms: ')`

### Conversion:
Height is converted from a string to a float using float(height). This allows for decimal values, which is necessary for height.
Weight is converted from a string to an integer using int(weight). This assumes that the weight will be entered as a whole number.  
`height_int = float(height)`  
`weight_int = int(weight)`

### BMI Calculation:
The BMI is calculated using the formula _weight / (height ** 2)_, which is weight divided by the square of the height.
The result is rounded to the nearest whole number using the round function.  
`bmi = round(weight_int / height_int ** 2)`

### Conversion to String:
The resulting BMI is converted to a string so that it can be concatenated with other strings for printing.  
`bmi_str = str(bmi)`

### Output:
The final BMI value is printed to the console.  
`print('Your BMI is: ' + bmi_str)`

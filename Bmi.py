print("\t\t\t Wellcome To Matric Bmi Calclutor")
print("\t\t\t   By Md Imran Hossen")

height = float(input("Enter Your Height in Meter :"))
weight = float(input("Enter Your Weight in kg :"))
bmi = weight / (height * height)
if bmi <= 18.5:
    print('Your BMI is', bmi, 'which means you are underweight.')


elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi, 'which means you are normal.')


elif bmi > 25 and bmi < 30:
    print('your BMI is', bmi, 'overweight.')


elif bmi > 30:
    print('Your BMI is', bmi, 'which means you are obese.')

else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
          'and decimals were asked.')

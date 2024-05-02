
## Global Variable(s)
app = 0

## Function(s)
def BMI(Height,Weight):
    result = 0.0
    result = Weight/pow(Height,2)
    return result

def BMI_Menu():
    print("Enter the Height in metres, and Weight in kilograms, in this form: a,b \n")
    bmilist = input()
    print("\nEntered information = ",bmilist.split,"\n")
    print(round(BMI(float(bmilist[0]),float(bmilist[1])),2),"\n")
    return

def AVG_Menu():
    print("\nEnter the numbers in this form: a,b,c,d\n")
    numlist = input()
    numlist = numlist.split
    print(numlist)
    return

while(app == 0):
    print("\nEnter 0 to start a program that calculates BMI\n", "\nEnter 1 to start a program that calculates the average of 4 numbers\n")
    app = input()

    if float(app) == 0:
        BMI_Menu()
        app = 0
        continue
    elif float(app) == 1:
        AVG_Menu()
        app = 0
        continue
    else:
        break

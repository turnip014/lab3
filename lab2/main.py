## Global Variable(s)
app = 0

## Function(s)
def BMI(Height,Weight):
    result = 0.0
    result = Weight/pow(Height,2)
    return result

def Display_Main_Menu():
    print('\nWhat is the height in metres? ')
    Height = input()
    print('\nWhat is the weight in kilograms? ')
    Weight = input()
    print (round (BMI(float(Height),float(Weight)),2),"\n")

def Calc_Avg():
    return

while(app == 0):
    print("Enter 0 to start a program that calculates BMI")
    app = input()

    if float(app) == 0:
        Display_Main_Menu()
        app = 0
        continue
    elif float(app) !=0 :
        break

import main as ma

bmi = ma.BMI_Menu()
classweight = 0

if bmi == 25:
    classweight = 0
elif bmi < 25:
    classweight = -1
elif bmi > 25:
    classweight = 1

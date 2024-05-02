import pandas as pda
import openpyxl

## Defining function(s)

def function():

    try: 
        pda.read_excel("PrestigeMall.xlsx") # Sheet to be accessed
        print("Currently viewing Excel sheet...\n\n\n\n",)

    except:
        print("Invalid")

    excel = pda.read_excel("PrestigeMall.xlsx")
    indexed = excel.set_index("Job sector") # Column to be indexed
    print(indexed.loc['IT/Eng'], "\n\n\n") # Var to be filtered for
    return

while (1):
    function() # Main function using pandas
    break
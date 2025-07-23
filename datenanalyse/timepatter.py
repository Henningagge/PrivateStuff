#was will ich analysiren ich will ein fenster was mir sagt an welchen wochen tag besonder vile gekauft wird
# ich will wissen welche monate umsatz stark sind
from getPostdata import *  

def weekday():
    monday = 0.0
    thuesday = 0.0
    wendsday = 0.0
    thurdsday = 0.0
    friday = 0.0
    saturday = 0.0
    sunday = 0.0
    dataarr = callForData()
    
    print(dataarr)
    for entry in dataarr:
        print("time")

weekday()  


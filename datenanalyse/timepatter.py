#was will ich analysiren ich will ein fenster was mir sagt an welchen wochen tag besonder vile gekauft wird
# ich will wissen welche monate umsatz stark sind
from getPostdata import *  
import re
from datetime import date
import calendar

def weekday():
    monday = 0.00
    tuesday = 0.00
    wednesday = 0.00
    thursday = 0.00
    friday = 0.00
    saturday = 0.00
    sunday = 0.00
    dataarr = callForData()
    
    print(dataarr)
    for entry in dataarr:
      if 'bestelldatum' in entry:
        day_name = getWeekdayFromDate(entry['bestelldatum'])
        day_name_lower = day_name.lower()
        buyamount = float(entry['preis'])
         
        if day_name_lower == 'monday':
                monday += buyamount
        elif day_name_lower == 'tuesday':
                tuesday += buyamount
        elif day_name_lower == 'wednesday': 
                wednesday += buyamount
        elif day_name_lower == 'thursday': 
                thursday += buyamount
        elif day_name_lower == 'friday':
                friday += buyamount
        elif day_name_lower == 'saturday':
                saturday += buyamount
        elif day_name_lower == 'sunday':
                sunday += buyamount
        else:
                print(f"Warnung: Unbekannter Wochentag gefunden: '{day_name}' in Eintrag: {entry}")
      else:
            print(f"Warnung: etwas nicht in Eintrag gefunden: {entry}")
    monday = round(monday, 2)
    tuesday = round(tuesday, 2)
    wednesday = round(wednesday, 2)
    thursday = round(thursday, 2)
    friday = round(friday, 2)
    saturday = round(saturday, 2)
    sunday = round(sunday, 2)
    print(monday, tuesday, wednesday, thursday, friday, saturday, sunday)
def getWeekdayFromDate(datum):
        day = calendar.day_name[datum.weekday()]
        
        return day
weekday()  


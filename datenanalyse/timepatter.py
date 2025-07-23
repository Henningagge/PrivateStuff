#was will ich analysiren ich will ein fenster was mir sagt an welchen wochen tag besonder vile gekauft wird
# ich will wissen welche monate umsatz stark sind
from getPostdata import *  
import re
def weekday():
    monday = 0.0
    tuesday = 0.0
    wednesday = 0.0
    thursday = 0.0
    friday = 0.0
    saturday = 0.0
    sunday = 0.0
    dataarr = callForData()
    
    print(dataarr)
    for entry in dataarr:
      if 'Wochentag' in entry:
        day_name = entry['Wochentag']
        day_name_lower = day_name.lower()
        buyamount = entry['Kaufmenge']
            
        if day_name_lower == 'montag':
                monday += buyamount
        elif day_name_lower == 'dienstag':
                tuesday += buyamount
        elif day_name_lower == 'mittwoch': 
                wednesday += buyamount
        elif day_name_lower == 'donnerstag': 
                thursday += buyamount
        elif day_name_lower == 'freitag':
                friday += buyamount
        elif day_name_lower == 'samstag':
                saturday += buyamount
        elif day_name_lower == 'sonntag':
                sunday += buyamount
        else:
                print(f"Warnung: Unbekannter Wochentag gefunden: '{day_name}' in Eintrag: {entry}")
    else:
            print(f"Warnung: Schlüssel 'Wochentag' nicht in Eintrag gefunden: {entry}")
    print(monday, tuesday, wednesday, thursday, friday, saturday, sunday)
weekday()  


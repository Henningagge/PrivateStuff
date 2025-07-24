import pymysql
import pymysql.cursors
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Password123!',
    'db': 'customerdata',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def writedata(conn):
    try: 
        with conn.cursor() as cursor:
            sql = "INSERT INTO `timepattern` (`Datum`,`Wochentag`,`Monat`,`Kaufmenge`) VALUES (%s, %s, %s, %s)"
            data_to_insert = ( '2023-10-26', 'Donnerstag', 'Oktober', 100)
            cursor.execute(sql, data_to_insert)


        conn.commit()
        print("Daten erfolgreich geschrieben.")
    except pymysql.Error as e:
        print(f"fehler {e}")
def readdata(conn):
    dataarr = []
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `Kundenbestellungen`"
            cursor.execute(sql)

            rows = cursor.fetchall()
            print("--- Daten aus der timepattern Tabelle ---")
            for row in rows:
                dataarr.append(row)
                print(row)
            
            return dataarr
    except pymysql.Error as e:
        print(f"fehler {e}")
    


    


if __name__ == "__main__":
    conn = None
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("Verbindung zur Datenbank hergestellt.")
        writedata(conn)
        readdata(conn)
    except pymysql.Error as e:
        print(f"Datenbankverbindungsfehler: {e}")
    finally:
        
        if conn:
            conn.close()
            print("Verbindung zur Datenbank geschlossen.")
def callForData():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("Verbindung zur Datenbank hergestellt.")
        
        return readdata(conn)
    except pymysql.Error as e:
        print(f"Datenbankverbindungsfehler: {e}")
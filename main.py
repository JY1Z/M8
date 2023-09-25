import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jyz',
         password='123456',
         autocommit=True
         )

def icao(icao):
  #sql = "SELECT name, iso_country FROM airport"
  #sql += " WHERE ident = '" + icao + "'"
  sql = "SELECT name, iso_country FROM airport WHERE ident ='"+ icao +"'"
  print(sql)
  cursor = connection.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  for n in result:
    print(n)
  return

icao("00AR")


def enter_code(code):
    sql = "SELECT name, type FROM airport WHERE iso_country ='"+ code +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    for i in result:
        if i[1] == "small_airport":
            a1 = a1 + 1
        if i[1] == "heliport":
            a2 = a2 + 1
        if i[1] == "medium_airport":
            a3 = a3 + 1
        if i[1] == "large_airport":
            a4 = a4 + 1
        if i[1] == "closed":
            a5 = a5 + 1
    print(f"{code} has {a1} small airport, "
          f"{a2} heliport,{a3} medium airport,"
          f"{a4} large_airport, {a5} closed")
    return
enter_code("FI")


from geopy.distance import geodesic
def distance(icao1,icao2):
    sql1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='"+ icao1 +"'"
    cursor = connection.cursor()
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    sql2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='"+ icao2 +"'"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for n in result1:
        d1 = n
    for n in result2:
        d2 = n
    D = geodesic(d1, d2).miles
    DKM = (D * 1609.34)/1000
    print(f"The distance between the two airports is {DKM:.2f} kilometers.")
    return

distance("ZSCN","ZYJZ")
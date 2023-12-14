number_as_string = input("Geben Sie eine Ganzzahl ein: ")

try:
    number_as_int = int(number_as_string)

    print("Die Zahl lautet:", number_as_int)
except ValueError:
    print("Das war keine Ganzzahl")
except:
    print("Hier ist etwas Anderes falsch gelaufen.")
finally:
    print("Dieser Teil wird auf jeden Fall ausgeführt.")



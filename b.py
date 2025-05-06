# sierra's first little uwu program: a temperature calculator

print("this is a temperature conversion program")

loop = True
while loop:
    a = input("please type in your current measurement: ").lower()

    # FAHRENHEIT
    if a == str("fahrenheit") or a == str("f"):
        temp = float(input("please input your temperature value: "))
        if type(temp) == float:
            b = input("please type in your desired new measurement: ").lower()
            if b == str("celsius") or b == str("c"):
                o1 = float(temp) - 32
                r1 = o1 * 5 / 9
                print(f"your temperature in the new measurement is {round(r1, 2)}°c")
                print("")
            elif b == str("kelvin") or b == str("k"):
                o1 = float(temp) - 32
                r1 = o1 * 5 / 9 - 273.15
                print(f"your temperature in the new measurement is {round(r1, 2)}°k")
                print("")
            else:
                print("invalid new measurement")
                print("")
        else:
            print("invalid temperature value")
            print("")

    # CELSIUS
    elif a == str("celsius") or a == str("c"):
        temp = float(input("please input your temperature value: "))
        if type(temp) == float:
            b = input("please type in your desired new measurement: ").lower()
            if b == str("fahrenheit") or b == str("f"):
                o1 = 9 / 5
                r1 = float(temp) * o1 + 32
                print(f"your temperature in the new measurement is {round(r1, 2)}°f")
                print("")
            elif b == str("kelvin") or b == str("k"):
                r1 = float(temp) + 273.15
                print(f"your temperature in the new measurement is {round(r1, 2)}°k")
                print("")
            else:
                print("invalid new measurement")
                print("")
        else:
            print("invalid temperature value")
            print("")

    # KELVIN
    elif a == str("kelvin") or a == str("k"):
        temp = float(input("please input your temperature value: "))
        if type(temp) == float:
            b = input("please type in your desired new measurement: ").lower()
            if b == str("fahrenheit") or b == str("f"):
                o1 = float(temp) - 273.15
                r1 = o1 * 9 / 5 + 32
                print(f"your temperature in the new measurement is {round(r1, 2)}°f")
                print("")
            elif b == str("celsius") or b == str("c"):
                r1 = float(temp) - 273.15
                print(f"your temperature in the new measurement is {round(r1, 2)}°c")
                print("")
            else:
                print("invalid new measurement")
                print("")
        else:
            print("invalid temperature value")
            print("")
    else:
        print("invalid temperature measurement")
        print("")

try:
    num = float(input("cube root of: "))

    def cuberoot(number):
        if number >= 0:
            return number ** (1 / 3)
        else:
            return -abs(number) ** (1 / 3)

    print(cuberoot(num))
except:
    print("Please give a valid number")

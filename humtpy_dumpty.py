def Humpty_Dumpty(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Humpty_Dumpty"
    elif number % 3 == 0:
        return "Humpty"
    elif number % 5 == 0:
        return "Dumpty"
    else:
        return number


num = int(input("Enter a number: "))
result = Humpty_Dumpty(num)
print(result)


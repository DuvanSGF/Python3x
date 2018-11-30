try:
    meaning = 42
    print(meaning/0)
    print("The meaning of life")
except(ValueError, TypeError):
    print("ValueError or TypeError ocurred")
except ZeroDivisionError:
    print("Divided by zero")
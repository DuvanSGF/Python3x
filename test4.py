try:
    print(1)
    print(20/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)

# Other Exercise

try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)

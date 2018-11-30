pairs = {1: "Apple",
         "Orange": [2,3,4],
         True: False,
         None: "True",
         }
print(pairs.get("Orange"))
print(pairs.get(True))
print(pairs.get(12345, "not in dictionary"))

fib = {1: 1,2: 1,3: 2,4: 3}
print(fib.get(4,0) + fib.get(7,5))

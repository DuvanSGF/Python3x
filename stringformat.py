nums = [4, 5, 6]
msg = "Numbers: {0} {1} {0}". format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra","cad"))

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)
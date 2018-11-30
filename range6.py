def func(x):
    res = 0
    for i in range(x):
     res += i
    return res

print(func(4))
##Second
def print_nums(x):
 for i in range(x):
  print(i)
  return
print_nums(10)

def print_double(x):
    print(2*x)
print_double(3)

def shout(word):
    """
    Print a world with an
    exclamation mark following
    it.
    """
    print(word + "!")
shout("spam")

#Square root problem


def SquareRoot(X):
  Root = X
  Temp = 0
  while Root != Temp:
    Temp = Root
    Root = 0.5*(Root+(X/Root))
  return Root

X = int(input("Enter square number: "))
Output = SquareRoot(X)
print("The root of {} is {}".format(X,Output))
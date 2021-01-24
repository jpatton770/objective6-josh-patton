


def Interest(Value,Rate):
  Rate = Rate / 100
  print(Rate)
  counter = 0
  while True:
    counter += 1
    Value = Value + (Value*Rate)
    print("After {} years, your new balance is {}".format(counter,Value)

Value = int(input("Enter amount: "))
Rate = int(input("Enter intrest rate: "))
Interest(Value,Rate)
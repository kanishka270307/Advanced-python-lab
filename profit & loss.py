sp = int(input("enter amount"))
cp = int(input("enter amount"))
if sp > cp:
    profit = sp-cp
    print("profit",profit)
elif cp > sp:
    loss = cp-sp
    print("loss",loss)
else: print ("no profit,no loss")
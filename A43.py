total_cost=float(input("What is the total cost?"))
money_given=float(input("What was the money given?"))
change=float(money_given-total_cost)
print("Change: ",str(change))
dollars=change-change%1

change=dollars
quarters=change-change%0.25
change=quarters
dimes=float(change-change%0.1)
change=dimes
nickels=float(change-change%0.05)
change=nickels
pennie=change-change%0.01
print("Dollar(s): ",str(dollars))
print("Quarters(s): ",str(quarters))
print("Dime(s): ",str(dimes))
print("Pennie(s): ",str(pennie))

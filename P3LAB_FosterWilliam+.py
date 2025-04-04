# William Foster
# 3-21-2025
# P3LAB
# a program that breaks your dollars
money = float(input("Enter the amount of money as a float: "))
cent = int(money * 100)
dollar = cent // 100
cent %= 100
quarter = cent // 25
cent %= 25
dime = cent // 10
cent %= 10
nickel = cent // 5
cent %= 5
penny = cent
if dollar > 0: print(f"{dollar} Dollar{'s' if dollar > 1 else ''}")
if quarter > 0: print(f"{quarter} Quarter{'s' if quarter > 1 else ''}")
if dime > 0: print(f"{dime} Dime{'s' if dime > 1 else ''}")
if penny > 0: print(f"{penny} Penn{'ies' if penny > 1 else 'y'}")
if money == 0: print("No change")
# William Foster
# 4-27-2025
# P5LAB
# A program that breaks your dollars

def make_change(change):
    cent = int(change * 100)
    dollar = cent // 100
    cent %= 100
    quarter = cent // 25
    cent %= 25
    dime = cent // 10
    cent %= 10
    nickel = cent // 5
    cent %= 5
    penny = cent

    if dollar > 0:
        print(f"{dollar} Dollar{'s' if dollar > 1 else ''}")
    if quarter > 0:
        print(f"{quarter} Quarter{'s' if quarter > 1 else ''}")
    if dime > 0:
        print(f"{dime} Dime{'s' if dime > 1 else ''}")
    if nickel > 0:
        print(f"{nickel} Nickel{'s' if nickel > 1 else ''}")
    if penny > 0:
        print(f"{penny} Penn{'ies' if penny > 1 else 'y'}")
    if change == 0:
        print("No change")

owed = 76.48
print(f"You owe ${owed}")
money = float(input("How much cash will you put in the self-checkout? "))
change = money - owed
print(f"Change is: ${change:.2f}")

make_change(change)

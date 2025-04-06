# William Foster
# 4-6-2025
# P4LAB2
# loop if yes
user_text = "yes"

while user_text.lower() == "yes":
    integer = int(input("Enter an integer: "))
    
    if integer >= 0:
        for i in range(1, 13):
            print(integer, "*", i, "=", integer * i)
    else:
        print("Negative numbers are not allowed.")

    user_text = input("Would you like to run the program again? ")

print("Exiting program...")

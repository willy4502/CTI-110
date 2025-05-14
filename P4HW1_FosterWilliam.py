# William Foster
# 4-14-2025
# P4HW1
# .

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("\ninvalid Score entered!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i+1} again:")

lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print("\n--------------Results-------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")
# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Grades

#Grade system A=90 or above, B=80-90, C=70-80, D=60-70, F=below 60

# ask usr for test score

score = input("Ener your test score (out of 100): \n")

# cast

score = int(score)

if score >= 90:
    print("A")
elif score >=80 and score < 90:
    print("B")
elif score >=70 and score < 80:
    print("C")
elif score >=60 and score < 70:
    print("D")
else:
    print("F. You're a FAILURE!")

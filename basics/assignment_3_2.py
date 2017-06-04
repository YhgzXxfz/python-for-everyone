score = raw_input("Enter Score: ")
try :
    s = float(score)
except :
    print "Input should be between 0.0 and 1.0 !"
    exit()


if s >= 0.9 :
    grade = "A"
elif s >= 0.8 :
    grade = "B"
elif s >= 0.7 :
    grade = "C"
elif s >= 0.6 :
    grade = "D"
else :
    grade = "F"

print grade

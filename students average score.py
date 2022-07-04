
#Calculating student's grades using their average score

print("Enter marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

totalScore = markOne+markTwo+markThree+markFour+markFive
average = totalScore/5

if average>=70 and average<=100:
    print("Your Grade is A")
elif average>=60 and average<69:
    print("Your Grade is B")
elif average>=50 and average<59:
    print("Your Grade is C")
elif average>=40 and average<49:
    print("Your Grade is D")
elif average>=0 and average<39:
    print("Your Grade is E")
else:
    print("Invalid Input!")
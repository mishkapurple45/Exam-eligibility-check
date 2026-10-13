#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a 
# medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75,
#  then allowed; otherwise, not allowed.

medical=input("Do you have a medical cause?")
if medical=="y":
    print("You can take this exam.")
else:
    a=int(input("What is your attendance?"))
    if a>75:
        print("You can take this exam")
    else:
        print("You can't take this exam")
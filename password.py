password="123shadow"
attempts=0
while attempts<3:
    guess=input("enter your password:")
    if guess==password:
       print("correct password")
       break

    else:
       print("incorrect password")
       attempts+=1
if attempts==3:
    print("system close")

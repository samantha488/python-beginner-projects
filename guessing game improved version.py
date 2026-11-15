import random

while True:
    print("welcome to the game !")
    difficulty=input("what difficulty are you choosing easy?medium? or hard?:").lower()

    if difficulty=="easy":
        secret_number=random.randint(1,10)
        lives=7

    elif difficulty=="medium":
        secret_number=random.randint(1,20)
        lives=5

    elif difficulty=="hard":
        secret_number=random.randint(1,100)
        lives=3

    else:
        print("invalid difficulty")
        continue

    while lives>0:
         guess=int(input("guess anumber and enter here:"))
        
         if guess==secret_number:
              print("hurray you got it in ",lives,"attempts")
         elif guess>secret_number:
              lives-=1
              print("too high try lower,lives:",lives)
         else:
              lives-=1
              print("too lower try higher,lives",lives)
        
    else:
         print("game over!")
         print("the secret number was",secret_number)
        
    play_again=input("do you wanna play again yes/no?").lower()
        
    if play_again!="yes":
         print("thanks for playing")
         break
                 
                 
        
        
        
                
                
               
        
            
        



    

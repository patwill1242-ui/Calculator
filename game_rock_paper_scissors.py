import random


sprite_rock_rock="""
    _______                _______
---'   ____)              (____   '---
      (_____)            (_____)
      (_____)            (_____)
      (____)              (____)
---.__(___)                (___)__.---

"""
sprite_rock_paper="""
    _______                 _______
---'   ____)           ____(____    '---
      (_____)         (______
      (_____)        (_______
      (____)          (_______
---.__(___)             (__________.---

"""
sprite_rock_scissors="""
    _______                _______
---'   ____)          ____(____   '---
      (_____)        (______
      (_____)       (__________
      (____)              (____)
---.__(___)                (___)__.---

"""
sprite_paper_rock="""
     _______               _______
---'    ____)____         (____   '---
           ______)       (_____)
          _______)       (_____)
         _______)         (____)
---.__________)            (___)__.---

"""
sprite_paper_paper="""
     _______                _______
---'    ____)____      ____(____    '---
           ______)    (______
          _______)   (_______
         _______)     (_______
---.__________)         (__________.---

"""
sprite_paper_scissors="""
     _______               _______
---'    ____)____     ____(____   '---
           ______)   (______
          _______)  (__________
         _______)         (____)
---.__________)            (___)__.---

"""
sprite_scissors_rock="""
    _______                _______
---'   ____)____          (____   '---
          ______)        (_____)
       __________)       (_____)
      (____)              (____)
---.__(___)                (___)__.---

"""
sprite_scissors_paper="""
    _______                 _______
---'   ____)____       ____(____    '---
          ______)     (______
       __________)   (_______
      (____)          (_______
---.__(___)             (__________.---

"""
sprite_scissors_scissors="""
    _______                _______
---'   ____)____      ____(____   '---
          ______)    (______
       __________)  (__________
      (____)              (____)
---.__(___)                (___)__.---

"""

all_posibilities=[ 
    {"draw":sprite_rock_rock,"value1":0,"value2":0,"result":"DRAW"},
    {"draw":sprite_rock_paper,"value1":0,"value2":1,"result":"YOU LOSE"},
    {"draw":sprite_rock_scissors,"value1":0,"value2":2,"result":"YOU WIN"},
    {"draw":sprite_paper_rock,"value1":1,"value2":0,"result":"YOU WIN"},
    {"draw":sprite_paper_paper,"value1":1,"value2":1,"result":"DRAW"},
    {"draw":sprite_paper_scissors,"value1":1,"value2":2,"result":"YOU LOSE"},
    {"draw":sprite_scissors_rock,"value1":2,"value2":0,"result":"YOU LOSE"},
    {"draw":sprite_scissors_paper,"value1":2,"value2":1,"result":"YOU WIN"},
    {"draw":sprite_scissors_scissors,"value1":2,"value2":2,"result":"DRAW"}
]

score=0

while True:
    while True:
        try:
            choose=int(input("Choose your move: 0:rock 1:paper 2:scissors "))
           
            if choose in [0,1,2]:
                break
            else:
                print("your choose is not valid, please try again")
            
        except ValueError:
                print("oops! That was no a valid number")
    
    pc_choose=random.randint(0,2)

    for x in all_posibilities:
        if x["value1"] == choose and x["value2"] == pc_choose:
            print(x["draw"])
            print(x["result"])
            if x["result"]== "YOU WIN":
                score += 1
            if x["result"]== "YOU LOSE":
                score = -1
            break
    if score != -1:
        print("Your score is ",score)
        if input("Would you like to finish? ") == "yes":
            break       
    else:
        print("GAME OVER")
        break
        
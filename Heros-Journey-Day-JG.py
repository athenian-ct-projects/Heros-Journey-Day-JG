print("Hero's Journey choose your own adventure game \nby JG '23")

def fightmonster(partyMember):
  if partyMember > random.random():
    print ("you hit the monster")
    return True
  else:
    print("you miss")
    print ("you lost the fight")
    return False

def even_or_odd():
    x = int(input("enter a number between 1 and 6: "))
    if x %2 ==0:
        print ("go two steps")
    else:
      print(" go 1 step ")

def main():
  member = input("choose a party member 1-4")
  memNumber = int(member)
  if memNumber == 1:
    partyMember = partyMember1
  elif memNumber == 2:
    partyMember = partyMember2
  elif memNumber == 3:
    partyMember = partyMember3
  elif memNumber == 4:
    partyMember = partyMember4

  menuChoice = 0
  while menuChoice is not 3:
   menuChoice = input("""press 1 to roll the dice, press 2 to see if you won the fight against the monster, """)
   menuNumber = int(menuChoice)
   if menuNumber == 1:
    even_or_odd()
   elif menuNumber == 2:
    fightmonster(partyMember) 
   else:
    print("not a choice")

  

import random

baseFight=0.5
baseBribe=0.3
basePlead=0.2
potion=0.2
partyMember1 = baseFight + 0.3 + basePlead + 0.2 
partyMember2=  basePlead + 0.3
partyMember3=  baseBribe + 0.3
partyMember4=  basePlead + 0.3
#print(partyMember1)

random.randint(1,3)

even_or_odd()

main()

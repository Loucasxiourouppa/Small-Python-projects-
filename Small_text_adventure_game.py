import time # importing time module so theres a slight pause on every choice.

# user inputs
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# objects
knife = 0

required = ("\nUse only A, B, or C\n") # this cuts down on duplication

def intro ():
    '''This prints my intro'''
    print ("You Wake up in your bedroom confused and distraught, you dont remember anything ")
    print ("you remember your name and the fact that this is indeed your house")
    print ("you try to turn on the lights but they dont come on so you decide to leave your bedroom to see what is going on")
    print ("As you leave your room you also notice all the lights in the house are turned off")
    print ("All of a sudden you hear really loud footsteps running behind you and you look back and see a big monster. You decide to:")
    '''this is adds a 2 second delay to the text'''  
    time.sleep(2)
    '''this prints the first three choices the player will make'''
    print (" A. Run towards the stairs ")
    print (" B. Try and fight it ")
    print (" C. jump out of your bedroom window ")
    choice = input(">>> ") # this is the first choice.
    if choice in answer_A:
        down_stairs()
    elif choice in answer_B:
        print ("\nYou try and fight it however your punches go through the monster and it kills you with one swing of an axe. "
                   "\n\nYou Died!")
    elif choice in answer_C:
        jump_window()

    else:
        print (required)

    time.sleep(2)

def jump_window(): 
    print ("\nYou escape through the window injured and see the monster go in your basement."
           " You decide to:")
    time.sleep(1)
  
    print (" A. Run towards the main road ")
    print (" B. You run to the police station near you ")
    choice = input(">>> ")

    if choice in answer_A:
        print ("\nYou run towards the road and happen to trip because your injured and get run over by a car. "
                   "\n\nYou Died!")
    elif choice in answer_B:
            option_police()
    
    else:
        print (required)



def down_stairs():
    '''prints my second function'''
    print('You Run Downstairs,')
    print('As you are running down stairs you trip and fall down the stairs breaking your leg')
    print('you stand up and try to walk outside your house but the all the exit doors are locked')
    print('You decide to hide. You hide: ')
    time.sleep(1)
    print ("  A. under the kitchen table.")
    print ("  B. You hide in the laundry room. ")
    choice = input(">>> ")
    
    if choice in answer_A:
        print ("\nYou hide under the kitchen table however after a thorough look the monster spots you and kills you")
        print ("You Died!!!")

    elif choice in answer_B:
        laundry_room()


def laundry_room():
        
    print ("\nYou decided to hide in the laundry room however the monster tries to open the door, you decide to:")
    print (" A. Hide in the pile of clothes")
    print (" B. hide behind the door")
    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        
     print("\n The monster opens the door violently and looks around the room and doesnt spot you under the pile of clothes. After ")
     print("One hour later you come out and dont see any signs of the monster so you break the doors lock and run outside the house.")
     print ("You survived!!!")
     print ("You got the SURVIVOR ENDING!!")
  
  
    elif choice in answer_B:
     print ("You hide behind the door, however the monster opens the door violently hitting you and spotting you")
     print ("It kills you...")
     print ("You died!")


    choice = input ('>>> ')
    '''if choice if the player picks up the knife'''
    if choice in yes:
        knife = 1 #picks up knife
    else:
        knife = 0
    '''adds a second delay'''
    time.sleep(1)
    if knife > 0:
        print (' You Picked up the knife and slash the monster with it but it wasnt enough and it killed you.')
        print ('You Lost!')
    else:# if the user didnt pick up the knife then...
      print ('You Didnt pick up the knife to defend yourself, the monster took the chance and killed you. You Died!')


def option_police(): 
  print ("\nYou ran towards the police station and explain your story and the police officers believe you because of your injured body .")
  print ("They carry out a search at your house and they find nothing except the broken window  "
  "You decide to :")
  time.sleep(1)
  print ("  A. ask them to look again.")
  print ("  B.Check the basement where you saw the monster go after the attack. ")
  choice = input(">>> ")
  if choice in answer_A:
    print("\nYou asked the cops and investigate again and again but find nothing and conclude the investigation, believing there was nothing from the beggining and it was all in your head")
    print ("The Cops and therapist decide its best for your health to put you in a mental aslym, they dont believe you")
    print ("You let the monster get away and it will hurt more people."
           "\nYou got the BAD ENDING!")
  
  elif choice in answer_B:
      basement_level()



def basement_level():
  print ("\nYou convince the cops to check the basement where it is hidden and head down there with the cops.")
  print (" All of a sudden you and the cops hear a big deep growl and ahead there are two doors.")
  print (" You see a door that has a bright red light coming through the cracks of the door and another door where you hear the loud growls coming from"
           " You decide to: ")
  time.sleep(1)
  print (" A. check the door with the oozing red light ")
  print (" B. check the door where the loud growls can be heard coming from ")
  choice = input ('>>> ')
  if choice in answer_A:
         red_door()
     

  elif choice in answer_B:
        
    print (" You decide to check the door where the loud growls can be heard coming from.")
    print (" You open it and find the monster weeping because its trying to defend its family, however from the fear, the cops shoot the monster with all the ammo they have and dies.")
    print (" You got the WEIRD UNSATISFYING ENDING")


def red_door():
  
      print (" You open the door with the red light and see that its an old blade that is glowing red and shaking")
      print (" BAAM! the second door opens and its the monster, the cops shoot at it out of fear but the monster is enraged and doesnt go down.")
      print (" The monster is interested in the blade and charges at you, do you stab it with the blade? Y/N")
      choice = input ('>>> ')
      if choice in yes :
          knife = 1
      else:
        knife = 0

      time.sleep(1)
    
      if knife > 0 :
        print (" You Stabbed the monster! The monster weeps in agony and dies saving you and the cops with you. You Won!!!")
        print (" You got the GOOD ENDING")
      else:
        print (" Out of fear you dont have the courage to stab the monster which ends up killing you and the cops out of retaliation.")
        print (" The monster later on destroys the blade which makes it stronger")
        print (" You got the BAD ENDING ")




 

'''starts my main function'''  
intro()


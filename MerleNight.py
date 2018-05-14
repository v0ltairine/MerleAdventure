print("It's Merle's big night out.")
print("Does he choose option 1 and head into the yard? Or option 2, where he'd head into the alley between the houses?")
path = input("> ")

if path == "1" and "option 1":
    print("Risky choice!")
    print("Merle isn't sure what lies ahead so he crouches down as low as possible so he can stay below the grassline.")
    print("He's quite smart: no one can see him from that strategic level.")
    print("Does he approach the grass (a) or hang close to the fence (b)?")
    
    yard_decision = input("> ")
    
    if yard_decision == "a":
            print("Oh no! The jungle in front of him is FULL of VERY SCARY INSECTS! Abort mission.")
            print("Run back to the house as quickly as you can, and - importantly - as low as you can...")
    else:
            print("Merle almost makes it to the end of the yard when...WTF!") 
            print("A tiny dinosaur swoops in from nowhere and perches upon the chainlink next to Merle's head.")
            print("It's just too much. Merle must retreat. No man is brave enough for this...")

elif path == "2" and "option 2":
    print("Good choice. He feels much safer here.")
    print("Should he hang around and nibble at the paint chips (option 1) or venture even deeper into the alley? (option 2)")

    next_decision = input("> ")
    
    if next_decision == "1" and "option 1":
            print('"Yum!" says Merle. "Thanks for choosing this option!"')
    else:
            print("Oh no! Merle meets his match: a medium-sized spider lurking in the corner.")
            print("Looks like this is the end for our brave little man...")
else: 
	print("That's not a valid option for Merle. Game over since you can't play nicely.")


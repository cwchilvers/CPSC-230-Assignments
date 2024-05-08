# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Adventure Game


# import random module

import random

application = 1

while application == 1:
    # set game value
    Game = 1

    # set death variable

    death = random.randint(1, 100)

    # set counters
    please_counter = 0

    moron_counter = 0

    # ask usr to play game (usr actually doesn't have a choice)
    yn = input("\"Play ROOMS of DOOMS?\": (Y/N)\n")

    while Game == 1:

        # if yes
        if yn == "y" or yn == "Y" or yn == "Yes" or yn == "yes" or yn == "Yes!" or yn == "YES!":
            print("\"Yay!\"\n\n")
            Game = 2
            break

        # if no
        elif yn == "n" or yn == "N" or yn == "No" or yn == "NO" or yn == "No!" or yn == "NO!":
            if please_counter == 3:
                print("\"I heard a yes!\"\n\n")
                Game = 2
                break
            please_counter += 1
            yn = input("\"Please?\"\n")

        # if usr is dumb
        elif yn != "y" or yn != "Y" or yn != "Yes" or yn != "yes" or yn != "Yes!" or yn != "n" or yn != "N" or yn != "No" or yn != "NO" or yn != "No!" or yn != "YES!" or yn != "NO!":
            if moron_counter == 2:
                print("\"I guess I'll have to say yes for you!\"\n\n")
                Game = 2
                break
            moron_counter += 1
            yn = input("\"Are you stupid or something? Say YES or NO!\"\n")

    # game intro
    while Game == 2:
        # game intro
        print \
            ("\"Alright. You're in a castle. Find the treasure. Also, there's a high probability that you will "
             "die.\" \n\n... \n\n\"Good luck!\" \n\n")

        # start game
        Game = 3

        # create variables and set loop control variables
        room = 1
        chair_attempts = 0
        break

    # game begins
    while Game == 3:

        # death
        if room == 0:
            print("u dead\n\n\n")
            break

        # room 1W
        while room == 1:
            room_1 = input("There's nothing in this room except a door and a chair.\n"
                           "Open the door (1) or sit in the chair (2)?: (1/2)\n")
            # if usr chooses door
            if room_1 == "door" or room_1 == "Door" or room_1 == "DOOR" or room_1 == "Door." or room_1 == "1":
                print("You enter through the door.\n")
                room = 4
                death = random.randint(1, 100)
                break
            # if usr chooses chair
            elif room_1 == "chair" or room_1 == "Chair" or room_1 == "CHAIR" or room_1 == "Chair" or room_1 == "2":
                # death
                if death > 80:
                    print("You sit in the chair...\n")
                    print("...\n...\n...\n...")
                    print("You hear the sound of a conga line approaching.")
                    print("...\n...\n...\n...\n\n")
                    print("You are run over by a wild conga line.\n\n")
                    room = 0
                    break
                else:
                    if chair_attempts != 2:
                        print("You sit in the chair...\n")
                        print("...\n...\n...\n...")
                        print("Nothing happened.\n")
                        chair_attempts += 1
                        death = random.randint(1, 100)
                    # if usr keeps choosing chair
                    elif chair_attempts == 2:
                        print("DUDE! Stop Sitting in the chair!\n")
                        death = random.randint(1, 100)

        # room 2
        while room == 2:
            room_2 = input("Another boring room.\n"
                           "Go to the door on the left (1), the door in the middle (2), or the door \n"
                           "on the right(3)?: (1/2/3)\n")

            # if usr chooses 3
            if room_2 == "3":
                print("You proceed through the door on the right...\n")
                room = 3

            # if usr chooses 1
            elif room_2 == "1":
                if death > 45:
                    print("You enter through the door. As soon as you step into the next room, you fall through\n"
                          "the floor like a poorly designed video game.")
                    print("...\n...\n...\n...")
                    print("You keep falling...\n")
                    print("...\n...You fall for hours...\n...\n...")
                    room = 0
                else:
                    print("You enter the door on the left...\n"
                          "...\n"
                          "Hey, this looks familiar.\n\n")
                    death = random.randint(1, 100)
                    room = 2

            # if usr chooses 2
            elif room_2 == "2":
                if death > 75:
                    print("You enter through the door. As soon as you step into the next room, you fall through\n"
                          "the floor like a crappy video game.")
                    print("...\n...\n...\n...")
                    print("You keep falling...\n")
                    print("...\n...you fall for hours...\n...\n...")
                    room = 0
                else:
                    print("You enter through the door in the middle...\n"
                          "...\n"
                          "Hey, this looks familiar.\n\n")
                    death = random.randint(1, 100)
                    room = 2

        # room 3
        while room == 3:
            room_3 = input("You hear your thoughts reverberate all around you.\n"
                           "You're inside your mind.\n\n"
                           "Keep thinking of a way out (1) or stop thinking (2)?: (1/2)\n")

            # if usr chooses 2
            if room_3 == "2":
                print("You stop thinking....\n"
                      "...\n...\n...\n"
                      "You're out of your mind!\n\n")
                death = random.randint(1, 100)
                room = 5

            # if usr chooses 1
            elif room_3 == "1":
                if death > 35:
                    print("You exit the room the way you came in.\n")
                    room = 0
                else:
                    print("You exit the room the way you came in.\n")
                    room = 4

        # room 4
        while room == 4:
            room_4 = input("There appears to be another door at the end of the other end of the room, but there's a\n"
                           "bunch of obnoxious Chapman students in the way. Tell them to move it (1) or politely ask \n"
                           "them to let you through (2)?: (1/2)\n")
            # if usr chooses 1
            if room_4 == "1":
                print("Frustrated, you yell at the students blocking your path to move it.")
                print("...")
                print("...")
                print("The students begin to dance!\n")
                room = "4 part 2"
                break
            if room_4 == "2":
                print("You politely ask the students if they could let you through to access the other door\n")
                print("...")
                print("...")
                print("...")
                print("...")
                print("...")
                print("...")
                print("\"Yeah, go ahead.\"\n")
                print("The students move out of the way, leaving a pathway to the door on the other side.\n"
                      "You enter through the door.\n\n")
                death = random.randint(1, 100)
                room = 2
                break

        # room 4 (part 2)
        while room == "4 part 2":
            room_4part2 = input("The students form a conga line. Join in on the fun (1) or nah (2)?\n")
            # if yes
            if room_4part2 == "1":
                print("You take part in the conga line.")
                print("...")
                print("The conga line leads you to another room and falls apart. The students run away.\n")
                death = random.randint(1, 100)
                room = 1
                break
            # if no
            elif room_4part2 == "2":
                print("\"Come on, man. Join us!\" the students say unanimously.\n\n")
                print("Suddenly the gravitational pull of the conga line reels you in.\n"
                      "You have been assimilated into the conga line.\n"
                      "Being the mindless human being you are, you follow the conga line into another room.\n"
                      "The line falls apart and the students flee for no apparent reason.\n")
                # death
                if death > 85:
                    print("...")
                    print("...")
                    print("...")
                    room = 0
                else:
                    death = random.randint(1, 100)
                    room = 1
                    break

        # room 5
        while room == 5:
            print("\"Hello world.\"\n\n")
            room_5 = input("Ignore the greeting (1) or repeat greeting back (2)?: (1/2)\n")

            # if usr ignores
            if room_5 == "1":
                print("You have chosen... wisely.\n\n A door appears in front of you. You proceed through the door.\n\n")
                death = random.randint(1, 100)
                room = 6

            # if usr responds
            elif room_5 == "2":
                print("...\nMy name isn't World!\n...\n...\nDIE!\n\n")
                room = 0
                break

        # room 6
        while room == 6:
            room_6 = input("This appears to be the final room. However there's nothing here except for a cat\n"
                           "taking a nap on top of your laptop.\nYou have an assignment due online tonight.\n"
                           "You really need to access that laptop.\n\nYou walk up to the cat napping on your laptop.\n"
                           "You reach out and- \n\n"
                           "\"YO HOLD UP!\" exclaimed the cat.\n\n\"You tryin' to pet me without my consent? Not cool, man.\n"
                           "If you want this nice, warm laptop back, you must answer this question first.\"\n"
                           "\"You ready?\" (1 = \"Yes\", 2 = \"Hold on.\")")
            # if yes
            if room_6 == "1":
                room = "6 part 2"
            # if hold on
            elif room_6 == "2":
                print("Too late!")
                room = "6 part 2"

        # room 6 (part 2)
        while room == "6 part 2":
            cats = input("\"Alright. Here it goes.\"\n\n\"Do you like cats?\": (1 = \"Hell yeah!\", 2 = \"No.\")\n")

            # if no
            if cats == "2":
                print(
                    "\"Same! I HATE cats! I freaking hate cats so freaking much that I freakedy freak freaking freak frak!\"\n")
                print("\"Here. Have your laptop back.\"\n\n"
                      "The cat steps off of the laptop."
                      "...\n"
                      "\"Go,\" the cat begins to cry.\n \"Take it. Take your laptop.\" Tears roll down the cat's face.\n"
                      "\"The world is a sad and desolate place, at least that's what I used to think. Then you came into my life.\"\n"
                      "\"You showed me that's not always true. You lit up the dark room I dwelled in. You gave me inspiration.\n"
                      "\"You provided me an alternative to the way I perceive the world around me. The world needs more people like you.\"\n\n"
                      "You grab your laptop and open up your homework, which is already finished.\n"
                      "You open up Blackboard and locate the submission link for the assignment and attach the file.\n"
                      "You look at the cat before clicking the submit button.\n"
                      "The cat nods in approval.\n\n"
                      "\"Thank you,\" says the cat.\n"
                      "\"I'll never forget you.\"\n"
                      "You click \"submit\" and receive an email notification. You check your email.\n\n"
                      "\"Your submission to Blackboard has been received.\"")
                room = "end"
                break

            # if hell yeah
            elif cats == "1":
                # if hell yeah and unlucky
                if death > 25:
                    print("...\n...\n...\n")
                    room = 0
                    break
                # if hell yeah and lucky
                elif cats == "1" and death < 25:
                    print("Sorry, I couldn't hear you. Let me say that again.")
                    death = random.randint(1, 100)

    # ask to play again
    Game = "Play again"

    while Game == "Play again":
        again = input("Play again?: (Y/N)\n")
        if again == "y" or again == "Y":
            Game = 2
            break
        elif again == "n" or again == "N":
            application = 0
            break

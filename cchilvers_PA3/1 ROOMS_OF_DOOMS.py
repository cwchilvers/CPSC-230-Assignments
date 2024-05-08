
#set game
Game = 1

#ask usr to play game
oui_non = input("Play ROOMS of DOOMS?: (Y/N)\n")

#set counter
please_counter = 0

while True:

    #if yes
    if oui_non == "Y" or oui_non == "y" or oui_non == "はい" or oui_non == "yes" or oui_non == "Yes" or oui_non == "Yes!":
        print("Yay!\n \n")
        please_counter == 4
        break
    
    #if usr says no
    elif oui_non != "Y" or oui_non != "y" or oui_non != "はい" or oui_non != "yes" or oui_non != "Yes" or oui_non != "Yes!":
        
        #plead usr to say yes
        if oui_non == "N" or oui_non == "n" or oui_non == "no" or oui_non == "No" or oui_non == "NO" or oui_non == "いいえ":
            if please_counter == 0 and oui_non == "N" or oui_non == "n" or oui_non == "no" or oui_non == "No" or oui_non == "NO" or oui_non == "いいえ":
                oui_non == input("Please?")
                please_counter += 1
            elif please_counter == 1 and oui_non == "N" or oui_non == "n" or oui_non == "no" or oui_non == "No" or oui_non == "NO" or oui_non == "いいえ":
                oui_non == input("Pretty please?")
                please_counter += 1
            elif please_counter == 2 and oui_non == "N" or oui_non == "n" or oui_non == "no" or oui_non == "No" or oui_non == "NO" or oui_non == "いいえ":
                oui_non == input("PRETTY pretty please?")
                please_counter += 1
            elif please_counter == 3 and oui_non == "N" or oui_non == "n" or oui_non == "no" or oui_non == "No" or oui_non == "NO" or oui_non == "いいえ":
                print("I heard a yes!\n \n")
                please_counter += 1
            elif oui_non == "Y" or oui_non == "y" or oui_non == "はい" or oui_non == "yes" or oui_non == "Yes" or oui_non == "Yes!":
                print("Yay!\n \n")
                please_counter == 4
                break
            #if yes after first no
            elif oui_non == "Y" or oui_non == "y" or oui_non == "はい" or oui_non == "yes" or oui_non == "Yes" or oui_non == "Yes!":
                print("Yay!\n \n")
                please_counter == 4
                break
            #if usr is says something else
            elif oui_non != "Y" or oui_non != "y" or oui_non != "はい" or oui_non != "yes" or oui_non != "Yes" or oui_non != "Yes!":
                oui_non = input("Enter Y or N, moron!:\n")

    elif please_counter == 4:
        break
    



    


#create variable and set loop control variable
next_room = 1



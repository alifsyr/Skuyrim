# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import F01_createdragonborn, F02_attribute, F03_explore, F04_foundmonster, F05_foundgold, F06_shopping, F08_alduskuy, F09_switchcity, F10_help, F11_saveandloadgame, F12_exitgame

'''
Zachrandika Alif Syahreza
Dimas Farhan Anshari
Ali Zayn Murteza
Muhammad Erwin Fattah
Muhammad Farhan
'''


# KAMUS GLOBAL
'''
    dragonborn_data : array of array of string
    item_data       : array of array of string
    monster_data    : array of array of string
    sidequest_data  : array of array of string
'''

endprogram  = False
gold        = 100
currentUser = [" $NOUSER", "$NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"" $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]

print("Welcome to Skuyrim")
dragonborn_data, item_data, monster_data, sidequest_data = F11_saveandloadgame.load()

print("Choose your character or create new character :")
newChar, currentUser = F11_saveandloadgame.dataload (dragonborn_data, currentUser)

if (newChar):
    dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

while (not endprogram):
    command = str(input("$ ")).capitalize()

    if   command == "Status":
        F02_attribute.attribute(currentUser, gold)

    elif command == "Explore":
        result = F03_explore.explore(currentUser)
        if (result == "gold"):
            gold, currentUser = F05_foundgold.foundgold(currentUser, gold)

        else:
            currentUser, quit, create, gold = F04_foundmonster.foundmonster(currentUser, monster_data, gold)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "Shopping":
        gold, currentUser = F06_shopping.shop(currentUser, item_data, gold)

    elif command == "Alduskuy":
        foundmonster = False
        foundmonster, monster = F08_alduskuy.alduskuy(foundmonster)
        if (foundmonster):
            currentUser, quit, create, gold = F04_foundmonster.foundmonster(currentUser, monster, gold)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "Switch City":
        foundmonster = False
        currentUser, foundmonster = F09_switchcity.switchcity(currentUser, foundmonster)
        if(foundmonster):
            currentUser, quit, create, gold = F04_foundmonster.foundmonster(currentUser, monster_data, gold)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "Help":
        section = 0
        F10_help.help(section)
        
    elif command == "Save":
        data = [dragonborn_data, item_data, monster_data, sidequest_data]
        names = ["dragonborn.csv", "item.csv", "monster.csv", "sidequest.csv"]
        F11_saveandloadgame.save(data, names, currentUser)

    elif command == "Exit":
        simpan = F12_exitgame.exit()
        if (simpan):
            data = [dragonborn_data, item_data, sidequest_data]
            names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
            F11_saveandloadgame.save(data, names, currentUser)

        print("Thanks for playing skuyrim, goodbye!")
        endprogram = True
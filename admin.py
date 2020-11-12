import modules, F11_saveandloadgame, F12_exitgame,tabulate


dragonborn_data, item_data, monster_data, sidequest_data = F11_saveandloadgame.load()
endprogram = False
while (not endprogram):
    password = (input("Enter password: "))
    if password == 'akusukakamu':
        print("Welcome!")
        print("What database do you want to user? (1 - item, 2 - monster)")
        database = int(input("database: ")) #awal lgsg muncul ini
        printitem(item_data, monster_data, database)
    
        while (not endprogram):
            command = str(input("$ "))
            if command == "switch":
                print("What database do you want to user? (1 - item, 2 - monster)")
                database = int(input("database: "))
                printitem(item_data,monster_data,database)

            elif command == "add":
                item_name = str(input("item name: "))
                item_atk = str(input("item atk: "))
                item_def = str(input("item deff: "))
                item_luck = str(input("item luck: "))
                item_health = str(input("item health: "))
                item_magic = str(input("item magic: "))
                item_gold = str(input("item gold: "))
                item_region = str(input("item region(1 for windhelm, 2 for solitude): "))
                item_data += [[str(modules.generateid(item_data)),item_name,item_atk,item_magic,item_def,item_luck,item_health,item_region,item_gold]] #masukin ke array sementara (magic sm price ga ada di spesifikasi)
                print("data successfully added to database")
            elif command == "delete":
                for i in item_arr: #display data item
                    if i[1] != "Nama" or i[2]!="Attack" or i[3]!="Magic" or i[4] != "Defense" or i[5] != "Luck" or i[6] != 'HP' or i[7] != "City" or i[8] != "Price":
                        print(i[0]+". "+i[1]+"|"+i[2]+" atk|"+i[4]+" def|"+i[5]+" luck|"+i[6]+" health|"+i[3]+" magic|"+i[7]+"|"+i[8]+" gold")
                delete = input("Which number: ")
                for i in item_arr:
                    if i[1] != "Nama" or i[2]!="Attack" or i[3]!="Magic" or i[4] != "Defense" or i[5] != "Luck" or i[6] != 'HP' or i[7] != "City" or i[8] != "Price":
                        if i[0] != delete:
                            print(i[1]+"|"+i[2]+" atk|"+i[4]+" def|"+i[5]+" luck|"+i[6]+" health|"+i[3]+" magic|"+i[7]+"|"+i[8]+" gold") #baru di display doang blm dihapus di arraynya
                new_item_arr = []
                for i in item_arr:
                    if i[0] != delete:
                        new_item_arr +=[i]
                item_arr = new_item_arr
                item_data = new_item_arr
            elif command == "save":
                data = [dragonborn_data, item_data, monster_data, sidequest_data]
                names = ["dragonborn.csv", "item.csv", "monster.csv", "sidequest.csv"]
                F11_saveandloadgame.saveadmin(data, names)
            elif command == "exit":
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.saveadmin(data, names)
                endprogram = True
    else:
        print("Password salah!")

def printdata(item_data, monster_data, database):
    data = []
    if database == 1:
        print("Showing data of all item:")
        for i in item_data: #display data item
            if i[1] != "Nama":
                data += [i]
        print(tabulate.tabulate(item,headers = ['ID','Nama','Attack','Magic','Defense','Luck','HP','City','Price']))
    elif database == 2:     #displaymonster
        print("Showing data of all monster:")
        for i in monster_data:
            if i[1]!= 'Nama' or i[2] !='Attack' or i[3] !='Defense' or i[4] != "HP":
                data += [i]
        print(tabulate.tabulate(item,headers = ['ID','Nama','Attack','Defense','HP']))
def introSession():
    print("Pilih role:\n1. Admin\n2. User")

def adminSession():
    print("1. Daftarkan User\n2. Cari Item Berdasarkan Rarity\n3. Cari Item Berdasarkan Tahun")

def userSession():
    print("1. Cari Item Berdasarkan Rarity\n2. Cari Item Berdasarkan Tahun")

def printGroup(i,array_of_gadget):
    print("Nama             : ", array_of_gadget[i][1])
    print("Deskripsi        : ", array_of_gadget[i][2])
    print("Jumlah           : ", array_of_gadget[i][3], " buah")
    print("Rarity           : ", array_of_gadget[i][4])
    print("Tahun Ditemukan  : ", array_of_gadget[i][5])
    print()

def findGadgetByRarity(rarity, array_of_gadget):
    n = len(array_of_gadget)
    for i in range(1,n):
        if array_of_gadget[i][4] == rarity:
            printGroup(i,array_of_gadget)

def findGadgetByYear(year, operator, array_of_gadget):
    n = len(array_of_gadget)
    for i in range(1,n):
        if operator == '=':
            if int(array_of_gadget[i][5]) == year:
                printGroup(i, array_of_gadget)
        elif operator == '<':
            if int(array_of_gadget[i][5]) < year:
                printGroup(i, array_of_gadget)
        elif operator == '>':
            if int(array_of_gadget[i][5]) > year:
                printGroup(i, array_of_gadget)    
        elif operator == '>=':
            if int(array_of_gadget[i][5]) >= year:
                printGroup(i, array_of_gadget)
        else:
            if int(array_of_gadget[i][5]) <= year:
                printGroup(i, array_of_gadget)
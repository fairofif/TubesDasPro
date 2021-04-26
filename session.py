def adminSession():
    print("1. Daftarkan User\n2. Cari Item Berdasarkan Rarity\n3. Cari Item Berdasarkan Tahun")

def userSession():
    print("1. Cari Item Berdasarkan Rarity\n2. Cari Item Berdasarkan Tahun")

def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    else:
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()

def findGadgetByRarity(rarity, arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i][4] == rarity:
            printGroup(i,arr)

def findGadgetByYear(year, operator, arr):
    n = len(arr)
    for i in range(1,n):
        if operator == '=':
            if int(arr[i][5]) == year:
                printGroup(i, arr)
        elif operator == '<':
            if int(arr[i][5]) < year:
                printGroup(i, arr)
        elif operator == '>':
            if int(arr[i][5]) > year:
                printGroup(i, arr)    
        elif operator == '>=':
            if int(arr[i][5]) >= year:
                printGroup(i, arr)
        else:
            if int(arr[i][5]) <= year:
                printGroup(i, arr)